# author: yuce
# created on 2019-05-03, at: 02:17 +0300

.PHONY: all build clean


all: build

build:
	python setup.py sdist

release: clean build
	twine upload dist/*

clean:
	rm -rf dist build openbsd.egg-info/
