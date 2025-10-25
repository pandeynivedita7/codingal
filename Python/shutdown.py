import os#operating system

def shutdown():
    print("Shutting down the system...")
    os.system("shutdown /s /t 1")   # For Windows
    # os.system("sudo shutdown now") # For Linux or macOS

# Call the function
shutdown()
