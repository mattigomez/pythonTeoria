# Dictionaries

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = { "Nombre":"Brais", "Apellido":"Moure", "Edad":35, 1:"Python"}

my_dict =  { "Nombre":"Brais",
             "Apellido":"Moure",
             "Edad":35,
             "Lenguajes":{"Python","Swift","Kotlin"},
             1:1.77
           }

print(my_other_dict)
print(my_dict)
#imprimo x nombre de clave
print(my_dict["Nombre"])

# cambio de valor en una clave
my_dict["Nombre"] = "Pepe"
print(my_dict[1])

# agrego clave valor
my_dict["Calle"] = "Casiano"
print(my_dict)

# elimino un elemento/clave
del my_dict["Calle"]
print(my_dict)

#cuando se busca, se tiene q buscar por la clave no por el valor
print("Moure" in my_dict)
print("Apellido" in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list = ["Nombre",1, "Ciudad"]

#creamos nuevo diccionario con claves sin valores
my_new_dict = my_other_dict.fromkeys((my_list))
print(my_new_dict)
# otra forma de hacerlo
my_new_dict = my_other_dict.fromkeys(("Nombre",1, "Ciudad"))
print(my_new_dict)


my_new_dict = my_other_dict.fromkeys(my_dict)
print(my_new_dict)

print(list(my_new_dict)) # list []
print(tuple(my_new_dict)) # tuple ()
print(set(my_new_dict)) # set {}