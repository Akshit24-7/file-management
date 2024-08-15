# file management project

import os

#creat file
def createFile(filename):
    try:
        with open ("pra.txt" , "x") as f :
            print(f"the file {filename} has created successfuly !")
    except FileExistsError :
         print("file allready exit ")

    except Exception as f :
        print("error occurred !")

#view files
def view_all_file():
    files = os.listdir()
    if not files:
        print("no file founded ")
    else:
        print("new file directory !")
        for file in files:
            print(file)

#delete files
def delect_file(filename):
    try:
        os.remove(filename)
    except FileExistsError :
        print(f"file has {filename} delect successfully !")

    except Exception as e :
        print("A error has been founded !")
    
#read file
def read_file(filename):
    try:
        with open ("pra.txt" , "r") as f :
            data = f.read()
        print(f"content of '{filename}' :" , "\n(data)")
    except FileExistsError :
        print(f"{filename} does not exit !!!")
    except Exception as e :
        print(f"error has been occureed")

#edit file
def edit_file(filename):
    try:
        with open ("pra,txt" , "a") as f :
            data = input("enter data to add")
            f.write(data , "\n")
            print(f"content added {filename} successfully")
    except FileExistsError:
        print(f"file doest not exit")
    except Exception as e :
        print(f"an error occurred !!")


def main():
    while True:
        print("FILE MANANGEMENT SYSTEM")
        print("1 :create file") 
        print("2 :view file")
        print("3 :delete file")
        print("4 :read file")
        print("5 :edit file")
        print("6 :Exit")

        choice = input("enter from (1 to 6) =")

        if choice == "1":
            filename = input("enter the file name to create !")
            createFile(filename)
        
        elif choice == "2":
            view_all_file()

        elif choice == "3":
            filename = input("enter the file you want to delect")
            delect_file(filename)

        elif choice == "4":
            filename = input("enter the file you want to read")
            read_file(filename)

        elif choice == "5":
            filename = input("enter the file you want to edit ")
            edit_file(filename)

        elif choice == "6":
            print("closing the app")

            break
        
        else:
            print("invalid syntax")

if __name__ == "__main__":
    main()


