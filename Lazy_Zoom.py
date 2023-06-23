import webbrowser
import time
import os

l = []
a = []
attempts = 3
payment = ""

print("***************************     LAZY CLASSES     ***************************")
print("**********************     DEVELOPED BY HAMZA UMER    **********************")

classes = int(input("How many classes do you have today?"))
done = 0
joiined = 0
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
        print("Current Time is: " + Current_time + "\t\tNext Class is at: " + time_arr[joined] + "\t\tLink is: " + link_arr[joined])
        Current_time = time.strftime("%H:%M:%S")
        time.sleep(1)

    if Current_time == time_arr[joined]:
        print("JOINING CLASS :D")
        webbrowser.open(link_arr[joined])
        joined = joined + 1

