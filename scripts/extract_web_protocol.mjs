#!/usr/bin/env node
/**
 * Recover Bale gRPC-Web services and protobuf codec shapes from official web
 * JavaScript bundles.
 *
 * This reads public, already-downloaded assets only. It never reads browser
 * storage, cookies, session files, or message payloads.
 */

import fs from "node:fs";
import path from "node:path";
import process from "node:process";
import { createRequire } from "node:module";

const require = createRequire(import.meta.url);
const acorn = require("acorn");
const walk = require("acorn-walk");

const SCALAR_READERS = new Set([
  "bool",
  "bytes",
  "double",
  "fixed32",
  "fixed64",
  "float",
  "int32",
  "int64",
  "sfixed32",
  "sfixed64",
  "sint32",
  "sint64",
  "string",
  "uint32",
  "uint64",
]);

function usage() {
  console.error(
    "usage: node scripts/extract_web_protocol.mjs BUNDLE_DIR [OUTPUT.json]",
  );
  process.exit(2);
}

function propertyName(property) {
  if (!property || property.type !== "Property") return null;
  if (!property.computed && property.key.type === "Identifier") {
    return property.key.name;
  }
  if (property.key.type === "Literal") return String(property.key.value);
  return null;
}

function objectProperties(node) {
  const result = new Map();
  if (!node || node.type !== "ObjectExpression") return result;
  for (const property of node.properties) {
    const name = propertyName(property);
    if (name !== null) result.set(name, property.value);
  }
  return result;
}

function literalString(node) {
  return node?.type === "Literal" && typeof node.value === "string"
    ? node.value
    : null;
}

function identifierName(node) {
  return node?.type === "Identifier" ? node.name : null;
}

function memberName(node) {
  if (!node || node.type !== "MemberExpression") return null;
  if (!node.computed && node.property.type === "Identifier") {
    return node.property.name;
  }
  if (node.property.type === "Literal") return String(node.property.value);
  return null;
}

function functionBody(node) {
  if (
    node &&
    (node.type === "FunctionExpression" ||
      node.type === "ArrowFunctionExpression")
  ) {
    return node.body;
  }
  return null;
}

function moduleFunctions(ast) {
  const modules = new Map();

  function addObject(object) {
    if (!object || object.type !== "ObjectExpression") return;
    for (const property of object.properties) {
      const id = propertyName(property);
      if (id !== null && functionBody(property.value)) {
        modules.set(id, property.value);
      }
    }
  }

  walk.simple(ast, {
    VariableDeclarator(node) {
      if (
        node.id.type === "Identifier" &&
        node.id.name === "__webpack_modules__"
      ) {
        addObject(node.init);
      }
    },
    CallExpression(node) {
      if (memberName(node.callee) !== "push") return;
      const payload = node.arguments[0];
      if (payload?.type !== "ArrayExpression") return;
      addObject(payload.elements[1]);
    },
  });
  return modules;
}

function defaultValue(node) {
  if (!node) return "unknown";
  if (node.type === "ArrayExpression") return "repeated";
  if (node.type === "ObjectExpression") return "map_or_message";
  if (node.type === "Literal") {
    if (node.value === null) return "null";
    if (typeof node.value === "boolean") return "bool";
    if (typeof node.value === "number") return "number";
    if (typeof node.value === "string") return "string";
  }
  if (node.type === "UnaryExpression" && node.operator === "!") return "bool";
  if (node.type === "Identifier" && node.name === "undefined") {
    return "message_or_optional";
  }
  if (
    node.type === "UnaryExpression" &&
    node.operator === "void" &&
    node.argument.type === "Literal" &&
    node.argument.value === 0
  ) {
    return "message_or_optional";
  }
  if (node.type === "NewExpression") return "message_or_bytes";
  return "unknown";
}

