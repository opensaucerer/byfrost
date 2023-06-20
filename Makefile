
testall:
	pip install -r requirements.txt && python3 -m unittest discover

testunit:
	pip install -r requirements.txt && python3 -m unittest discover

testnose:
	pip install -r requirements.txt && python3 -m nose2

wheel:
	rm -rf build dist && ./setup.py sdist bdist_wheel

install:
	pip uninstall byfrost -y && pip install dist/byfrost-0.0.0.0-py2.py3-none-any.whl --force-reinstall

testpypi:
	python3 -m twine upload --repository testpypi dist/*