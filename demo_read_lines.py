from file_handler import FileHandler


with open("demo_sample.txt", "w") as f:
    f.write("Hello World\nPython is fun")


fh = FileHandler("demo_sample.txt")
lines = list(fh.read_lines())

print(" Lines read from the file:")
for line in lines:
    print("-", line)


expected = ["Hello World", "Python is fun"]
print("\n Match expected:", lines == expected)
