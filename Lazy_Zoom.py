import shutil
import webbrowser
import time
import os

l = []
a = []
attempts = 3
payment = ""

print("***************************     LAZY CLASSES     ***************************")
print("**********************     DEVELOPED BY HAMZA UMER    **********************")

cont = str(input("THIS PROGRAM IS PASSWORD PROTECTED: "
                 "DAMAGE. CONTINUE? (Y/n)"))

if cont != "Y" or cont != "y":
    if cont != "N" or cont != "n":
        print("INCORRECT ENTRY!!!")
    print("EXITING PROGRAM!!!")
    os.system("pause")
    exit()

while payment != "PASSWORD":
    payment = input("ENTER PASSWORD PROVIDED TO YOU TO UNLOCK THE FILE: ")

    if payment != "PASSWORD":
        attempts = attempts - 1
        attempts_show = str(attempts)
        print("INCORRECT PASSWORD... RETRY... ATTEMPTS REMAIN:  " + attempts_show)
        if attempts == 0:
            print("INCORRECT PASSWORD..... Unauthorised access..... Deleting Program from Your Computer")
            path = os.getcwd()
            print("DELETING FILES FROM: " + path)
            print("RESTARTING DEVICE IN 10 SECONDS!!!")
            os.system("shutdown /s /t 10")
            print("DELETING THE PROGRAM!!!")
            time.sleep(5)
            os.remove("Lazy_Zoom.exe")
            os.system("pause")
            exit()






else:
    print("AUTHORIZED!!!")
    classes = int(input("How Many Classes do you have today?"))
    done = 0
    joined = 0
    link_arr = []
    time_arr = []

    while done < classes:
        link = input("Enter Zoom Link Number in ORDER of TIME TABLE: ")
        link_arr.append(link)
        time_of_join = input("Enter Time (Format:- HH:MM:SS)(24 hour format) ->")
        time_arr.append(time_of_join)
        done = done + 1

    Current_time = time.strftime("%H:%M:%S")

    while joined < classes:
        while Current_time != time_arr[joined]:
            print("Current Time is: " + Current_time + "\t\tNext Class is at: " + time_arr[joined] + "\t\tLink is: " +
                  link_arr[joined])
            Current_time = time.strftime("%H:%M:%S")
            time.sleep(1)

        if Current_time == time_arr[joined]:
            print("JOINING CLASS :D")
            webbrowser.open(link_arr[joined])
            joined = joined + 1
