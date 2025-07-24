from file_handler import AdvancedFileHandler

# Use from_content to create file and return handler
af = AdvancedFileHandler.from_content("new_created.txt", "Hello from @classmethod!")

# Show result
print(f"✅ Created file: {af.filename}")
print(f"📄 File content:")

with open(af.filename, "r") as f:
    print(f.read())
