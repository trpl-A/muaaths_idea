
from colorama import Fore, Style 



# for collecting details of all appropriate lecturers
def collect_details():
    # dict for details
    lecturer_details = {}

    d0 = input("enter your work email address: ").capitalize()
    d1 = input("enter your first name: ").capitalize()
    d2 = input("enter your first surname: ").capitalize()
    d3 = input("enter your initials: ").upper()
    d4 = input("enter the subject that you teach: ")
    # d4 = input("enter the subjects that you teach: ")

    d5 = input("enter the subject code for the subject that you teach: ")
    # d5 = input("enter the subject codes for the subject that you teach \n> ")


    lecturer_details["email"] = d0 
    lecturer_details["initials"] = d3

    lecturer_details["name"] = d1
    lecturer_details["surname"] = d2
    lecturer_details["subject(s)"] = d4
    lecturer_details["subject_code(s)"] = d5

    # collect_details.list_of_details = []
    # l = collect_details.list_of_details

    file = open("records/details_of_each_lecturer.txt", "a")


    for d in lecturer_details:
        # print(d, lecturer_details[d])
        # l.append(lecturer_details[d])
        file.write(f"{d}: {lecturer_details[d]}\n")

    file.write(f"\n")

# end of function =====================================
collect_details()




# lecturer confirmation, from one lecturer
def lecturer_confirmation():
    lecturer_confirmation.present_to_teach = True

    confirmed = False

    while not confirmed:
        lecture_attendance = input("\nWill you be present for your lecture? (y/n) ").lower()
        if lecture_attendance == "n":
            lecturer_confirmation.present_to_teach = False
            
            confirm = input("Are you sure? (y/n) ").lower()
            if confirm == "y":
                confirmed = True 
                reason = input("enter reason for absence\n")

                # print(f"\n> Lecturer attendance \n{lecturer_confirmation.present_to_teach}")
                # print(f"\n> Reason \n{reason}")

                with open("records/lecturer.txt", "w") as file:
                    file.write(f"Lecturer attendance: {lecturer_confirmation.present_to_teach}")
                    file.write(f"\nReason: {reason}")
                

        elif lecture_attendance == "y":
            confirm = input("Are you sure? (y/n) ").lower()
            if confirm == "y":
                confirmed = True 
                # print(f"\nLecturer attendance: {lecturer_confirmation.present_to_teach}")
                
                with open("records/lecturer.txt", "w") as file:
                    file.write(f"Lecturer attendance: {lecturer_confirmation.present_to_teach}")
        

        else:
            print(f"{Fore.RED + Style.BRIGHT}invalid response{Fore.RESET + Style.RESET_ALL}")

# end of function =====================================
# lecturer_confirmation()
