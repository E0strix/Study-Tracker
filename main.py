# from modules.add_subject import add_subject

def main():
    print("Hello, welcome to student tracker 9000")
    while True:
        print("\n------------------------")
        print("Choose an option")
        print("------------------------")
        print("\n1- Add subjects (max. 12)")
        op = input("Choose from the options above:")

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
    while True:
        subjects = input("\nEnter no. subjects studying:")

main()