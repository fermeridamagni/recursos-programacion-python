# Manejo de excepciones

# Las excepciones son errores que ocurren durante la ejecución de un programa. Python proporciona un mecanismo para manejar excepciones que permite al programador controlar lo que sucede cuando ocurre un error.
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Error: división por cero")
