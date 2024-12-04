HST = 0.13
LABOUR = 0.75
RENT = 1
MATERIAL = 0.5
diameter = float(input("What is the diameter of the pizza you want? (in) "))
subtotal = RENT + LABOUR + (diameter * MATERIAL)
tax = subtotal * HST
total = subtotal + tax
print("Your total is: $", total)