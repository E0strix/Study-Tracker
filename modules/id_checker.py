import json 
from pathlib import Path

PATH = "../data/student.json"



def check_id():
    with open(PATH, "r") as file:
        content = json.load(file)

    
