import json 

TARGET = "data/credentials.json"



def check_id(student_id, student_pass):
    try:
        with open(TARGET, "r") as file:
            content = json.load(file)
    except (json.decoder.JSONDecodeError, FileNotFoundError):
        content = []

        with open (TARGET, "w") as file:
            json.dump(content, file)

        return False, "\nNo users exist! Create one"

    for value in content:
        if value["id"] == student_id and value["password"] == student_pass:
            return True, f"Logging in as {student_id}"

    return False, "\nStudent ID or password is incorrect"



def id_creation():
    pass