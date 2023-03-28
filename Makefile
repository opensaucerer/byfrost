
test-all:
	python setup.py pytest

test-unit:
	pip install -r requirements.txt && python -m unittest discover

test-nose:
	pip install -r requirements.txt && python -m nose2

wheel:
	python setup.py bdist_wheel

install:
	pip install dist/bifrost-0.0.1-py3-none-any.whl