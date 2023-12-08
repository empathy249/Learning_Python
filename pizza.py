#Congratulations, you've got a job at Python Pizza! Your first job is to build
#an automatic pizza order program.
#Based on a user's order, work out their final bill.
#Small pizza (S): $15
#Medium pizza (M): $20
#Large pizza (L): $25
#Add pepperoni for small pizza (Y or N): +$2
#Add pepperoni for medium or large pizza (Y or N): +$3
#Add extra cheese for any size pizza (Y or N): +$1

print("Welcome to python pizza!")

size = input("What size pizza would you like: S, M, or L ").lower()
if size != "s" or "m" or "l":
    print("Please only enter S, M, or L")
    size = input("What size pizza would you like: S, M, or L ").lower()
else:
    print("\n")

extraCheese = input("Would you like extra cheese? Y or N ").lower()
if extraCheese != "y" or "n":
    print("Please only enter Y or N")
    extraCheese = input("Would you like extra cheese? Y or N ").lower()
else:
    print("\n")

toppings = input("Would you like pepperoni on your pizza? Y or N ").lower()
if toppings != "y" or "n":
    print("Please only enter Y or N")
    toppings = input("Would you like pepperoni on your pizza? Y or N ").lower()
else:
    print("\n")

price = 0

if size == "s":
    price = 15
    if extraCheese == "y":
        price += 1
    if toppings == "y":
        price += 2
if size == "m":
    price = 20
    if extraCheese == "y":
        price += 1
    if toppings == "y":
        price += 3
if size == "l":
    price = 25
    if extraCheese == "y":
        price += 1
    if toppings == "y":
        price += 3
else:
    print("Please only enter S, M, or L")

print(f"Thank you for choosing python pizza! Your order total is ${price}")