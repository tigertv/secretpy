
all: install
	
install: setup.py
	python setup.py install --user
uninstall: 
	pip uninstall secretpy
test: setup.py
	python setup.py test
clean:
	rm -rf dist build secretpy.egg-info
	
