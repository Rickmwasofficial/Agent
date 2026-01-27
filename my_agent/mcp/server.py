from fastmcp import FastMCP
from pathlib import Path
import time

server = FastMCP("Code review and editing")

path = Path("./code_samples/code_1.py")

@server.tool
def read_file(path_2: str):
    """
    Read contents of the file
    """
    content = path.read_text()
    return {
        "message": "Successful",
        "content": content
    }

@server.tool
def edit_file(content: str):
    """
    Edit this file with the content
    """
    lines = content.splitlines()
    with path.open("w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")
            f.flush()
            time.sleep(0.1)

    new_content = path.read_text()

    return {
        "message": "Successful",
        "new_content": new_content
    }


if __name__ == "__main__":
    server.run(transport="stdio")



