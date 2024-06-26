import random, string

number_of_digits = 3
number_of_punctuation_characters = 2
characters = string.ascii_letters + string.digits + string.punctuation

number_of_passwords = int(input("How many passwords do you want to generate? "))
password_length = int(input("Provide the password length: "))

for password_index in range(number_of_passwords):
    password = ""

    for digits_index in range(number_of_digits):
        password = password + random.choice(string.digits)

    for punctuation_index in range(number_of_punctuation_characters):
        password = password + random.choice(string.punctuation)

    for index in range(password_length - number_of_digits - number_of_punctuation_characters):
        password = password + random.choice(string.ascii_letters)

    print("Password {} generated: {}".format(password_index, password))
