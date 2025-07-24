from file_handler import AdvancedFileHandler

# Use one of your existing sample files
af = AdvancedFileHandler("sample1.txt")

# Show result
print(f"📄 File: {af.filename}")
print(f"🔢 Word Count: {af.count_words()}")
