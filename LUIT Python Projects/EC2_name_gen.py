'''**EC2 Random Name Generator**

Several departments share an AWS environment. You need to ensure that the EC2s are properly named and are unique so team members can easily tell who the EC2 instances belong to. Use Python to create your unique EC2 names that the users can then attach to the instances. The Python Script should:
1. All the user to input how many EC2 instances they want names for and output the same amount of unique names.
2. Allow the user to input the name of their department that is used in the unique name.
3. Generate random characters and numbers that will be included in the unique name'''

import random, string
characters = string.ascii_letters + string.digits + string.punctuation
while 1:
    ec2_count = int(input("How many EC2 instances do you want names for? "))
    ec2_len = int(input("What length would you like your EC2 name to be? "))
    name_of_dept = str(input("What is the name of your dept? "))
    for x in range(0,ec2_count):
        ec2 = ""
        for x in range(0, ec2_len):
            ec2_chars = random.choice(characters)
            ec2 = ec2 + ec2_chars
        print("here is the EC2 Names: ", ec2 + name_of_dept )
    


    
