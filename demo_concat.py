from file_handler import FileHandler, AdvancedFileHandler

f1 = AdvancedFileHandler("sample1.txt")
f2 = FileHandler("sample2.txt")

combined = f1.concat_files(f2)

print(f"\n Files combined into: {combined.filename}\n")
with open(combined.filename, "r") as f:
    print(" Combined file content:")
    print(f.read())
