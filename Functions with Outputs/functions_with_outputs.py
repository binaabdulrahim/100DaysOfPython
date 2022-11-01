#Functions with outputs
#Create a function called format_name that returns a string
def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"
    
formated_string = format_name("bina", "BINA")
print(formated_string) 

#Or you can do this print(formated_name("bina", "Bina"))

