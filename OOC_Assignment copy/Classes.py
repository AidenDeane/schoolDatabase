import datetime
import os 

# Name: Aiden Deane
# Title: OOC Database - Classes.py
# Date: Final Commit 15 Oct 2024
# Description: Teacher and student classes children of Person. Arranger for all classes, exports to main.py. Feature allows you to read and write files! 
# As I write this, I realize that I did not have a safeguard for people with duplicate names. 


class Person:
    personnelManifest = []
    def __init__ (self,name,average,subject,materials,teacher):

        self.name = name
        self.average = average
        self.subject = subject
        self.teacher = teacher
        self.filename = (self.name+(".txt"))
        self.materials = materials
        Person.personnelManifest.append(self)


    def printInfo(self):
        print("Name:", self.name +str("\nAverage: ") +str(self.average) +str("\nSubject:"),self.subject +str("\nChecked-out materials: ")+str(self.materials) +str("\nFile:"),self.filename+str("\nTeacher?"),self.teacher)

    def getMaterials(self):
        print(self.name+str("\'s checked-out items:"),self.materials)

    def saveInfo(self):          # os.getcwd() finds the dir it is currently in so I don't have to make a README.md for "installaton" instructions
        filepath = os.path.join(f"{os.getcwd()}/infoFiles/{self.filename}") # Makes it so it can be dropped anywhere and still function. (I pray that I am right. Did not test this.)
        self.info = input("Enter the information you want to save.\n> ")
        openFile = open(filepath, 'a') # Opens the filepath; appends information to file instead of overwriting like 'w' would. If file does not exist, it will be created automagically
        openFile.write(f"{datetime.date.today()} >>> {self.info}\n") # https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/
        openFile.close()

    def getInfo(self):
        filepath = os.path.join(f"{os.getcwd()}/infoFiles/{self.filename}") # Declaring global would error, had to copypasta this
        openFile = open(filepath,'r') # Opens file at designated filepath as read only
        print(openFile.read()) #Outputs the file's contents
        openFile.close() # closes

class Student(Person):
    def __init__(self,name,average,subject):
        super().__init__(name,average,subject,[],"No") # Adult? No

class Teacher(Person):
    
    def __init__(self,name,average,subject):
        super().__init__(name,average,subject,[],"Yes") # Adult? Yes

class Item:
    itemManifest = []
    def __init__(self,item,total,count):
        self.item = item
        self.total = total
        self.count = count
        Item.itemManifest.append(self) # Appends itself to a list so It can be used to call index in list instead of typing each obj.

    def checkout(self,amount,person):
        self.amount = amount
        self.count = self.count-self.amount
        self.person = person
        if self.item not in person.materials:
            person.materials.append(self.item)
        # Appends to list if not in list; does nothing if in list
        # Note: I tried for a few hours to create a dict where it lists the item AND how many items checked out
        # I ended up ditching it because it would end up duplicating itself. 
        


    def query(self):
        return(f"Total: {self.total}, Available: {self.count}") #F strings are the future
