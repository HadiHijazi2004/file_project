.PHONY: help run test clean install combine concat wordcount static classmethod decorator readlines alldemo

help:
	@echo ""
	@echo "Usage:"
	@echo "  make run         - Run file_handler.py"
	@echo "  make test        - Run all pytest tests"
	@echo "  make clean       - Delete generated .txt files"
	@echo "  make install     - Install from requirements.txt"
	@echo "  make readlines   - Read lines using FileHandler"
	@echo "  make wordcount   - Count words in file"
	@echo "  make combine     - Combine two files using + operator"
	@echo "  make classmethod - Demonstrate @classmethod"
	@echo "  make static      - Demonstrate @staticmethod"
	@echo "  make decorator   - Demonstrate custom decorator"
	@echo "  make concat      - Concatenate multiple files"
	@echo "  make alldemo     - Run all demo files"

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

readlines:
	python demo_read_lines.py

alldemo:
	python demo_combine.py
	python demo_concat.py
	python demo_wordcount.py
	python demo_static.py
	python demo_classmethod.py
	python demo_decorator.py
	python demo_read_lines.py

clean:
	rm -f *.txt

install:
	pip install -r requirements.txt
