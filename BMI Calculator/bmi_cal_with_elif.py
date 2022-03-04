height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))

bmi = round(weight/height ** 2)

if bmi < 18.5:
    print(f"Your bmi is {bmi}, you're underweight")
elif bmi < 25:
    print(f"Your bmi is {bmi}, you're normal weight")
elif bmi < 30:
    print(f"Your bmi is {bmi}, you're overweight")
elif bmi < 35:
    print(f"Your bmi is {bmi}, you're obese")
else:
    print(f"Your bmi is {bmi}, you're clinically obese")   