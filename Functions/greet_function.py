# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
    print("Hello")
    print("How is it going? ")
    print("What's going on? ")
greet()

#function that allows for input 
#'name' is the parameter
#'Sarah' i sthe argument
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How is it going {name} ?")
    print(f"What's going on {name}?")
greet_with_name("Sarah")