# انتشار Bale Session در GitHub و PyPI

## بررسی محلی

```bash
python scripts/generate_proto.py --check
pytest -q
ruff check .
ruff format --check .
mypy src
git diff --check
```

## ساخت بسته

```bash
python -m pip install --upgrade build twine
python -m build
twine check dist/*
```

قبل از انتشار، نسخهٔ `project.version` در `pyproject.toml` را افزایش دهید و
اطمینان حاصل کنید که هیچ session، JWT، cookie، trace یا دادهٔ شخصی در commit و
بسته وجود ندارد.

## انتشار

```bash
twine upload dist/*
```

نام بستهٔ PyPI `bale-session` است، اما import عمومی آن `bale` است:

```bash
pip install bale-session
```

توکن PyPI را فقط از keyring یا متغیر محیطی امن به ابزار انتشار بدهید و هرگز در
shell history، README یا فایل پروژه ذخیره نکنید.
