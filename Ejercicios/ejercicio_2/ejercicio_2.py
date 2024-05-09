# Escribe un programa que solicite al usuario dos números enteros, y luego imprima la suma, resta, multiplicación, división, división entera, residuo y potencia de los dos números.


def obtenerNumeros():
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))

    return num1, num2


def hacerOperaciones():
    num1, num2 = obtenerNumeros()

    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = num1 / num2
    divisionEntera = num1 // num2
    residuo = num1 % num2
    potencia = num1**num2

    print(f"La suma de {num1} y {num2} es: {suma}")

    print(f"La resta de {num1} y {num2} es: {resta}")

    print(f"La multiplicación de {num1} y {num2} es: {multiplicacion}")

    print(f"La división de {num1} y {num2} es: {division}")

    print(f"La división entera de {num1} y {num2} es: {divisionEntera}")

    print(f"El residuo de {num1} y {num2} es: {residuo}")

    print(f"La potencia de {num1} elevado a {num2} es: {potencia}")


hacerOperaciones()
