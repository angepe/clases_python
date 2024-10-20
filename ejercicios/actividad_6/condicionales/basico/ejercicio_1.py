# Verificar si un número es positivo, negativo o cero
# Descripción: Crea un programa que pida al usuario un número y verifique
# si es positivo, negativo o cero.

def pedir_numero():
    while True:
        try:
            numero = float(input("Por favor, ingresa un número (puede ser negativo o positivo): "))
            return numero
        except ValueError:
            print("Eso no es un número válido. Inténtalo de nuevo.")

def evaluar_numero(numero):
    if numero > 0:
        print("El número es positivo.")
    elif numero < 0:
        print("El número es negativo.")
    else:
        print("El número es cero.")

# Uso de la función
numero = pedir_numero()
evaluar_numero(numero)

