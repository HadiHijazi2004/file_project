from file_handler import FileHandler

# Create FileHandler instances
f1 = FileHandler("sample1.txt")
f2 = FileHandler("sample2.txt")

# Combine using __add__
combined = f1 + f2

# Display result
print(f"\n✅ Files combined into: {combined.filename}\n")
with open(combined.filename, "r") as f:
    print("📄 Combined file content:")
    print(f.read())
