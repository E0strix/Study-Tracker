import json

TARGET = "data/credentials.json"
TARGET_2 = "data/telemetry.json"

symbols = ["!", "@", "#", "$", "%", "&"]

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
            return True, f"Logging in as S-{student_id}"

    return False, "\nStudent ID or password is incorrect"



def id_creation(student_pass):
    if len(student_pass) < 8 or len(student_pass) > 12:
        return False, "Your password should be atleast 8 characters and no longer than 12", None

    elif not any(char.isdigit() for char in student_pass):
        return False, "Your password should contain atleast one number", None

    elif not any(char in symbols for char in student_pass):
        return False, "Your password should contain atleast one these symbol (!, @, #, $, %, &)", None


    # Credentials json check
    try:
        with open(TARGET, "r") as file:
            content = json.load(file)
    except (json.decoder.JSONDecodeError, FileNotFoundError):
        content = [] # prep the json file when json doesnt exist

        with open (TARGET, "w") as file:
            json.dump(content, file)


    # Telemetry json check
    try: # if telemetry json exists
        with open(TARGET_2, "r") as file:
            content_2 = json.load(file)

        num = int(content_2["student_no"])
        num += 1

        content_2["student_no"] = str(num).zfill(4)

        with open(TARGET_2, "a") as file: # Updating telemetry json with new no of student
            json.dump(content_2, file)

        content.append({str(num).zfill(4) : student_pass})

        with open(TARGET, "a") as file: # Updating credentials json with new user details
            json.dump(content, file)

        return True, f"Your Student number is {str(num).zfill(4)}", str(num).zfill(4)

    except (json.decoder.JSONDecodeError, FileNotFoundError): #if telemetry json doesnt exist
        content_2 = []
        content_2.append({"student_no" : 1})

        with open(TARGET_2, "w") as file: # Writing to telemetry json
            json.dump(content_2, file)

        num = 1
        content.append({str(num).zfill(4) : student_pass}) # Writing to credentials json

        with open(TARGET, "w") as file:
            json.dump(content, file)

        return True, f"Your Student number is {str(num).zfill(4)}", str(num).zfill(4)












#
# with open(TARGET_2, "w") as file:
#     content_2 = {"student_no" : 1}
#     json.dump(content_2, file)
#
#
#
# with open(TARGET, "a") as file:
#     content = {"id" : student_pass}
#     json.dump(content, file)