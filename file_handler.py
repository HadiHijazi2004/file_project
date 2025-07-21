def deco(color: str):
    color = {
        "blue": "\033[94m",
        "red": "\033[91m",
        "green": "\033[92m]",
        "yellow": "\033[93m",
        "reset": "\033[0m"
    }

    def decorator(func):
        def wrapper(*args, **kwargs):
            print(colors.get(color.lower(), ""), end="")
            result = func(*args, **kwargs)
            print(color["reset"], end="")
            return result
        return wrapper
    return decorator







class FileHandler:
    def __init__(self, filename):
        self._filename = filename


    @property
    def filename(self):
        """Getter for filename"""
        return self._filename
    

    @filename.setter
    def filename(self, value):
        """setter with type check"""
        if not isinstance(value, str):
            raise ValueError("Filename must be a string")
        self._filename = value


    def read_lines(self):
            """generator to read file line by line"""
            with open(self._filename, 'r') as f:
                for line in f:
                    yield line.strip()


    def __str__(self):
         return f"<FileHandler: {self._filename}"


    def __add__(self, other):
        if not isinstance(other, FileHandler):
            raise TypeError("can only add FileHandler object")
     

        new_filename = "combined_file.txt"
        with open(new_filename, 'w') as f_out:
          with open(self._filename, 'r') as f1:
              for line in f1:
                  f_out.write(line if line.endswith('\n') else line + '\n')
          with open(other.filename, 'r') as f2:
             for line in f2:
                 f_out.write(line if line.endswith('\n') else line + '\n')
             
        return FileHandler(new_filename)


class AdvancedFileHandler(FileHandler):
    """child class with extra features"""

    def count_words(self):
        """return total word count in file"""
        with open(self.filename, 'r') as f:
            return sum(len(line.split()) for line in f)
    
    @staticmethod
    def is_text_file(filename):
        """check if the file is a .txt file"""
        return filename.endswith(".txt")
    
    @classmethod
    def from_content(cls, filename, content):
        """create a file from content and return a FileHandler instance"""
        with open(filename, 'w') as f:
            f.write(content)
        return cls(filename)
    
    