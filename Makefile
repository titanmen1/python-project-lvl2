# Makefile
install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python -m pip install dist/*.whl

package-remove:
	python -m pip uninstall hexlet-code

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest -vv

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml