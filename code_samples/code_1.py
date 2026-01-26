def greeting(name: str) -> None:
    """
    Displays a greeting message to the terminal.

    Args:
        name (str): The name of the person or group to greet.
    """
    if not name:
        print("Hello World")
        return

    print(f"Hello {name}")


if __name__ == "__main__":
    greeting(name="Gdg Members")