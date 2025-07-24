import pytest 
from file_handler import FileHandler, AdvancedFileHandler

#fixture to create a sample file with text
@pytest.fixture
def sample_file(tmp_path):
    test_file = tmp_path / "testfile.txt"
    test_file.write_text("Hello World\nPython is fun")
    return str(test_file)

#fixture for AdvancedFileHandler
@pytest.fixture
def advanced_file(sample_file):
    return AdvancedFileHandler(sample_file)

#test 1: check line reading
def test_read_lines(sample_file):
    fh = FileHandler(sample_file)
    lines = list(fh.read_lines())
    assert lines == ["Hello World", "Python is fun"]

# test 2: check word count
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
