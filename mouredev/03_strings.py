# Strings
"""
my_string = "mi string"
my_other_string = "mi otro string"

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "este es un string \ncon salto de linea"
print (my_new_line_string)

my_tab_string = "\t Este es un string con tabulacion"
print (my_tab_string)

my_scape_string = "\tEste es un string \nescapado"
print (my_scape_string)
"""

# Formateo
"""
name, surname, age = "Mati", "Gomez", 26

print ("Mi nombre es {} {} y mi edad es {}".format(name,surname,age))
print ("Mi nombre es %s %s y mi edad es %s" %(name,surname,age))
print (f"Mi nombre es {name} {surname} y mi edad es {age}") # esta es la forma mas practica
"""
# Desempaquetado de caracteres
"""
language = "Python"
a, b , c, d, e, f= language
print (language)
print(a)
print(e)
"""

# Division
"""
language = "Python"
language_slice = language[1:3] # yt
language_slice = language[1:] # ython
print(language_slice)
"""
# Reverse
"""
greeting = 'Python'
print(greeting[::-1]) # nohtyP
"""
#Funciones
language = "python"
print(language.capitalize()) # Primer letra mayuscula
print(language.upper().isupper()) # Todo letra mayuscula , isupper verifica si esta todo mayus
print(language.lower()) # Todo letra minuscula
print(language.count("t")) # Cuenta cantidad de letras t
print("1".isnumeric()) # si es un numero , rta boolean

