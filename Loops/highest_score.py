#Write a program that calculates the highest score from a List of scores
#Use For Loops to figure out the average
#Cannot use min or max function 
#Round it to nearest whole number

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
	student_scores[n] = int(student_scores[n])
print(student_scores)

#max function in for loop 
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")


# #min function in for loop
# lowest_score = 0
# # for score in student_scores:
#     if score < lowest_score: 
#         lowest_score = score
# print(f"The lowest score in the class is: {lowest_score}")

