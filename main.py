from pathlib import Path
import os

def readfileandfolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i, items in enumerate(items):
        print(f"{i+1} : {items}")

def updatefile():

    try:
        readfileandfolder()

        name=input("tell which file to update?")
        p=Path(name)
        if p.exists() and p.is_file():
            print("press 1 for changing the name of your file")
            print("press 2 for overwritting your data in file")
            print("press 3 for appending some new data to your file")

            res=int(input("Enter your response:"))

            if res == 1:
                name2=input("Tell the new name of this file")
                p2=Path(name2)
                p.rename=p2

            if res == 2:
                with open(p,'w') as fs:
                    data=input("Tell what you want to write to overwrite:")
                    fs.write(data)

            if res == 3:
                with open(p,'a') as fs:
                    data=input("Write the data to append to this file")
                    fs.write(" "+data)
    except Exception as err:
        print(f"some error occured as {err}")

def readfile():
    try:
        readfileandfolder()
        name = input("Which file you wanna read?")
        p=Path(name)
        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                data = fs.read()
                print(data)
            print("FILE READ SUCCESSFULLY!")
        else:
            print("FILE DOESNT EXIST")
    except Exception as err:
        print(f"An error occured as {err}")

def createfile():
    try:
        readfileandfolder()
        name=input("Please tell your file name:")
        p = Path(name)
        if not p.exists() and p.is_file():
            with open(p,'w') as fs:
                data = input("What you want to write in this file:")
                fs.write(data)
            print("File created successfully!")
        else:
            print("File already exists!")
    except Exception as err:
        print(f"An error occured as {err}")

def deletefile():
    try:
        readfileandfolder()
        name = input("Which file you wanna delete?")
        p=Path(name)
        if p.exists() and p.is_file():
            os.remove(p)

            print("File removed successfully!")
        else:
            print("No such file exists!")
    except Exception as err:
        print(f"An error occured as {err}")

print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for updating a file")
print("Press 4 for deleting a file")

check = int(input("please enter your response:"))

if check ==1:
    createfile()
if check == 2:
    readfile()
if check == 3:
    updatefile()
if check == 4:
    deletefile()