# Declarar la Función
# palabra def nombre_funcion
# funciones por lo general reciben parametros
# la palabra return devuelve un resultado


def sumar(numero_1, numero_2):
    numero_final = numero_1 + numero_2
    return numero_final


def imprimir_hola():
    return print("hola")


# Llamar la función

suma = sumar(1, 3)
print(suma)
print(sumar(20, 40))

imprimir_hola()