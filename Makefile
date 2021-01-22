install:
	poetry install

gendiff:
	poetry run gendiff

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	pip install --force --user dist/*.whl

lint:
	poetry run flake8 brain_games

.PHONY: install
