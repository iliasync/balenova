# Account-session compatibility audit

Sources checked on 2026-08-31:

- the public JavaScript chunks served by `https://web.bale.ai/` (including the
  service descriptors and protobuf codecs in `index.637d04713b.js`), and
- Balethon commit `a98aa699847ca09ed42ea93eb498581ceb8bb761`.
- `Zellias/balejs` commit `c288e695f4f1fd4229b05a1a582c8b86e7ad8157`.

The public Web bundle marks the following account-session RPCs as unary calls.
The Files service is gRPC-Web; the messaging/auth/groups/users calls are also
available through the WebSocket envelope used by this client.

| Service | RPC | Local method | Status | Verification |
| --- | --- | --- | --- | --- |
| `bale.auth.v1.Auth` | `StartPhoneAuth`, `ValidateCode`, `ValidatePassword`, `SignUp` | `start_phone_auth`, `validate_code`, `validate_password`, `sign_up` | implemented | Web + Balethon + local proto |
| `bale.auth.v1.Auth` | `GetAuthSessions`, `TerminateSession`, `TerminateAllSessions`, `GetJWTToken`, `SignOut` | matching snake_case methods | implemented | Web + local proto |
| `bale.messaging.v2.Messaging` | `LoadDialogs`, `LoadHistory`, `SendMessage`, `UpdateMessage`, `DeleteMessage`, `ForwardMessages` | matching methods | implemented | Web + Balethon + local proto |
| `bale.messaging.v2.Messaging` | reactions, views, pin/unpin, multi-media | matching methods | implemented | Web + local proto |
| `ai.bale.server.Files` | `GetNasimFileUrl`, `GetNasimFileUrls`, `GetNasimFilePublicUrl` | `get_file`, `get_file_urls`, `get_file_public_url` | implemented | Web + Balethon; `file_urls` is repeated |
| `ai.bale.server.Files` | `GetNasimFileUploadUrl`, `GetNasimFileUploadResume`, `FileUploadCancel` | matching upload methods | implemented | Web + Balethon + local tests |
| `bale.v1.Configs` | `GetParameters`, `EditParameter` | `get_parameters`, `edit_parameter` | implemented | Web; `parameters` is repeated |
| `bale.messaging.v2.Messaging` | `LoadDialogs` peer-only responses | `get_dialogs_by_type`, `get_groups`, `get_channels`, `get_private_chats`, `get_bots` | implemented | live Web; resolves `user_peers`/`group_peers` read-only |
| `bale.users.v1.Users` | `GetFullUser`, `LoadFullUsersSequentially` | `get_full_user`, `load_full_users_sequentially` | implemented | Web codec + local proto/tests |
| `bale.users.v1.Users` | `EditAvatar`, `RemoveAvatar`, `LoadAvatars` | `edit_avatar`, `remove_avatar`, `load_user_avatars` | implemented | Web codec + local proto/tests |
| `bale.users.v1.Users` | `GetContacts`, `AddContact`, `RemoveContact`, `SearchContacts` | matching snake_case methods | implemented | Web codec + local proto/tests |
| `bale.users.v1.Users` | `BlockUser`, `UnblockUser`, `LoadBlockedUsers` | matching snake_case methods | implemented | Web codec + local proto/tests |
| `bale.users.v1.Users` | `GetUserPrivacyStatus`, `SetUserPrivacyStatus`, `GetUserFullPrivacy` | matching snake_case methods | implemented | Web codec + local proto/tests |
| `bale.users.v1.Users` | sex, birth date, time zone, preferred languages, local name | matching `edit_*` methods | implemented | Web codec + local proto/tests |

## Scope decisions

Balethon’s ordinary surface is Bot API (webhooks, `getUpdates`, bot payments,
inline bot callbacks, and bot-only update objects). Those methods are excluded
from this account-session library. Web methods that delete/reset account data,
change account security or phone ownership, upload a complete address book, or
manage cards are also intentionally not exposed as high-level wrappers. This
includes `DeleteAccount`, `LogOut`, password/2FA RPCs, `ChangePhoneNumber`,
`ConfirmPhoneNumber`, `ResetContacts`, `ImportContacts`, `AddCard`, and the
default-card mutations. `NotifyAboutDeviceInfo` remains internal because it is
Web-client telemetry rather than a user-facing account operation. Unknown or
minified codecs are documented as unsupported rather than guessed.

## Newly verified Users schemas

The current bundle provides complete codecs and field numbers for the following
previously unsupported account-session methods:

- profile: `EditSex`, `EditBirthDate`, `EditAvatar`, `RemoveAvatar`,
  `EditMyTimeZone`, `EditMyPreferredLanguages`, `EditUserLocalName`,
  `GetFullUser`, and `LoadFullUsersSequentially`;
- avatars and blocks: `LoadAvatars`, `BlockUser`, `UnblockUser`, and
  `LoadBlockedUsers`;
- contacts: `GetContacts`, `AddContact`, and `RemoveContact`;
- privacy: `GetUserPrivacyStatus`, `SetUserPrivacyStatus`, and
  `GetUserFullPrivacy`.

All are unary RPC descriptors on `bale.users.v1.Users`. Their source proto
messages, generated modules, wrappers, int32/int64 boundary checks, and fake
transport tests are now present locally. They have not been exercised against a
live account in this audit.

The local session smoke run successfully exercised `get_me`,
`get_auth_sessions`, `get_parameters`, `load_dialogs`, `get_chat`,
`load_users`, `load_full_users`, `load_history`, `get_call_logs`, and
`get_ongoing_calls`. No mutating RPC was sent.

## File schema correction

The current Web codec decodes `GetNasimFileUrls` as
`repeated FileUrlDescription file_urls = 1` and `GetParameters` as
`repeated ExtKeyValue parameters = 1`. The source protos and generated modules
in this repository now match those wire shapes. Older recordings that use the
singular `file_url`/`params` names can still be consumed by the client’s
compatibility fallback where applicable.
