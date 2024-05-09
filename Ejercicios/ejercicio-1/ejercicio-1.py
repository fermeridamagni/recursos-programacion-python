# Escribe un programa que solicite al usuario su nombre y su edad, y luego imprima un mensaje que diga "Hola, [nombre]! Tienes [edad] años.".


def obtenerDatosDeUsuario():
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))

    return nombre, edad


def mostrarDatosDeUsuario(nombre, edad):
    print(f"Su nombre es {nombre} y su edad es {edad}")


nombre, edad = obtenerDatosDeUsuario()

mostrarDatosDeUsuario(nombre, edad)
