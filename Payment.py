
yes_payments = ["gcash","card","cash"]

payment = input("Please payment method: ").lower()

if payment in yes_payments:
    print("Valid payment method")
else:
    print("Invalid payment method")




