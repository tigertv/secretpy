.PHONY: all package package2 package3 install install2 install3 uninstall uninstall2 uninstall3 test test2 test3 upload clean

all: package

package: package2 package3

package2: setup.py
	python setup.py sdist bdist_wheel
package3: setup.py
	python3 setup.py sdist bdist_wheel

install: install2 install3

install2: setup.py
	python setup.py install --user
install3: setup.py
	python3 setup.py install --user

uninstall: 
	make -i uninstall2	
	make -i uninstall3	

uninstall2: 
	pip uninstall secretpy
uninstall3: 
	pip3 uninstall secretpy

test: test2 test3

test2: setup.py
	python setup.py test
test3: setup.py
	python3 setup.py test

upload: 
	python -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
clean:
	rm -rf dist build secretpy.egg-info secretpy/*.pyc secretpy/__pycache__ tests/*.pyc test/__pycache__
	
