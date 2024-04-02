# Listas

#my_list = list()
my_other_list = []

# print(len(my_list))

my_list = [35,24,62,52,30,30,17]
my_other_list = [35, 1.77, "Brais", "Moure"]
"""
print(my_list)
print(len(my_list))


print( type(my_other_list))

print(my_other_list[0]) 
print(my_other_list[1]) 
print(my_other_list[-1]) 
print(my_other_list[-3]) 
print(my_other_list.count("Brais")) # cuenta cantidad de veces que se encuentra la variable
print(my_list.count(30)) # cuenta cantidad de veces que se encuentra la variable


age, height , name , surname = my_other_list
print(name )

print(my_list + my_other_list)

my_other_list.append("MoureDev")
print(my_other_list)


my_other_list.remove("Rojo")
print(my_other_list)
"""

# insert agrega por indice a la lista... append agrega el elemento a lo ultimo de la lista
my_other_list.insert(1, "Rojo")
print(my_other_list)


my_other_list[1] = "Azul"
print(my_other_list)

my_list.remove(30)
print(my_list)

# pop saca un elemento de la lista, por defecto el -1 , el ultimo
my_pop_element = my_list.pop(0)
print(my_pop_element)
print(my_list)

del my_list[1]
print(my_list)
# remove elimina el primer elemento que coincide... del elimina por indice

#copiamos lista antes de darle clear y vaciarla
my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

#reverse imprime los valores de la list al revez
my_new_list.reverse()
print(my_new_list)

#sort ordena de mayor a menor
my_new_list.sort()
print(my_new_list)

#agarra el elemento del 1 al 3 sin incluirlo
print(my_new_list[1:3])

my_list = "hello python"
# si ponemos "" entre [] = queda type list
# si ponemos "" entre {} = queda type set
print(type(my_list))