function codecRef(node, context) {
  if (!node) return null;
  if (node.type === "Identifier") {
    return `${context.moduleId}:local:${node.name}`;
  }
  if (node.type === "MemberExpression") {
    const exported = memberName(node);
    const alias = identifierName(node.object);
    if (alias && exported && context.imports.has(alias)) {
      return `${context.imports.get(alias)}:export:${exported}`;
    }
    if (alias && exported) return `${context.moduleId}:member:${alias}.${exported}`;
  }
  return null;
}

function readerType(expression, context) {
  let wrapper = false;
  let node = expression;
  if (node?.type === "MemberExpression" && memberName(node) === "value") {
    wrapper = true;
    node = node.object;
  }

  if (node?.type === "CallExpression") {
    const method = memberName(node.callee);
    if (SCALAR_READERS.has(method)) {
      return { type: method, reference: null, wrapper };
    }
    if (method === "decode") {
      return {
        type: "message",
        reference: codecRef(node.callee.object, context),
        wrapper,
      };
    }
  }

  let found = null;
  if (node) {
    walk.simple(node, {
      CallExpression(call) {
        const method = memberName(call.callee);
        if (!found && SCALAR_READERS.has(method)) found = method;
      },
    });
  }
  return { type: found ?? "unknown", reference: null, wrapper };
}

function encodeFields(codec, context, defaults) {
  const encode = objectProperties(codec).get("encode");
  const body = functionBody(encode);
  if (!body) return [];
  const messageName = identifierName(encode.params?.[0]);
  if (!messageName) return [];
  const found = new Map();

  walk.ancestor(body, {
    CallExpression(node, ancestors) {
      if (
        memberName(node.callee) !== "uint32" ||
        node.arguments[0]?.type !== "Literal" ||
        typeof node.arguments[0].value !== "number"
      ) {
        return;
      }
      const tag = node.arguments[0].value;
      const number = tag >>> 3;
      if (!number) return;

      let name = null;
      let repeated = false;
      let map = false;
      const forOf = [...ancestors]
        .reverse()
        .find((item) => item.type === "ForOfStatement");
      if (
        forOf?.right?.type === "MemberExpression" &&
        identifierName(forOf.right.object) === messageName
      ) {
        name = memberName(forOf.right);
        repeated = true;
      }

      const searchAncestors = [...ancestors].reverse();
      for (const ancestor of searchAncestors) {
        if (name || ancestor === body) break;
        walk.simple(ancestor, {
          MemberExpression(member) {
            if (!name && identifierName(member.object) === messageName) {
              name = memberName(member);
            }
          },
        });
      }
      if (!name) return;
      const defaultNode = defaults.get(name);
      repeated ||= defaultNode?.type === "ArrayExpression";
      map = defaultNode?.type === "ObjectExpression";
      repeated ||= map;

      let type = "unknown";
      let reference = null;
      for (const ancestor of searchAncestors) {
        if (ancestor.type !== "CallExpression") continue;
        const method = memberName(ancestor.callee);
        if (ancestor === node && method === "uint32") continue;
        if (SCALAR_READERS.has(method)) {
          type = method;
          break;
        }
        if (method === "encode") {
          type = "message";
          reference = codecRef(ancestor.callee.object, context);
          break;
        }
      }
      if (type === "unknown" && forOf) {
        walk.simple(forOf.body, {
          CallExpression(call) {
            const method = memberName(call.callee);
            if (type === "unknown" && SCALAR_READERS.has(method)) type = method;
            if (type === "unknown" && method === "encode") {
              type = "message";
              reference = codecRef(call.callee.object, context);
            }
          },
        });
      }
      found.set(number, {
        number,
        name,
        repeated,
        map,
        type,
        reference,
        wrapper: false,
        default: defaultValue(defaultNode),
      });
    },
  });
  return [...found.values()];
}

