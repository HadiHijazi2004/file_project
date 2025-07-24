from file_handler import AdvancedFileHandler


files = ["report.pdf", "notes.txt", "script.py", "data.txt"]

for name in files:
    result = AdvancedFileHandler.is_text_file(name)
    print(f"{name:12} ➜ {' is a text file' if result else ' not a text file'}")
