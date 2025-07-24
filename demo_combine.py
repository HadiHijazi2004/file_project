from file_handler import FileHandler

f1 = FileHandler("sample1.txt")
f2 = FileHandler("sample2.txt")


combined = f1 + f2


print(f"\n Files combined into: {combined.filename}\n")
with open(combined.filename, "r") as f:
    print(" Combined file content:")
    print(f.read())