function codecFields(codec, context) {
  const properties = objectProperties(codec);
  const decode = properties.get("decode");
  const body = functionBody(decode);
  if (!body || body.type !== "BlockStatement") return [];

  let baseName = null;
  let defaults = new Map();
  walk.simple(body, {
    VariableDeclarator(node) {
      if (node.id.type !== "Identifier") {
        return;
      }
      let candidate = objectProperties(node.init);
      if (
        node.init?.type === "CallExpression" &&
        node.init.callee.type === "Identifier"
      ) {
        candidate = context.factories.get(node.init.callee.name) ?? candidate;
      }
      if (candidate.size > defaults.size) {
        baseName = node.id.name;
        defaults = candidate;
      }
    },
  });

  // Newer ts-proto output initializes messages through a createBase helper.
  // If that helper is empty (or unavailable), infer the message variable from
  // the object receiving assignments/pushes in decoder switch cases.
  if (!baseName) {
    const candidates = new Map();
    walk.simple(body, {
      AssignmentExpression(node) {
        if (node.left.type !== "MemberExpression") return;
        const direct = identifierName(node.left.object);
        const nested =
          node.left.object.type === "MemberExpression"
            ? identifierName(node.left.object.object)
            : null;
        const name = direct ?? nested;
        if (name) candidates.set(name, (candidates.get(name) ?? 0) + 1);
      },
      CallExpression(node) {
        if (memberName(node.callee) !== "push") return;
        const target = node.callee.object;
        if (target?.type !== "MemberExpression") return;
        const name = identifierName(target.object);
        if (name) candidates.set(name, (candidates.get(name) ?? 0) + 1);
      },
    });
    if (candidates.size) {
      baseName = [...candidates].sort((a, b) => b[1] - a[1])[0][0];
      walk.simple(body, {
        VariableDeclarator(node) {
          if (identifierName(node.id) !== baseName) return;
          if (
            node.init?.type === "CallExpression" &&
            node.init.callee.type === "Identifier"
          ) {
            defaults = context.factories.get(node.init.callee.name) ?? defaults;
          }
        },
      });
    }
  }

  const fields = new Map();
  walk.simple(body, {
    SwitchCase(node) {
      if (node.test?.type !== "Literal" || typeof node.test.value !== "number") {
        return;
      }
      const number = node.test.value;
      let discovered = null;
      const block = { type: "BlockStatement", body: node.consequent };
      walk.simple(block, {
        AssignmentExpression(assignment) {
          const left = assignment.left;
          if (left.type !== "MemberExpression") return;
          if (identifierName(left.object) === baseName) {
            const name = memberName(left);
            if (!name) return;
            discovered = {
              number,
              name,
              repeated: false,
              map: false,
              ...readerType(assignment.right, context),
            };
            return;
          }
          // map<K,V>: message.map[entry.key] = entry.value
          const mapTarget = left.object;
          if (
            mapTarget.type === "MemberExpression" &&
            identifierName(mapTarget.object) === baseName
          ) {
            const name = memberName(mapTarget);
            if (!name) return;
            let decoded = null;
            walk.simple(block, {
              CallExpression(call) {
                if (!decoded && memberName(call.callee) === "decode") {
                  decoded = {
                    type: "message",
                    reference: codecRef(call.callee.object, context),
                    wrapper: false,
                  };
                }
              },
            });
            discovered = {
              number,
              name,
              repeated: true,
              map: true,
              ...(decoded ?? readerType(assignment.right, context)),
            };
          }
        },
        CallExpression(call) {
          if (memberName(call.callee) !== "push") return;
          const target = call.callee.object;
          if (
            target?.type !== "MemberExpression" ||
            identifierName(target.object) !== baseName
          ) {
            return;
          }
          const name = memberName(target);
          if (!name) return;
          discovered = {
            number,
            name,
            repeated: true,
            map: false,
            ...readerType(call.arguments[0], context),
          };
        },
      });
      if (discovered) fields.set(number, discovered);
    },
  });

  for (const encoded of encodeFields(codec, context, defaults)) {
    const existing = fields.get(encoded.number);
    if (!existing || existing.type === "unknown") fields.set(encoded.number, encoded);
  }

  for (const [name, value] of defaults) {
    if ([...fields.values()].some((field) => field.name === name)) continue;
    fields.set(1_000_000 + fields.size, {
      number: null,
      name,
      repeated: value.type === "ArrayExpression",
      map: value.type === "ObjectExpression",
      type: "unknown",
      reference: null,
      wrapper: false,
    });
  }

  return [...fields.values()]
    .map((field) => ({
      ...field,
      default: defaultValue(defaults.get(field.name)),
    }))
    .sort((a, b) => (a.number ?? 1e9) - (b.number ?? 1e9));
}

