from modules import data_entry

STUDENT_ID = 0000

def welcome(): # prompt user to login/sign up
    print("Hello, welcome to student tracker 9000")
    while True:
        print("\n1- Login")
        print("2- Sign up")
        print("Enter q to exit")
        op = input("Choose from the options above: ")

        if op.strip().lower() == "q":
            return
        elif op == "1":
            login()
            break 
        elif op == "2":
            sign_up()
            break
        else:
            print("Incorrect! Please enter correct option!")
            


def login():
    pass



def sign_up():
    pass



def menu(): # main menu
    while True:
        print("\n------------------------")
        print("Main menu")
        print("------------------------")
        print("1- Subjects configurations")
        print("Enter q to exit")
        op = input("Choose from the options above: ")

        if op.strip().lower() == "q":
            return
        elif op.strip().lower() == "1":
            add_subject()
            break
        else:
            print("Incorrect! Please enter correct option!")



def subject_configuration():
    pass



def add_subject():
    while True:  # No. of subjects checker
        try:
            subject_count = int(input("\nEnter no. subjects studying: "))

            if subject_count > 12:
                print("No. of subjects should be 12 or less")
            elif subject_count < 1:
                print("You must enter at least 1 subject")
            else:
                break
        except ValueError:
            print("Incorrect! Please enter a number")   

    count = 0
    while True: # prompt to enter subject
        if count < subject_count: 
            subject = input(f"\nEnter the subject {count + 1}. (Enter q to exit): ")

            if subject.strip().lower() == "q":
                break

            result = data_entry.add_subject(subject)

            if result:
                print("Duplicate detected! Try again")
            else:
                count += 1
        else: 
            break
    


def remove_subject():
    pass





if __name__ == "__main__":  
    welcome()