# Leer un archivo

with open("archivo.txt", "r") as archivo:

    contenido = archivo.read()

    print(contenido)

# Escribir un archivo

with open("archivo.txt", "w") as archivo:

    archivo.write("Hola, mundo!")

# Leer un archivo línea por línea

with open("archivo.txt", "r") as archivo:

    for linea in archivo:

        print(linea, end="")

# Leer un archivo en una lista

with open("archivo.txt", "r") as archivo:

    lineas = archivo.readlines()

    print(lineas)

# Escribir un archivo línea por línea

with open("archivo.txt", "w") as archivo:

    archivo.write("Línea 1\n")

    archivo.write("Línea 2\n")

    archivo.write("Línea 3\n")
