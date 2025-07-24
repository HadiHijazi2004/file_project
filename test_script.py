from file_handler import FileHandler, AdvancedFileHandler

fh1 = FileHandler("sample1.txt")
fh2 = FileHandler("sample2.txt")
combined = fh1 + fh2

adv = AdvancedFileHandler(combined.filename)
print(adv)
print("Total words:", adv.count_words())
