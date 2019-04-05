.PHONY: all package install install2 install3 uninstall uninstall2 uninstall3 test test2 test3 upload clean

all: package

package: 
	python setup.py sdist bdist_wheel --universal

check:
	twine check dist/*

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
	python -m twine upload dist/*

clean:
	rm -rf dist build secretpy.egg-info 
	find . -name "*.pyc" -type f -delete
	find . -name "__pycache__" -type d -delete
