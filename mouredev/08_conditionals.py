# Conditionals
# Establecer flujo de codigo mediante condicionales

my_condition = False 

if my_condition:
    print("Se ejecuta la condicion del if")

my_condition = 5 *5

if my_condition == 10:
    print("Se ejecuta la condicion del segundo if")


if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
elif my_condition == 25:
    print("Es igual a 25")
#si cumple el elif no entra en el else
else:
    print ("Es menor que 10 o mayor que 20")
    #si esta a esta altura(sangria/tabulacion) sigue en el else.   

# Orden de jerarquia : 1. if 2. elif 3. else



print("La ejecucion continua")


