## Análisis del código Python

**Indicaciones:**

- Escribe un programa que solicite al usuario dos números enteros, y luego imprima la suma, resta, multiplicación, división, división entera, residuo y potencia de los dos números.

**Descripción:**

Este código presenta dos funciones:

1. `obtenerNumeros()`:
   - Solicita al usuario dos números enteros.
   - Convierte los valores ingresados a tipo entero.
   - Retorna ambos números como un tuple.
2. `hacerOperaciones()`:
   - Llama a la función `obtenerNumeros()` para obtener dos números del usuario.
   - Realiza las siguientes operaciones con los números obtenidos:
     - Suma
     - Resta
     - Multiplicación
     - División
     - División entera
     - Residuo
     - Potencia
   - Imprime el resultado de cada operación utilizando la técnica de formateo de cadenas `f-strings`.

**Entrada:**

- El usuario ingresa dos números enteros a través de la función `obtenerNumeros()`.

**Salida:**

- Se imprimen los resultados de las operaciones matemáticas realizadas con los números ingresados.

**Explicación paso a paso:**

**Función `obtenerNumeros()`:**

1. **Solicita el primer número:**
   - Se utiliza la función `input()` para mostrar un mensaje al usuario indicando que ingrese el primer número.
   - El valor ingresado por el usuario se almacena como cadena de texto en la variable `num1`.
2. **Convierte el primer número a tipo entero:**
   - Se utiliza la función `int()` para convertir la cadena de texto `num1` a un número entero.
   - El valor entero convertido se almacena en la variable `num1`.
3. **Solicita el segundo número:**
   - Se utiliza la función `input()` para mostrar un mensaje al usuario indicando que ingrese el segundo número.
   - El valor ingresado por el usuario se almacena como cadena de texto en la variable `num2`.
4. **Convierte el segundo número a tipo entero:**
   - Se utiliza la función `int()` para convertir la cadena de texto `num2` a un número entero.
   - El valor entero convertido se almacena en la variable `num2`.
5. **Retorna los números:**
   - Se utiliza la instrucción `return` para devolver un tuple que contiene las variables `num1` y `num2`.

**Función `hacerOperaciones()`:**

1. **Obtiene los números:**
   - Se llama a la función `obtenerNumeros()` para obtener dos números del usuario.
   - Los valores retornados por `obtenerNumeros()` se almacenan en las variables `num1` y `num2`.
2. **Realiza las operaciones:**
   - Se realizan las siguientes operaciones matemáticas con los números `num1` y `num2`:
     - Suma: `suma = num1 + num2`
     - Resta: `resta = num1 - num2`
     - Multiplicación: `multiplicacion = num1 * num2`
     - División: `division = num1 / num2`
     - División entera: `divisionEntera = num1 // num2`
     - Residuo: `residuo = num1 % num2`
     - Potencia: `potencia = num1**num2`
3. **Imprime los resultados:**
   - Se utiliza la técnica de formateo de cadenas `f-strings` para crear mensajes que incluyen los resultados de cada operación.
   - Los mensajes se imprimen utilizando la función `print()`.

**Ejemplo de ejecución:**

**Entrada:**

- Primer número: 10
- Segundo número: 5

**Salida:**

```
La suma de 10 y 5 es: 15
La resta de 10 y 5 es: 5
La multiplicación de 10 y 5 es: 50
La división de 10 y 5 es: 2.0
La división entera de 10 y 5 es: 2
El residuo de 10 y 5 es: 0
La potencia de 10 elevado a 5 es: 100000
```

**Comentarios adicionales:**

- El código está bien estructurado y utiliza funciones para separar las responsabilidades.
- Se utiliza la técnica de formateo de cadenas `f-strings` para mejorar la legibilidad de los mensajes impresos.
- Se podría mejorar el código agregando manejo de errores para situaciones donde el usuario ingrese valores no válidos, como letras o números con punto decimal.
