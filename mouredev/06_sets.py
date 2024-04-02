# Sets

my_set = set()
my_other_set = {} # dict = diccionario

print(type(my_set))
print(type(my_other_set)) 

my_other_set = {"Brais", "Moure", 35 }
print(type(my_other_set)) 

print(my_other_set) # imprime con ubicaciones al azar

print(len(my_other_set))

my_other_set.add("Mouredev")

print(my_other_set) 
"""Un set no es una estructura ordenada, cuando usamos add 
se agrega en una posicion aleatoria """

my_other_set.add("Mouredev") # add no admite repetidos, por eso lo muestra 1 sola vez
# tuplas y list si admiten repetidos

# comprobamos si esta moure y mouri en el set . Rta boolean
print("Moure" in my_other_set)
print("Mouri" in my_other_set)

my_other_set.remove("Moure")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))
print(my_other_set)


"""lo paso a lista y ahora si puedo agarrar un elemento
 (el q se encuentre en esa posicion en la ejecucion)
 NO OLVIDAR que cada vez q se genere el set 
 los elementos tomaran indices al azar 
 """
my_set = {"Brais", "Moure", 35 }
my_list = list(my_set)

print(my_list)
print(my_list[0])

my_other_set = {"Python", "JavaScript", "React"}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union({"C#","NodeJs","React"})) 
#React imprime 1 sola vez porque no acepta q se repita

print("my_set:", my_set)
print("my_new_set:", my_new_set)
print(my_new_set.difference(my_set))