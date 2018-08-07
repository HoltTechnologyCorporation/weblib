build: venv deps develop

venv:
	virtualenv --no-site-packages --python=python3.4 .env
	
deps:
	.env/bin/pip install -r requirements_dev.txt
	#.env/bin/pip install -r requirements_full.txt

develop:
	.env/bin/python setup.py develop

flake:
	flake8 weblib test

flake_verbose:
	flake8 weblib test --show-pep8

test:
	py.test

coverage:
	py.test --cov weblib --cov-report term-missing

clean:
	find -name '*.pyc' -delete
	find -name '*.swp' -delete

doc:
	sh -c 'cd docs; make html'

upload:
	git push --tags; python setup.py sdist upload

.PHONY: all build venv flake test vtest testloop cov clean doc
