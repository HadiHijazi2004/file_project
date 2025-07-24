def deco(color: str):
    colors = {
        "blue": "\033[94m",
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "reset": "\033[0m"
    }

    def decorator(func):
        def wrapper(*args, **kwargs):
            print(colors.get(color.lower(), ""), end="")
            result = func(*args, **kwargs)
            print(colors["reset"], end="")
            return result
        return wrapper
    return decorator

@deco("green")
def greet():
    print("Hello from decorated function!")


@deco("red")
def warn():
    print("Warning: This is red!")

@deco("blue")
def info():
    print("Information in blue.")

greet()
warn()
info()