import json
from pathlib import Path

# File path
OUTPUT_FILE = "data/subjects.json"


def add_subject(subject):
    try:
        with open (OUTPUT_FILE, "r") as file:
            content = json.load(file)
    except (json.decoder.JSONDecodeError, FileNotFoundError): 
        content= []
    
    if content:
        if subject in content:
            return True

        content.append(subject)
        with open(OUTPUT_FILE, "w") as file:
            json.dump(content, file, indent=4)
    else: 
        subjects = []
        subjects.append(subject)
        with open(OUTPUT_FILE, "w") as file:
            json.dump(subjects, file, indent=4)