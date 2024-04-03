# Loops

# While / mientras

my_condition = 0

# imprime infinitas veces 0
while my_condition <= 10:
    print(my_condition)
    my_condition += 2
else: # es opcional
    print("Mi condicion es mayor que 10")

print ("La ejecucion continua")

while my_condition < 20:
    my_condition += 2
    if my_condition == 16:
        print("Mi condicion es 16, se detiene")
        break
    print(my_condition)

print ("La ejecucion continua")
    
# For   / sirve para iterar un listado de elementos
# 7hs 4min