from file_handler import AdvancedFileHandler


af = AdvancedFileHandler.from_content("new_created.txt", "Hello from @classmethod!")


print(f" Created file: {af.filename}")
print(f" File content:")

with open(af.filename, "r") as f:
    print(f.read())
