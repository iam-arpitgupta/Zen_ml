# defininf the dir and the path 
import os 
from pathlib import Path

project_name = "src"

list_of_files = [
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_preprocessing.py",
    f"{project_name}/components/model_training.py",
    f"{project_name}/config/__init__.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/data_ingestion.py",
    f"{project_name}/__init__.py",
    f"{project_name}/constants/__init__.py",
    ".env",
    "app.py",
    "requirements.txt",
    "setup.py",
    "pyproject.toml",
    "testEnvironment.py",
    "config.yaml"
]
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        print(f"file is already present at: {filepath}")