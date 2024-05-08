# Definición de una clase


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")


# que es self?
# self es una referencia al objeto actual que se está creando o manipulando. Es similar a la palabra clave this en otros lenguajes de programación.

# Creación de un objeto

juan = Persona("Juan", 25)

# Llamada a un método del objeto

juan.saludar()  # Hola, mi nombre es Juan y tengo 25 años.
