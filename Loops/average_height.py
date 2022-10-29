#Write a program that calculates the average student heights from a list of heights
#Use For Loops to figure out the average
#Cannot use sum or len function 
#Round it to nearest whole number

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
	student_heights[n] = int(student_heights[n])
print(student_heights)

#sum function in for loop 
total_height = 0
for height in student_heights:
	total_height += height
print(f"The total height is: {total_height}")

#len function in for loop
number_of_students = 0
for students in student_heights:
    number_of_students += 1
print(f"The number of students are: {number_of_students}")

