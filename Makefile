
all: package

package: setup.py
	python setup.py sdist bdist_wheel
install: setup.py
	python setup.py install --user
uninstall: 
	pip uninstall secretpy
test: setup.py
	python setup.py test
upload: 
	python -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
clean:
	rm -rf dist build secretpy.egg-info
	
