.PHONY: help run test clean venv install

help:
	@echo ""
	@echo "Usage:"
	@echo "  make run        - Run file_handler.py"
	@echo "  make test       - Run all pytest tests"
	@echo "  make clean      - Delete generated .txt files"
	@echo "  make install    - Install from requirements.txt"
	@echo ""

run:
	python file_handler.py

test:
	pytest

demo:
	python demo_concat.py

combine:
	python demo_combine.py

wordcount:
	python demo_wordcount.py

static:
	python demo_static.py

classmethod:
	python demo_classmethod.py

clean:
	del /q *.txt 2>nul || echo "No .txt files to delete"

install:
	pip install -r requirements.txt
