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
	uv run gendiff gendiff/test_files/file1.json gendiff/test_files/file2.json

lint:
	uv run ruff check gendiff
