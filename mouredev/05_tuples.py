### Tuples

my_tuple = tuple()
my_other_tuple = (50,20,30)


my_tuple = (35, 1.77 , "Brais" , "Moure" , 35)
print(my_tuple)
print(type(my_tuple))

print(my_tuple[1]) 
print(my_tuple[-1]) 

print(my_tuple.count(35))
print(my_tuple.index("Moure")) 
print(my_tuple.index(35)) # devuelve el primer 35 que encuentra

print(my_tuple)
print(my_other_tuple)

"""
da error el siguiente codigo ya que en la tupla 
los elementos son constantes 
y no permiten modificarse

my_tuple[1] = 1.80
print(my_tuple)
"""
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])
# transformo en list
my_tuple = list(my_tuple)
print(type(my_tuple))
print(my_tuple)
# Ahora si puedo modificar indice 0 y agregar en el 1 azul
my_tuple[0] = 40
my_tuple.insert(1,"Azul")

# vuelvo a transformar en tupla
my_tuple= tuple(my_tuple)
print(tuple(my_tuple))
print(type(my_tuple))

# la tupla se puede usar , no se puede modificar

del my_tuple
print (my_tuple)
