import json
from pathlib import Path

# File path
OUTPUT_FILE = "data/subjects.json"


def add_subject(subject):

    if Path(OUTPUT_FILE).exists():
        with open (OUTPUT_FILE, "r") as file:
            content = json.load(file)
    else:     
        content = []

    if content:
        if subject in content:
            return "Duplicate detected! Try Again"


        content.append(subject)
        with open(OUTPUT_FILE, "w") as file:
            json.dump(content, file, indent=4)
    else: 
        subjects = []
        subjects.append(subject)
        with open(OUTPUT_FILE, "w") as file:
            json.dump(subjects, file, indent=4)