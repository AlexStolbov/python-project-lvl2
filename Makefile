install:
	poetry install

gendiff:
	poetry run gendiff

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --force --user dist/*.whl

lint:
	poetry run flake8 hexlet_python_package
	poetry run flake8 tests

run3:
	poetry run gendiff -f j tests/fixtures/step3/lvl2_original.json tests/fixtures/step3/lvl2_modified.json

run3abs:
	poetry run gendiff -f j ~/all/PythonProjects/Hexlet/python-project-lvl2/tests/fixtures/step3/lvl2_original.json ~/all/PythonProjects/Hexlet/python-project-lvl2/tests/fixtures/step3/lvl2_modified.json

runtests:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml tests
