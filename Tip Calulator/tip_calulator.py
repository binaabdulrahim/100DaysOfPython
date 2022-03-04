print("Welcome to the tip calculator ")
starting_bill = float(input("What was the total bill? "))
person = float(input("How many people to split the bill? "))
percentage = int(input("What percentage tip would you like to give? 10, 12, 15, or 18 "))

total_bill = (starting_bill*(1+percentage/100))
payment_per_person = round(total_bill/person,2)

#f string goes in front of the "" & input the variable inside a set of {}
print(f"Each person should pay: {payment_per_person} ")