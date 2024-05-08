# Leer un archivo

with open("archivo.txt", "r") as archivo:

    contenido = archivo.read()

    print(contenido)

# Escribir un archivo

with open("archivo.txt", "w") as archivo:

    archivo.write("Hola, mundo!")
