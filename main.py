from modules import data_entry



def main(): #menu
    print("Hello, welcome to student tracker 9000")
    while True:
        print("\n------------------------")
        print("Choose an option")
        print("------------------------")
        print("\n1- Add subjects (max. 12)")
        print("Enter q to exit")
        op = input("Choose from the options above: ")

        if op.strip().lower() == "q":
            return
        elif op == "1":
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

    count = 0
    while True:
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
    







# def subject_entry():
#       

#     for x in range (1, subject_count + 1): # For no. of subjects, entering the subjects
#         subject = input(f"\nEnter the subject {x}(Enter q to exit): ")
        
#         if subject in ["q", "Q"]:
#             break   

#         result = data_entry.add_subject(subject)

#         if result == "Duplicate detected! Try Again":
#             subject_entry()
#             break










if __name__ == "__main__":  
    main()