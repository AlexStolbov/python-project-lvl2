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
	poetry run flake8 brain_games

run3:
	poetry run gendiff -f j resource/step3/lvl2_original.json resource/step3/lvl2_modified.json

run3abs:
	poetry run gendiff -f j ~/all/PythonProjects//Hexlet/python-project-lvl2/resource/step3/lvl2_original.json ~/all/PythonProjects//Hexlet/python-project-lvl2/resource/step3/lvl2_modified.json