function wrapperCodecReference(wrapper, method, context) {
  const body = functionBody(wrapper);
  if (!body) return null;
  let result = null;
  walk.simple(body, {
    CallExpression(node) {
      if (memberName(node.callee) !== method) return;
      const candidate = codecRef(node.callee.object, context);
      if (candidate && !result) result = candidate;
    },
  });
  return result;
}

function exportedCodecs(body, context, localCodecs) {
  const exports = new Map();
  walk.simple(body, {
    CallExpression(node) {
      if (memberName(node.callee) !== "d") return;
      for (const argument of node.arguments.slice(1)) {
        if (argument?.type !== "ObjectExpression") continue;
        for (const property of argument.properties) {
          const exported = propertyName(property);
          if (!exported) continue;
          const value = property.value;
          if (value.type === "ArrowFunctionExpression") {
            if (value.body.type === "Identifier" && localCodecs.has(value.body.name)) {
              exports.set(exported, `${context.moduleId}:local:${value.body.name}`);
            }
          } else if (value.type === "Identifier" && localCodecs.has(value.name)) {
            exports.set(exported, `${context.moduleId}:local:${value.name}`);
          } else {
            const props = objectProperties(value);
            if (props.has("encode") && props.has("decode")) {
              const id = `${context.moduleId}:inline:${exported}`;
              context.codecs.set(id, {
                id,
                module: context.moduleId,
                local_name: null,
                export_name: exported,
                fields: codecFields(value, context),
              });
              exports.set(exported, id);
            }
          }
        }
      }
    },
  });
  return exports;
}

function analyzeModule(moduleId, fn, sourceFile, state) {
  const body = functionBody(fn);
  if (!body || body.type !== "BlockStatement") return;
  const requireName = identifierName(fn.params[2]);
  const context = {
    moduleId,
    imports: new Map(),
    factories: new Map(),
    codecs: state.codecs,
  };

  walk.simple(body, {
    VariableDeclarator(node) {
      if (
        node.id.type === "Identifier" &&
        node.init?.type === "CallExpression" &&
        identifierName(node.init.callee) === requireName &&
        node.init.arguments[0]?.type === "Literal"
      ) {
        context.imports.set(node.id.name, String(node.init.arguments[0].value));
      }
    },
    FunctionDeclaration(node) {
      if (!node.id) return;
      let returned = null;
      walk.simple(node.body, {
        ReturnStatement(statement) {
          if (!returned && statement.argument?.type === "ObjectExpression") {
            returned = objectProperties(statement.argument);
          }
        },
      });
      if (returned) context.factories.set(node.id.name, returned);
    },
  });

  const services = new Map();
  const localCodecs = new Map();
  walk.simple(body, {
    VariableDeclarator(node) {
      if (node.id.type !== "Identifier" || node.init?.type !== "ObjectExpression") {
        return;
      }
      const props = objectProperties(node.init);
      const service = literalString(props.get("serviceName"));
      if (service) services.set(node.id.name, service);
      if (props.has("encode") && props.has("decode")) {
        localCodecs.set(node.id.name, node.init);
      }
    },
  });

  for (const [name, codec] of localCodecs) {
    const id = `${moduleId}:local:${name}`;
    state.codecs.set(id, {
      id,
      module: moduleId,
      local_name: name,
      export_name: null,
      fields: codecFields(codec, context),
    });
  }

  const exports = exportedCodecs(body, context, localCodecs);
  for (const [name, target] of exports) {
    state.exports.set(`${moduleId}:export:${name}`, target);
    const codec = state.codecs.get(target);
    if (codec && codec.export_name === null) codec.export_name = name;
  }

  walk.simple(body, {
    ObjectExpression(node) {
      const props = objectProperties(node);
      const method = literalString(props.get("methodName"));
      const serviceVariable = identifierName(props.get("service"));
      if (!method || !serviceVariable || !services.has(serviceVariable)) return;
      const requestType = props.get("requestType");
      const responseType = props.get("responseType");
      const requestWrapper = objectProperties(requestType).get("serializeBinary");
      const responseWrapper = objectProperties(responseType).get("deserializeBinary");
      state.methods.push({
        service: services.get(serviceVariable),
        method,
        request_stream: props.get("requestStream")?.value === true,
        response_stream: props.get("responseStream")?.value === true,
        request_codec: wrapperCodecReference(
          requestWrapper,
          "encode",
          context,
        ),
        response_codec: wrapperCodecReference(
          responseWrapper,
          "decode",
          context,
        ),
        module: moduleId,
        source: sourceFile,
      });
    },
  });
}

