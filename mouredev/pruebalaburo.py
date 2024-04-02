#Se deben completar las funciones proporcionadas para que al correr la función main() devuelva el resultado esperado.
lista_personas = [
    ('11111111', 'Pedro', 'Paez', 24),
    ('22222222', 'Fito', 'Garcia', 23),
    ('33333333', 'Leo', 'Peralta', 26),
    ('44444444', 'Bruno', 'Mac', 25),
    ('55555555', 'Nico', 'Zaoral', 27),
    ('44444444', 'Bruno', 'Mac', 25),
]

print (type(lista_personas))
def ordenar(lista_personas):
    """El método debe devolver una lista con las edades ordenadas de menor a mayor"""
    return sorted([persona[3] for persona in lista_personas])


def convertir_a_diccionario(lista_personas):
    """Hacer un diccionario que tenga como claves los “dni” y como valores tuplas con nombre, apellido y edad"""
    diccionario = {}
    for dni, nombre, apellido, edad in lista_personas:
        diccionario[dni] = (nombre, apellido, edad)
    return diccionario

##### ver ####
def devolver_edad(lista_personas, dni):
    """Para la 'lista_personas' devuelve la edad de la persona que tenga el dni definido."""
    diccionario = convertir_a_diccionario(lista_personas)
    return diccionario.get(dni, "DNI no encontrado")


def eliminar_repetidos(lista_personas):
    """El método debe devolver los elementos únicos"""
    return list(set(lista_personas))


def separar_por_edad(lista_personas):
    """Devolver dos listas
    * lista 1: mayores de 25 (incluido)
    * lista 2: menores de 25
    """
    mayores_de_25 = []
    menores_de_25 = []
    for persona in lista_personas:
        if persona[3] >= 25:
            mayores_de_25.append(persona)
        else:
            menores_de_25.append(persona)
    return mayores_de_25, menores_de_25


def obtener_promedio(lista):
    """Implementar obtener el promedio de la lista de números que se recibe.
    Capturar con un try/except la excepción de dividir por cero"""
    try:
        promedio = sum(lista) / len(lista)
    except ZeroDivisionError:
        return "No se puede calcular el promedio de una lista vacía"
    return promedio


def main():
    """Este método no debe modificarse y es solo a fines de probar el código"""
    print('Resultados:\n')
    print(' * Edades ordenadas: %s\n' % ordenar(lista_personas))
    print(' * Elementos como diccionario: %s\n' % convertir_a_diccionario(lista_personas))
   # print(' * La edad para dni 55555555 es: %s\n' % devolver_edad(lista_personas, '55555555'))
    print(' * Elementos únicos: %s\n' % eliminar_repetidos(lista_personas))
    print(' * Los mayores de 25 son: %s\n' % separar_por_edad(lista_personas)[0])
    print(' * Los menores de 25 son: %s\n' % separar_por_edad(lista_personas)[1])
    print(' * El promedio de las edades es: %s\n' % obtener_promedio(ordenar(lista_personas)))
    print(' * El promedio de una lista vacía es: %s\n' % obtener_promedio([]))


if __name__ == "__main__":
    main()

