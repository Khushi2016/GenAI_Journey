# 1 password checker 

password = input("Enter password: ")
if password == "admin123":
    print("Login Successful")
else:
    print("Wrong Password")

# voting eligibility

age = int(input("Enter age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")

# Student Grade System

marks = int(input("Enter student marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
elif marks > 100:
    print("Invalid Marks")
else:
    print("Fail")