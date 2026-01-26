from pathlib import Path

path = Path("./code_samples/code_1.py")

def edit_file(content: str):
    """
    Edit this file with the content
    """
    new_content = path.write_text(content)
    return {
        "message": "Successful",
        "new_content": new_content
    }
    

if __name__ == "__main__":
    edit_file("This is the edited content!")