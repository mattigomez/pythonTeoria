## Variables
"""
my_string_variable = "My string variable"
print (my_string_variable)

# Int (entero)
my_int_variable = 5
print (my_int_variable)
"""
#pasamos de int a string
"""
my_int_to_str_variable = str(my_int_variable)
print (my_int_to_str_variable)
print (type(my_int_to_str_variable))

my_bool_variable = False
print (my_bool_variable)
"""
# Concatenacion de variables 
"""
print(my_string_variable, my_int_variable, my_bool_variable)
print("Este es el valor de:" , my_bool_variable)
"""
## Funciones del sistema 
""" 
# lenght cuenta caracteres
print (len(my_string_variable))
"""

# Variables en una sola linea, no es buena practica para un codigo escalable
"""
name, surname, alias, age = "Mati", "Gomez" , "MatiGo" , 26
print("Me llamo:", name,surname,"me dicen:" ,alias, "y tengo:",age,"años")
""" 
# Inputs
"""
first_name = input('What is your name: ')
age = input('How old are you? ')

print(first_name)
print(age)
"""
# Forzamos el tipo  ( tipado dinamico)
address: str = "mi direccion"
address = 32
address = 1.2
print(type(address))
