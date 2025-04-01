# import os                      #Provides functions to interact with the operating system (e.g., creating files, directories).
# from pathlib import Path      #A more modern way to handle file system paths.
# import logging         # Used to display messages (logs) about what the script is doing.

# logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

# Sets the logging level to INFO, meaning messages at this level or higher (e.g., warnings, errors) will be displayed.
#format='[%(asctime)s]: %(message)s:': Specifies how log messages should appear.

# %(asctime)s → Adds a timestamp.

# %(message)s → Displays the log message.




# project_name="text_summary"

# list_files=[
#     ".github/workflows/.gitkeep",
#     f"src/{project_name}/__init__.py",
#     f"src/{project_name}/components/__init__.py",
#     f"src/{project_name}/utils/__init__.py",
#     f"src/{project_name}/utils/common.py",
#     f"src/{project_name}/logging/__init__.py",
#     f"src/{project_name}/config/configuration.py",
#     f"src/{project_name}/pipeline/__init__.py",
#     f"src/{project_name}/entity/__init__.py",
#     f"src/{project_name}/constants/__init__.py",
#     "config/config.yaml",
#     "params.yaml",
#     "app.py",
#     "main.py",
#     "Dockerfile",
#     "requirements.txt",
#     "setup.py",
#     "research/trials.ipynb"
# ]

# for file in list_files:
#     filepath=Path(file)
#     filedir,filename=os.path.split(filepath)

#     if filedir!= "":
#         os.makedirs(filepath, exist_ok=True)
#         logging.info(f"Created directory: {filedir} for the file: {filename}")

#     if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
#         with open(filepath, "w") as f:
#             pass    
#             logging.info(f"Created empty file: {filepath}")
    
#     else :
#         logging.info(f"File already exists: {filepath}")


import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = "text_summary"

list_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "test.py"
]

for file in list_files:
    filepath = Path(file)
    dir_path = filepath.parent  # Get directory path

    # Ensure the directory exists
    if not dir_path.exists():
        os.makedirs(dir_path, exist_ok=True)
        logging.info(f"Created directory: {dir_path}")

    # Ensure the file is created and is not a directory
    if filepath.exists() and filepath.is_dir():
        logging.warning(f"Removing incorrect directory: {filepath}")
        os.rmdir(filepath)  # Remove it since it's wrongly a directory

    # Create the file if it does not exist
    if not filepath.exists():
        with open(filepath, "w"):
            pass
        logging.info(f"Created empty file: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")
