# Escribe un programa que solicite al usuario un número entero, y luego imprima si el número es par o impar.


def obtenerNumero():
    num = int(input("Ingrese un número entero: "))

    return num


def esPar(num):
    if num % 2 == 0:
        print(f"El número {num} es par.")
    else:
        print(f"El número {num} es impar.")


num = obtenerNumero()

esPar(num)
