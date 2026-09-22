
try:
    level = int(input("Enter grade level: "))
    if level >= 7 and level <= 12:
        print("Invalid input")
except ValueError:
    print("Invalid input")






