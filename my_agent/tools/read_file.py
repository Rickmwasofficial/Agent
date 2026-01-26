from pathlib import Path

path = Path("./code_samples/code_1.py")

def read_file(path_2: str):
    """
    Read contents of the file
    """
    content = path.read_text()
    return {
        "message": "Successful",
        "content": content
    }
    

if __name__ == '__main__':
    read_file()

