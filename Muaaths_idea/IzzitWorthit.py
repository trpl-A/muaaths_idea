"""
started:    23/02/23
updated:    24/02/23
desc:       an app to make a student's life less stressful 
            by informing that person about critical news
creator:    RFX
version:    0.1 (version 'skeleton')
"""


import os 
import time 
from colorama import Fore, Style
# ===============================


# percentages
public_transport = 100
loadshedding = True 
# loadshedding = 100

# lecture_attendence = 100
access_to_blackboard = True
# access_to_blackboard = 100



# lecturer confirmation
def read_file1():
    with open("records/lecturer.txt", "r") as file:
        f = file.readlines()
        result = f[0].strip("\n")
    	
        i = result.index(":")
        # print(i)

        read_file1.final = result[(i+2)::]
        # print(final)

# end of function =====================================
# read_file()


# alternate version for the function above
# def read_file1(dir):
#     with open(dir, "r") as file:
#         f = file.readlines()
#         result = f[0].strip("\n")
    	
#         i = result.index(":")
#         # print(i)

#         read_file1.final = result[(i+2)::]
#         # print(final)

# # end of function =====================================
# d = "records/lecturer.txt"
# # read_file(d)



# blackboard
def read_file2():
    with open("records/blackboard.txt", "r") as file:
        f = file.readlines()
        result = f[0].strip("\n")
    	
        i = result.index(":")
        # print(i)

        read_file2.final = result[(i+2)::]
        # print(read_file2.final)

# end of function =====================================
# read_file2()



# summary
def homepage():
    read_file1()
    read_file2()

    note = """
    The purpose of this application is for students to determine if 
    it is *Worthit* to travel to campus.
    
    We understand that some students live a long 
    distance from the educational institute, and that it 
    can be frustrating to travel for many
    hours, get stuck in traffic, and maybe experience other 
    delays to get to the campus only
    to be met with a slap to face knowing that the class 
    that you tried so hard to attend was
    cancelled. 
    
    Maybe there was a valid reason for the cancelation or maybe not.
    The app aims to provide an idea for students to make 
    a more educated decision by providing the
    student with RELEVANT and TIMELY information 

    IZZITWORTHIT to stress for something that may not even happen?
    """


    title = "Summary"
    line = len(title) * "="
    current_time = time.asctime()

    print(f"\n{Fore.YELLOW + Style.BRIGHT}{note}{Fore.RESET + Style.RESET_ALL}\n")
    input("click here and enter to continue...")
    os.system("cls")

    print(f"\n{title} \t\t\t\t{current_time}")
    print(f"{line}\n")

    print(f"1) public transport reliability: \t{public_transport}%")
    print(f"2) load-shedding: \t\t\t{loadshedding}")
    print(f"3) lecturer attendance: \t\t{read_file1.final}")
    # print(f"3) lecturer attendence: \t\t{lecturer_confirmation.present_to_teach}")
    print(f"4) access to Blackboard: \t\t{read_file2.final}")

    option = input("\nEnter a number to view more details \n> ")
    if option == "1":
        os.system("cls")

    elif option == "2":
        os.system("cls")

    elif option == "3":
        os.system("cls")

    elif option == "4":
        os.system("cls")


    else:
        print("invalid input")

# end of function =====================================
# homepage()


# <<< END >>>