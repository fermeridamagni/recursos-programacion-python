### 2.2.4. Operadores

Python cuenta con varios operadores que permiten realizar operaciones aritméticas, lógicas y de comparación. Algunos de los operadores más comunes son:

- Operadores aritméticos:`+`,`-`,`*`,`/`,`//`,`%`,`**`.
- Operadores de comparación:`==`,`!=`,`>`,`<`,`>=`,`<=`.
- Operadores lógicos:`and`,`or`,`not`.

```python
# Operadores aritméticos

a = 10
b = 3

suma = a + b

resta = a - b

multiplicacion = a * b

division = a / b

division_entera = a // b

residuo = a % b

potencia = a**b

print(f"Suma: {suma}")

print(f"Resta: {resta}")

print(f"Multiplicación: {multiplicacion}")

print(f"División: {division}")

print(f"División entera: {division_entera}")

print(f"Residuo: {residuo}")

print(f"Potencia: {potencia}")


# Operadores de comparación
x = 10
y = 20

print(f"x == y: {x == y}")

print(f"x != y: {x != y}")

print(f"x > y: {x > y}")

print(f"x < y: {x < y}")

print(f"x >= y: {x >= y}")

print(f"x <= y: {x <= y}")


# Operadores lógicos
p = True
q = False

print(f"p and q: {p and q}")

print(f"p or q: {p or q}")

print(f"not p: {not p}")

print(f"not q: {not q}")

# Operadores de identidad
a = 10
b = 10
c = 20

print(f"a is b: {a is b}")

print(f"a is c: {a is c}")

print(f"a is not b: {a is not b}")

print(f"a is not c: {a is not c}")

# Operadores de pertenencia

lista = [1, 2, 3, 4, 5]

print(f"1 in lista: {1 in lista}")

print(f"6 in lista: {6 in lista}")

print(f"1 not in lista: {1 not in lista}")

print(f"6 not in lista: {6 not in lista}")

# Operadores de asignación

a = 10

a += 5

print(a)  # 15

a -= 5

print(a)  # 10

a *= 2

print(a)  # 20

a /= 4

print(a)  # 5.0

a //= 2

print(a)  # 2.0

a %= 2

print(a)  # 0.0

a **= 3

print(a)  # 0.0

a = 10

a &= 2

print(a)  # 2

a = 10

a |= 2

print(a)  # 10

a = 10

a ^= 2

print(a)  # 8

a = 10

a >>= 2

print(a)  # 2

a = 10

a <<= 2

```
