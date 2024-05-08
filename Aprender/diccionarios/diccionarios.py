# Definición de un diccionario

persona = {"nombre": "Juan", "edad": 25, "altura": 1.75}


# Acceso a elementos del diccionario


print(persona["nombre"])  # Juan


print(persona["edad"])  # 25


print(persona["altura"])  # 1.75


# Modificación de elementos del diccionario


persona["edad"] = 30


print(persona)  # {'nombre': 'Juan', 'edad': 30, 'altura': 1.75}


# Agregar elementos al diccionario


persona["peso"] = 70


print(persona)  # {'nombre': 'Juan', 'edad': 30, 'altura': 1.75, 'peso': 70}


# Eliminar elementos del diccionario


del persona["altura"]


print(persona)  # {'nombre': 'Juan', 'edad': 30, 'peso': 70}
