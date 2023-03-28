
test-unit:
	pip install requirements.txt && python -m unittest discover

test-nose:
	pip install requirements.txt && python -m nose2