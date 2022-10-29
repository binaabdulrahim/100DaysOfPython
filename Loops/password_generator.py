#Write a program that automatically generates pw for you

import random, string
characters = string.ascii_letters + string.digits + string.punctuation
while 1:
    pw_count = int(input("How many password you like to generate? "))
    pw_len = int(input("What length would you like your passwords to be? "))
    name_of_dept = str(input("What is the name of your dept? "))
    for x in range(0,pw_count):
        pw = ""
        for x in range(0, pw_len):
            pw_chars = random.choice(characters)
            pw = pw + pw_chars
        print("here is the passwords: ", pw + name_of_dept )