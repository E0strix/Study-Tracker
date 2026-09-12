import json 
from pathlib import Path

PATH = "../data/student.json"



def check_id():
    try:
        with open(PATH, "r") as file:
            content = json.load(file)
    except (json.decoder.JSONDecodeError, FileNotFoundError):

        content = {}

        with open (PATH, "w") as file:
            json.dump(content, file, indent=4)

        return False    
