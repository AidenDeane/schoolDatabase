from Classes import *
from Database import *
import time
import os

# Name: Aiden Deane
# Title: OOC Database - main.py
# Date: Final Commit 15 Oct 2024
# Description: Imports class and database files, puts them to use in a database-esque menner. 


def wait(sec): #too lazy 
    return time.sleep(sec)


def clear():
     return os.system("clear")

def listPeople():
    global usrInput
    for i in Person.personnelManifest:
                print("]",i.name)

def listItem():
    global usrInput
    for i in Item.itemManifest:
                print("]",i.item)
end = False


while end == False:
    clear()
    print("Welcome to the school database.")
    wait(1)
    usrInput = int(input("[1] Get Personal data\n[2] Checking-out items\n[3] Get item data\n[4] Get remarks\n[5] Save remarks\n[6] Quit\n> "))
    if usrInput == 1:
        clear()
        #print(Person.personnelManifest.name)
        listPeople()
        while usrInput <= len(Person.personnelManifest):
            usrInput = int(input("\n> "))-1
            clear()
            if usrInput < len(Person.personnelManifest) and usrInput >-1:
                personFinder = Person.personnelManifest[usrInput]
                personFinder.printInfo()
                wait(5)
                break
            elif usrInput >= len(Person.personnelManifest) or usrInput <0:
                print("Error: Cannot access obj at index!")
                wait(2)
                break
    elif usrInput == 2:
        clear()
        usrInput = 0
        listItem()
        while usrInput <= len(Item.itemManifest):
            usrInput = int(input("\n> "))-1
            if usrInput < len(Item.itemManifest) and usrInput >-1:
                objectFinder = Item.itemManifest[usrInput]
                clear()
                listPeople()
                break
            elif usrInput >= len(Item.itemManifest) or usrInput <0:
                print("Error: Cannot access obj at index!")
                wait(2)
                usrInput = 999 ## Absolutely will not reset without this. Hopefully nobody decides to create 999 objects else Y2K happens
                break
        while usrInput <= len(Person.personnelManifest):
            usrInput = int(input("\n> "))-1
            if usrInput < len(Person.personnelManifest) and usrInput >-1:
                personFinder = Person.personnelManifest[usrInput]
            elif usrInput >= len(Person.personnelManifest) or usrInput <0:
                print("Error: Cannot access obj at index!")
                wait(2)
                break
            clear()
            amount = int(input("How many would you like to check-out? \n> ")) ## Separates the if statements
            if amount > objectFinder.count or amount <0:
                 print("Error: Cannot check out this many items!")
                 wait(2)
            else:
                objectFinder.checkout(amount,personFinder)
                print("Item successfully checked out!")
                wait(2)
            break
    
    elif usrInput == 3:
        clear()
        usrInput = 0
        for i in Person.personnelManifest:
            print("]",i.name,i.materials) # prints name and materials for each person
        for i in Item.itemManifest:
            print("]",i.item, i.query()) # lists total and available
        wait(5)
              
    elif usrInput == 4:
        clear()
        usrInput = 0
        listPeople()
        while usrInput != len(Person.personnelManifest):
            usrInput = int(input("\n> "))-1
            if usrInput < len(Person.personnelManifest) and usrInput >-1:
                personFinder = Person.personnelManifest[usrInput]
                personFinder.getInfo()
                wait(5)
                break
            elif usrInput >= len(Person.personnelManifest) or usrInput <0:
                print("Error: Cannot access obj at index!")
                wait(2)
                break
                
        
    elif usrInput == 5:
        clear()
        usrInput = 0
        listPeople()
        while usrInput != len(Person.personnelManifest):
            usrInput = int(input("\n> "))-1
            personFinder = Person.personnelManifest[usrInput]
            personFinder.saveInfo()
            break

    elif usrInput ==6:
         end = True
    else:
        clear()
        print("Error: Response not recognized!")
        wait(2)