
sub = 0
add = 0
n1 = int(input("Enter a number: "))
n2 = int(input("Enter another number: "))

def subtract():
    global sub
    sub = n1 - n2
    print(f"The difference of {n1} and {n2} is {sub}")

def addition():
    global add
    add = n1 + n2
    print(f"The sum of {n1} and {n2} is {add}")

addition()
subtract()




























