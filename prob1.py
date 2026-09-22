
try:
    age = int(input("Enter your age: "))
    if age >= 12 and age <= 18:
        print("Valid age")
except ValueError:
    print("Invalid input. Please enter a whole number")






