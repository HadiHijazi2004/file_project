.PHONY: help run test clean venv install

help:
	 ""
	"Usage:"
    "  make run        - Run file_handler.py"
	"  make test       - Run all pytest tests"
    "  make clean      - Delete generated .txt files"
    "  make install    - Install from requirements.txt"
	"  make wordcount  - count words"
	"  make combine    - combines files"
	"  make classmethod - classmethod"
	"  make staticmethod - static method"
	"  make decorator - decorator"
	"  make concat - concat"
	"  make alldemo- runs all demos"

run:
	python file_handler.py

test:
	pytest

combine:
	python demo_combine.py

concat:
	python demo_concat.py

wordcount:
	python demo_wordcount.py

static:
	python demo_static.py

classmethod:
	python demo_classmethod.py

decorator:
	python demo_decorator.py

alldemo:
	python demo_combine.py
	python demo_concat.py
	python demo_wordcount.py
	python demo_staticmethod.py
	python demo_classmethod.py
	python demo_decorator.py

clean:
	del /q *.txt 2>nul || echo "No .txt files to delete"

install:
	pip install -r requirements.txt
