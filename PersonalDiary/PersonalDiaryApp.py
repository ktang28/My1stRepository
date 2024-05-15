import os
from datetime import datetime

with open("myDiary.txt") as my_file:
    entries = my_file.read()
while True:

    print("1 - add an entry, 2 - read previous entries, 0 - quit:")
    operation = input("Please enter your selection:")
    if operation == "1":
        dt = datetime.now()
        content = input("Please type diary entry: ")
        with open("myDiary.txt","a") as diary:
            diary.write(str(dt) +"\n")
            diary.write(f"{content}"+"\n")

        print("Diary saved\n")
    elif operation == "2":
        print("Entries: ")
        with open("myDiary.txt") as diary:
            for row in diary:
                print(row)
    elif operation == "0":
        print('Bye now!'+"\n")
        break

p = open("myDiary.txt", "r")
lines = p.read()
p.close()

try:
    print(lines)
except FileNotFoundError:
    print("Error: The diary file does not exist.")
except PermissionError:
    print("Error: Permission denied when reading the diary file.")

