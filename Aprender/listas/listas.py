# Definición de una lista

numeros = [1, 2, 3, 4, 5]


# Acceso a elementos de la lista


print(numeros[0])  # 1


print(numeros[1])  # 2


print(numeros[2])  # 3


# Modificación de elementos de la lista


numeros[0] = 10


print(numeros)  # [10, 2, 3, 4, 5]


# Agregar elementos a la lista


numeros.append(6)


print(numeros)  # [10, 2, 3, 4, 5, 6]


# Eliminar elementos de la lista


numeros.remove(3)


print(numeros)  # [10, 2, 4, 5, 6]
