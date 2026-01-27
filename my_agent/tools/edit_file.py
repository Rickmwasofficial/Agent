from pathlib import Path
import time

path = Path("./code_samples/code_1.py")

def edit_file(content: str):
    """
    Edit this file with the content
    """
    lines = content.splitlines()
    with path.open("w", encoding="utf-8') as f:
        for line in lines:
            f.write(line + "\n")
            f.flush()
            time.sleep(0.1
                      )
    return {
        "message": "Successful",
        "new_content": new_content
    }
    

if __name__ == "__main__":
    edit_file("This is the edited content!")
