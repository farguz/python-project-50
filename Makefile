install:
	uv sync

build:
	uv build

package-install:
	uv tool install dist/*.whl

package-uninstall:
	rm -r -f dist/
	uv tool uninstall hexlet-code

gendiff:
	uv run gendiff

lint:
	uv run ruff check gendiff
