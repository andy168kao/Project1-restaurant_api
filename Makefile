install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
		pip install pylint

format:
	black *.py

lint:
	pylint --disable=C,R app.py

test:
	python -m pytest -vv --cov=hello test_hello.py

all: install lint test
