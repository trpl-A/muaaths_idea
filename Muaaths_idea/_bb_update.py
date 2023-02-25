
from colorama import Fore, Style


# blackboard online
def blackboard_confirmation():
    present_to_teach = True

    confirmed = False 

    while not confirmed:
        bb = input("\nIs Blackboard accessable and online? (y/n) ").lower()
        if bb == "n":
            present_to_teach = False 
            confirmed = True 

            reason = input("Enter a reason for for the website being offline\n")

            with open("records/blackboard.txt", "w") as file:
                file.write(f"Blackboard accessable: {present_to_teach}")
                file.write(f"\nReason: {reason}")


        elif bb == "y":
            confirmed = True 

            # print(f"\nIs Blackboard accessable: {present_to_teach}")
            
            with open("records/blackboard.txt", "w") as file:
                file.write(f"Blackboard accessable: {present_to_teach}")

        else:
            print(f"{Fore.RED + Style.BRIGHT}Invalid response{Fore.RESET + Style.RESET_ALL}")

# end of function =====================================
blackboard_confirmation()
