from file_handler import AdvancedFileHandler


af = AdvancedFileHandler("sample1.txt")


print(f" File: {af.filename}")
print(f" Word Count: {af.count_words()}")
