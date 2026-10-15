
n1 = int(input("Enter a number: "))
n2 = int(input("Enter another number: "))

def subtract(n1,n2):
    subv = n1 - n2
    return subv
sub = subtract(n1,n2)

def addition(n1,n2):
    addv = n1 + n2
    return addv
add = addition(n1,n2)

def multiplication(n1,n2):
    mulv = n1 * n2
    return mulv
mul = multiplication(n1,n2)

def division(n1,n2):
    divv = n1 / n2
    return divv
div = division(n1,n2)

print(f"The difference of {n1} and {n2} is {sub}")
print(f"The sum of {n1} and {n2} is {add}")
print(f"The product of {n1} and {n2} is {mul}")
if n2 == 0:
    print("Cannot divide by zero")
else:
    print(f"The quotient of {n1} and {n2} is {div:.2f}")


























