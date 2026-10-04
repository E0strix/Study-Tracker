import json

TARGET = "data/credentials.json"
TARGET_2 = "data/telemetry.json"

symbols = ["!", "@", "#", "$", "%", "&"]

def check_id(student_id, student_pass):
    try:
        with open(TARGET, "r") as file:
            content = json.load(file)
    except (json.decoder.JSONDecodeError, FileNotFoundError):
        content = {}
        with open (TARGET, "w") as file:
            json.dump(content, file, indent = 4)
        return False, "\nNo users exist! Create one"

    if student_id in content:
        if content[student_id] == student_pass:
            return True, f"Logging in as S-{student_id}"
        else:
            return False, "\nIncorrect password!"
    else:
        return False, "Incorrect student id!"



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
        content = {} # create json file when json doesnt exist
        with open (TARGET, "w") as file:
            json.dump(content, file, indent = 4)


    # Telemetry json check
    try: # if telemetry json exists
        with open(TARGET_2, "r") as file:
            content_2 = json.load(file)

        num = int(content_2["student_no"]) # count updated
        num += 1
        leading_num = str(num).zfill(4)
        content_2["student_no"] = leading_num

        with open(TARGET_2, "w") as file: # Updating telemetry json with new no of student
            json.dump(content_2, file, indent = 4)

        content[leading_num] = student_pass
        with open(TARGET, "w") as file: # Updating credentials json with new user details
            json.dump(content, file, indent = 4)
        return True, f"Your Student number is {leading_num}", leading_num

    except (json.decoder.JSONDecodeError, FileNotFoundError): #if telemetry json doesnt exist
        content_2 = {}
        content_2["student_no"] = "0001"
        with open(TARGET_2, "w") as file: # Creating the first count, creation of first user
            json.dump(content_2, file, indent = 4)

        content["0001"] = student_pass # Writing to credentials json, creation of first user
        with open(TARGET, "w") as file:
            json.dump(content, file, indent = 4)

        return True, "Your Student number is 0001", "0001"