from file_handler import deco  

@deco("green")
def greet():
    print("Hello from decorated function!")

@deco("red")
def warn():
    print("Warning: This is red!")

@deco("blue")
def info():
    print("Information in blue.")

# Run them
greet()
warn()
info()
