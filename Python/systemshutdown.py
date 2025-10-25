import os# operating system

def shutdown():
    choice = input("Do you want to shutdown your computer? (yes/no): ").strip().lower()
    if choice == "yes":
        # For Windows
        os.system("shutdown /s /t 1")
        # For Linux/Mac, use:
        # os.system("sudo shutdown now")
    else:
        print("Shutdown cancelled.")

# Call the function
shutdown()