function resolveReference(reference, exports) {
  let current = reference;
  const seen = new Set();
  while (current && exports.has(current) && !seen.has(current)) {
    seen.add(current);
    current = exports.get(current);
  }
  return current;
}

function main() {
  const bundleDirectory = process.argv[2];
  const outputPath = process.argv[3] ?? null;
  if (!bundleDirectory) usage();

  const state = { codecs: new Map(), exports: new Map(), methods: [] };
  const files = fs
    .readdirSync(bundleDirectory)
    .filter((name) => name.endsWith(".js"))
    .sort();
  const releases = new Set();
  let parsedFiles = 0;
  let moduleCount = 0;

  for (const name of files) {
    const filename = path.join(bundleDirectory, name);
    const source = fs.readFileSync(filename, "utf8");
    const release = source.match(/SENTRY_RELEASE=\{id:"([^"]+)"\}/)?.[1];
    if (release) releases.add(release);
    let ast;
    try {
      ast = acorn.parse(source, {
        ecmaVersion: "latest",
        sourceType: "script",
        allowHashBang: true,
      });
    } catch (error) {
      console.error(`skip ${name}: ${error.message}`);
      continue;
    }
    parsedFiles += 1;
    for (const [moduleId, fn] of moduleFunctions(ast)) {
      moduleCount += 1;
      analyzeModule(moduleId, fn, name, state);
    }
  }

  for (const codec of state.codecs.values()) {
    for (const field of codec.fields) {
      field.reference = resolveReference(field.reference, state.exports);
    }
  }
  for (const method of state.methods) {
    method.request_codec = resolveReference(method.request_codec, state.exports);
    method.response_codec = resolveReference(method.response_codec, state.exports);
    method.request_fields = state.codecs.get(method.request_codec)?.fields ?? [];
    method.response_fields = state.codecs.get(method.response_codec)?.fields ?? [];
  }

  const methods = state.methods.sort((a, b) =>
    `${a.service}/${a.method}`.localeCompare(`${b.service}/${b.method}`),
  );
  const uniqueMethods = new Set(methods.map((x) => `${x.service}/${x.method}`));
  const services = [...new Set(methods.map((x) => x.service))].sort();
  const codecs = Object.fromEntries(
    [...state.codecs.entries()].sort(([a], [b]) => a.localeCompare(b)),
  );
  const document = {
    format: "bale-web-protocol-ast",
    format_version: 1,
    releases: [...releases].sort(),
    source: {
      bundle_directory: path.resolve(bundleDirectory),
      javascript_files: files.length,
      parsed_files: parsedFiles,
      webpack_modules: moduleCount,
    },
    counts: {
      services: services.length,
      methods: uniqueMethods.size,
      method_descriptors: methods.length,
      codecs: Object.keys(codecs).length,
      codec_fields: Object.values(codecs).reduce(
        (total, codec) => total + codec.fields.length,
        0,
      ),
    },
    services,
    methods,
    codecs,
  };
  const rendered = `${JSON.stringify(document, null, 2)}\n`;
  if (outputPath) fs.writeFileSync(outputPath, rendered, { mode: 0o600 });
  else process.stdout.write(rendered);
}

main();
