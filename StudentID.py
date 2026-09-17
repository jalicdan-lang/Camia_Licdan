import re

ID = input("Please enter your student ID: ")

B = r"\d{4}-\d{4}"

if re.fullmatch(B,ID):
    print("Valid ID")
else:
    print("Invalid ID")






