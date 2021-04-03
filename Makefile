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
	poetry run flake8 gen_diff
	poetry run flake8 tests

run4:
	poetry run gendiff tests/fixtures/step4/lvl2_original.json tests/fixtures/step4/lvl2_modified.json

run4abs:
	poetry run gendiff ~/all/PythonProjects/Hexlet/python-project-lvl2/tests/fixtures/step4/lvl2_original.json ~/all/PythonProjects/Hexlet/python-project-lvl2/tests/fixtures/step4/lvl2_modified.json

run5:
	poetry run gendiff tests/fixtures/step5/original.yml tests/fixtures/step5/modified.yml

run6json:
	poetry run gendiff tests/fixtures/step6/file1.json tests/fixtures/step6/file2.json

run6yml:
	poetry run gendiff tests/fixtures/step6/file1.yml tests/fixtures/step6/file2.yml

run7stylish:
	poetry run gendiff --format stylish tests/fixtures/step6/file1.json tests/fixtures/step6/file2.json

run7plain:
	poetry run gendiff --format plain tests/fixtures/step6/file1.json tests/fixtures/step6/file2.json

runtests:
	poetry run pytest -v

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml tests
