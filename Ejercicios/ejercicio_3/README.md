## Análisis del código Python

**Descripción:**

Este código presenta dos funciones:

1. `obtenerNumero()`:
   - Solicita al usuario un número entero.
   - Convierte el valor ingresado a tipo entero.
   - Retorna el número entero ingresado.
2. `esPar(num)`:
   - Determina si un número dado es par o impar.
   - Imprime un mensaje indicando si el número es par o impar.

**Entrada:**

- El usuario ingresa un número entero a través de la función `obtenerNumero()`.

**Salida:**

- Se imprime un mensaje indicando si el número ingresado es par o impar.

**Explicación paso a paso:**

**Función `obtenerNumero()`:**

1. **Solicita el número:**
   - Se utiliza la función `input()` para mostrar un mensaje al usuario indicando que ingrese un número entero.
   - El valor ingresado por el usuario se almacena como cadena de texto en la variable `num`.
2. **Convierte el número a tipo entero:**
   - Se utiliza la función `int()` para convertir la cadena de texto `num` a un número entero.
   - El valor entero convertido se almacena en la variable `num`.
3. **Retorna el número:**
   - Se utiliza la instrucción `return` para devolver el valor de la variable `num`.

**Función `esPar(num)`:**

1. **Verifica si el número es par:**
   - Se utiliza el operador `%` para calcular el residuo de la división de `num` por 2.
   - Si el residuo es 0, significa que el número es par.
   - Si el residuo es distinto de 0, significa que el número es impar.
2. **Imprime el mensaje correspondiente:**
   - Se utiliza una sentencia `if-else` para determinar el mensaje a imprimir:
     - Si el número es par, se imprime un mensaje indicando que es par.
     - Si el número es impar, se imprime un mensaje indicando que es impar.

**Ejemplo de ejecución:**

**Entrada:**

- Número: 8

**Salida:**

```
El número 8 es par.
```

**Comentarios adicionales:**

- El código está bien estructurado y utiliza funciones para separar las responsabilidades.
- Se utiliza una sentencia `if-else` para verificar si un número es par o impar de manera clara y concisa.
- Se podría mejorar el código agregando la capacidad de verificar si el usuario ingresa un valor válido (un número entero).
