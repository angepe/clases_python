# Determinar si un estudiante aprobó o no
# Descripción: Crea un programa que pida la calificación de un estudiante
# y determine si ha aprobado (60 o más) o no.

def pedir_nota():
    while True:
        try:
            nota = float(input("Por favor, ingresa la nota del estudiante: "))
            return nota
        except ValueError:
            print("Eso no es un número válido. Inténtalo de nuevo.")

def evaluar_nota(nota):
    if nota >= 60:
        print("El estudiante aprobo.")
    else:
        print("El estudiante reprobo.")

# Uso de la función
nota = pedir_nota()
evaluar_nota(nota)            