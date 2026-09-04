from pathlib import Path
import json

# File paths
Code_dir = Path(__file__).resolve().parent()
Output_file = Code_dir.parent / "data" / "subjects.json"


def add_subject():
    with open(Output_file, "w") as file:
        file.write("\n")