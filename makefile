.PHONY: help run test clean venv install

help:
	@echo ""
	@echo "Usage:"
	@echo "  make run        - Run main.py"
	@echo "  make test       - Run all pytest tests"
	@echo "  make clean      - Delete generated .txt files"
	@echo "  make install    - Install from requirements.txt"
	@echo ""

run:
	python main.py

test:
	pytest

clean:
	del /q *.txt 2>nul || echo "No .txt files to delete"

install:
	pip install -r requirements.txt
