print("Welcome to the Pizza Devliveries!")
size = input("What size pizza would you want to order? S, M, or L ")
add_pepperoni = input ("Do you want to add pepperoni? Y or N ")
extra_cheese = input ("Do you want extra cheese? Y or N ")

bill = 0

if size == "S":
    bill +=15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if extra_cheese == "Y":
    bill += 1
    
print(f"Your final bill is ${bill}. ")