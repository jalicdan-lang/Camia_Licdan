
try:
    score = input("Please input your examination score: ")
    if 100 >= score >= 0:
        print("Valid score")
    else:
        print("Please enter a value between 0 and 100")
except ValueError:
    print("Invalid input, please enter a number")












