"""
File operations to create or delete folders
"""

from pathlib import Path

def create_path(type: str, path: str, content: str):
    """
    Docstring for create
    
    :param type: The type of object you are creating, file or folder
    :type type: str
    :param path: The path of where you want to create it.
    :type path: str
    :param content: The content to be put in the path
    """
    try:
        if type.lower() == "file":
            with Path(path).open("w", encoding="utf-8") as f:
                f.write(content)
        else:
            folder = Path(path)
            folder.mkdir(parents=True, exist_ok=True)
        return {
            "message": f"{type} creation was successful",
            "Path": str(Path(path))
        }
    except Exception as e:
        return {
            "message": f"{type} creation was not successful",
            "error": e
        }