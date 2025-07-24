import pytest
from file_handler import FileHandler, AdvancedFileHandler, deco
from io import StringIO
import sys


@pytest.fixture
def sample_file(tmp_path):
    test_file = tmp_path / "testfile.txt"
    test_file.write_text("Hello World\nPython is fun")
    return str(test_file)

@pytest.fixture
def advanced_file(sample_file):
    return AdvancedFileHandler(sample_file)

def test_read_lines(sample_file):
    fh = FileHandler(sample_file)
    lines = list(fh.read_lines())
    assert lines == ["Hello World", "Python is fun"]

def test_word_count(advanced_file):
    assert advanced_file.count_words() == 5

def test_file_combination(tmp_path):
    file1 = tmp_path / "f1.txt"
    file2 = tmp_path / "f2.txt"
    file1.write_text("Hello\nWorld")
    file2.write_text("Python\nRocks")

    fh1 = FileHandler(str(file1))
    fh2 = FileHandler(str(file2))
    combined = fh1 + fh2

    with open(combined.filename) as f:
        lines = [line.strip() for line in f.readlines()]

    assert lines == ["Hello", "World", "Python", "Rocks"]

def test_concat_files(tmp_path):
    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.txt"
    file1.write_text("One\nTwo")
    file2.write_text("Three\nFour")

    af = AdvancedFileHandler(str(file1))
    fh2 = FileHandler(str(file2))

    combined = af.concat_files(fh2)
    with open(combined.filename, "r") as f:
        lines = [line.strip() for line in f.readlines()]
    assert lines == ["One", "Two", "Three", "Four"]


def test_decorator_output(capsys):
    @deco("red")
    def say_hello():
        print("Hello")

    say_hello()
    captured = capsys.readouterr()
    assert "Hello" in captured.out

def test_static_method():
    assert AdvancedFileHandler.is_text_file("example.txt") is True
    assert AdvancedFileHandler.is_text_file("data.csv") is False

def test_class_method(tmp_path):
    file_path = tmp_path / "newfile.txt"
    handler = AdvancedFileHandler.from_content(str(file_path), "This is a test file.")
    assert isinstance(handler, AdvancedFileHandler)
    with open(file_path, "r") as f:
        assert f.read() == "This is a test file."
