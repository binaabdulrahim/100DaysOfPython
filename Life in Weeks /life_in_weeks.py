name = input("What is your name? ")
age = input("What is your current age? ")

#Calculation

age_as_int = int(age)
years = 90 - age_as_int
days = years * 365
weeks = years * 52
months = years * 12


message= f"You have {years} years, {days} days, {weeks} weeks, {months} months remaining"
print(message)



