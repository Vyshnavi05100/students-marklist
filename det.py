from db import *
import sys
class Login:
    def __init__(self):
        self.data = Info()
        self.login_reg()

    def login_reg(self):
        print("=============Markslist=============")
        print("1. Register")
        print("2. Login")
        n = int(input("Enter your choice:"))
        if n == 1:
            self.register()
        elif n == 2:
            self.login()
        else:
            print("Invalid choice")

    def register(self):
        rollno = int(input("Enter the rollno:"))
        name=input("Enter the student name:")
        self.data.insert(rollno,name)
        print("Registration successful!")

    def login(self):
        rollno =int(input("Enter the student number:"))
        name=input("Enter the student name:")
        self.data.insert(rollno,name)
        
        if not self.data:
            print("No data found!! Please register first.")
        else:
            print("Data found!!")
            self.marks(rollno,name)

    def marks(self,rollno,name):
        print("Enter the marks:")
        telugu = int(input("Marks in Telugu:"))
        hindi = int(input("Marks in Hindi:"))
        english = int(input("Marks in English:"))
        maths = int(input("Marks in Maths:"))
        science = int(input("Marks in Science:"))
        social = int(input("Marks in Social:"))
        total = telugu + hindi + english + maths + science + social
        print("Total marks:", total)
        self.per(rollno,name, total)

    def per(self,rollno,name, total):
        percentage = (total / 600) * 100
        print("Percentage:", percentage)
        self.grade( rollno,name, total, percentage)

    def grade(self, rollno,name, total, percentage):
        if percentage >= 85 and percentage <= 100:
            grade = "A"
        elif percentage >= 70 and percentage < 85:
            grade = "B"
        elif percentage >= 55 and percentage < 70:
            grade = "C"
        elif percentage >= 40 and percentage < 55:
            grade = "D"
        else:
            grade = "Fail"
        print("Grade:", grade)
        # Insert the marks info into database
        self.data.insert( rollno,name, total, percentage, grade)
        return(0)
obj=Login()
sys.exit()
