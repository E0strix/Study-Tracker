# from modules.add_subject import add_subject

def main():
    print("Hello, welcome to student tracker 9000")
    while True:
        print("\n------------------------")
        print("Choose an option")
        print("------------------------")
        print("\n1- Add subjects (max. 12)")
        op = input("Choose from the options above: ")

        if op == "1":
            subject_entry()
            break 
        elif op == "2":
            break
        elif op == "3":
            break
        else:
            print("Incorrect! Please enter correct option!")


def subject_entry():
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

    for x in range (1, subject_count + 1):
            subject = input(f"\nEnter the subject {x}: ")
        
        




main()