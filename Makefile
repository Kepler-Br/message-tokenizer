all: build

build:
	python -m build

push:
	twine upload --repository nexus dist/*

clean:
	@rm -rf dist src/barkeputils.egg-info
