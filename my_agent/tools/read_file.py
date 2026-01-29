from pathlib import Path


def read_file(path: str):
    """
    Read contents of the file
    """
    file = Path(path)
    try:
        content = file.read_text()
        return {
            "message": "Successful",
            "content": content
        }
    except Exception as e:
        return {
            "message": f"Not Successful. Error: {e}"
        } 
    

if __name__ == '__main__':
    read_file()

