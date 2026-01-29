from pathlib import Path
import time

def edit_file(path: str, content: str):
    """
    Edit this file with the content
    """
    try:
        directory = Path(path)
        lines = content.splitlines()
        with directory.open("w", encoding="utf-8") as f:
            for line in lines:
                f.write(line + "\n")
                f.flush()
                time.sleep(0.1)
                
        new_content = directory.read_text()
        return {
            "message": "Successful",
            "new_content": new_content
        }
    except Exception as e:
        return {
            "message": f"Not Successful. Error: {e}"
        }
    

if __name__ == "__main__":
    edit_file("This is the edited content!")
