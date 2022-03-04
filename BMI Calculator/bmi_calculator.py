height = input("Enter height in meters: ")
weight = input("Enter weight in kilograms: ")

bmi = int(weight)/float(height) ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)