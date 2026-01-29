"""
View all the folders and files in a given directory/folder
"""

from pathlib import Path
from typing import List, Dict

def find_project_root(
    start: Path | None = None,
    markers: tuple[str, ...] = (".git", ".gitignore", "pyproject.toml", "requirements.txt", "package-lockc.json")
) -> Path:
    """
    Walks upwards from `start` until a project root marker is found.
    """
    current = start or Path(__file__).resolve().parent

    for parent in (current, *current.parents):
        if any((parent / marker).exists() for marker in markers):
            return parent

    raise RuntimeError("Project root not found")


def list_dirs(path: str = '') -> Dict[str, List[Path]]:
    """
    Returns the root directory/folder and all the subfolders and files within it.
    Do Not Add a path argument if you want to find all existing files within the project
    Add a path argument when you want to find all the contents of a folder which is not the root.
    """
    path = find_project_root() if not path else Path(path)
    paths: List[Path] = []

    for item in path.iterdir():
        paths.append(item)
        if item.is_dir() and item.name not in [".venv", ".venv2", "venv", ".adk", "__pycache__"]:
            paths.extend(list_dirs(str(item))["paths"])

    return {
        "root": str(path),
        "paths": [str(rl) for rl in paths]
    }
    
if __name__ == "__main__":
    print(list_dirs())
