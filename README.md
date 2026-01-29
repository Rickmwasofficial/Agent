# Code Reviewer Agent

This project is a Python-based agent that acts as a Senior Software Engineer and Code Quality Specialist. It analyzes source code, identifies areas for improvement, and performs edits to enhance performance, readability, security, and maintainability.

## Description

The agent leverages the `google-adk` library to create a Gemini-powered agent. The agent is configured to understand and refactor code based on a set of predefined instructions. It can read files, list directories, and edit files within the project.

The core of the agent is defined in `my_agent/agent.py`. It uses the `gemini-3-pro-preview` model and is configured with a specific persona and instructions to review and refactor code.

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/your-username/your-repository.git
    ```
2.  Navigate to the project directory:
    ```bash
    cd your-repository
    ```
3.  Create a virtual environment:
    ```bash
    python -m venv .venv
    ```
4.  Activate the virtual environment:
    -   On Windows:
        ```bash
        .venv\Scripts\activate
        ```
    -   On macOS and Linux:
        ```bash
        source .venv/bin/activate
        ```
5.  Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

The agent can be used to review and refactor code. The main entry point for the agent is `my_agent/agent.py`.

To use the agent, you would typically run it with the ADK runtime, providing it with files or directories to process.

## Project Structure

```
.
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── code_samples
│   └── code_1.py
└── my_agent
    ├── __init__.py
    ├── agent.py
    ├── .adk
    │   └── session.db
    └── tools
        ├── create_ops.py
        ├── delete_ops.py
        ├── edit_file.py
        ├── list_dirs.py
        └── read_file.py
```

### Key Files

-   `my_agent/agent.py`: The main agent definition, including the model, persona, and instructions.
-   `my_agent/tools/`: A directory containing the tools available to the agent.
    -   `create_ops.py`: Functions for creating files and directories.
    -   `delete_ops.py`: Functions for deleting files and directories.
    -   `edit_file.py`: A function for editing files.
    -   `list_dirs.py`: A function for listing the contents of a directory.
    -   `read_file.py`: A function for reading the contents of a file.
-   `requirements.txt`: A list of the Python dependencies for this project.

## Tools

The agent is equipped with the following tools:

-   **`create_path(type: str, path: str, content: str)`**: Creates a file or a folder at a specified path.
-   **`delete_path(type: str, path: str)`**: Deletes a file or a folder at a specified path.
-   **`edit_file(path: str, content: str)`**: Edits the content of a file at a specified path.
-   **`list_dirs(path: str = '')`**: Lists the contents of a directory. If no path is provided, it lists the contents of the project root.
-   **`read_file(path: str)`**: Reads the content of a file at a specified path.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
