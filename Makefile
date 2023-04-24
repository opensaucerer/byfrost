
test-all:
	python setup.py pytest

test-unit:
	pip install -r requirements.txt && python -m unittest discover

test-nose:
	pip install -r requirements.txt && python -m nose2

wheel:
	rm -rf build dist && ./setup.py sdist bdist_wheel

install:
	pip uninstall byfrost -y && pip install dist/byfrost-0.0.0.0-py2.py3-none-any.whl --force-reinstall

testpypi:
	python3 -m twine upload --repository testpypi dist/*