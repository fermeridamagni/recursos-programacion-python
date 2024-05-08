### 2.2.10. Excepciones

Las excepciones son errores que ocurren durante la ejecución de un programa. En Python, las excepciones se manejan utilizando bloques `try` y `except`.

```python
# Manejo de excepciones


try:
    x = 10 / 0
except ZeroDivisionError:
    print("Error: división por cero")

```
