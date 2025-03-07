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
	uv run gendiff gendiff/tests/test_files/file1.json gendiff/tests/test_files/file2.yml

lint:
	uv run ruff check gendiff

lint-with-fix:	
	uv run ruff check --fix gendiff

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report xml

check: test lint