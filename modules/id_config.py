import json 
from pathlib import Path

TARGET = "../data/student.json"



def check_id(student_id, student_pass):
    try:
        with open(TARGET, "r") as file:
            content = json.load(file)
    except (json.decoder.JSONDecodeError, FileNotFoundError):
        content = []

        with open (TARGET, "w") as file:
            json.dump(content, file)

        return False, "No users exist! Create one"