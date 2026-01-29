"""
File operations to create or delete folders
"""

from pathlib import Path

def delete_path(type: str, path: str):
    """
    Docstring for delete
    
    :param type: The type of object you are deleting, file or folder
    :type type: str
    :param path: The path of where you want to delete it.
    :type path: str
    """
    try:
        if type.lower() == "file":
            Path(path).unlink(missing_ok=True)
        else:
            folder = Path(path)
            if not folder.exists():
                return
            is_empty = not any(folder.iterdir())
            if is_empty:
                folder.rmdir()
            else:
                for item in folder.iterdir():
                    if item.is_file():
                        item.unlink()
                    elif item.is_dir():
                        delete_path("dir", str(item))
                folder.rmdir()
    except Exception as e:
        return {
            "message": f"{type} deletion was not successful",
            "error": e
        }