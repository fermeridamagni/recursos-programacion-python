## Análisis del código Python

**Instrucciones:**

- Escribe un programa que solicite al usuario su nombre y su edad, y luego imprima un mensaje que diga "Hola, [nombre]! Tienes [edad] años.".

**Descripción:**

Este código presenta dos funciones:

1. `obtenerDatosDeUsuario()`:
   - Solicita al usuario su nombre y edad.
   - Convierte la edad ingresada a tipo entero.
   - Retorna el nombre y la edad como un tuple.
2. `mostrarDatosDeUsuario(nombre, edad)`:
   - Imprime un mensaje con el nombre y la edad del usuario, utilizando la técnica de formateo de cadenas `f-strings`.

**Entrada:**

- El usuario ingresa su nombre y edad a través de la función `obtenerDatosDeUsuario()`.

**Salida:**

- La función `mostrarDatosDeUsuario()` imprime un mensaje con el nombre y la edad del usuario.

**Explicación paso a paso:**

**Función `obtenerDatosDeUsuario()`:**

1. **Solicita el nombre del usuario:**
   - Se utiliza la función `input()` para mostrar un mensaje al usuario indicando que ingrese su nombre.
   - El valor ingresado por el usuario se almacena en la variable `nombre`.
2. **Solicita la edad del usuario:**
   - Se utiliza la función `input()` para mostrar un mensaje al usuario indicando que ingrese su edad.
   - El valor ingresado por el usuario se almacena como cadena de texto en la variable `edad`.
3. **Convierte la edad a tipo entero:**
   - Se utiliza la función `int()` para convertir la cadena de texto `edad` a un número entero.
   - El valor entero convertido se almacena en la variable `edad`.
4. **Retorna el nombre y la edad:**
   - Se utiliza la instrucción `return` para devolver un tuple que contiene las variables `nombre` y `edad`.

**Función `mostrarDatosDeUsuario(nombre, edad)`:**

1. **Imprime un mensaje con el nombre y la edad:**
   - Se utiliza la técnica de formateo de cadenas `f-strings` para crear un mensaje que incluye el nombre y la edad del usuario.
   - El mensaje se imprime utilizando la función `print()`.

**Ejemplo de ejecución:**

**Entrada:**

- Nombre: Juan
- Edad: 30

**Salida:**

```
Su nombre es Juan y su edad es 30
```

**Comentarios adicionales:**

- El código está bien estructurado y utiliza funciones para separar las responsabilidades.
- Se utiliza la técnica de formateo de cadenas `f-strings` para mejorar la legibilidad del mensaje impreso.
- Se podría mejorar el código agregando validación de entrada para verificar que el usuario ingrese un nombre válido y una edad numérica.
