# Importar un módulo

import math

# Utilizar una función del módulo

print(math.sqrt(16))  # 4.0

# Importar un módulo con un alias

import math as m

# Utilizar una función del módulo con el alias

print(m.sqrt(16))  # 4.0

# Importar una función específica de un módulo

from math import sqrt

# Utilizar la función importada

print(sqrt(16))  # 4.0

# Importar varias funciones de un módulo

from math import sqrt, pow

# Utilizar las funciones importadas

print(sqrt(16))  # 4.0

print(pow(2, 3))  # 8.0

# Importar todas las funciones de un módulo

from math import *

# Utilizar las funciones importadas

print(sqrt(16))  # 4.0

print(pow(2, 3))  # 8.0

# Importar un módulo de un paquete

import numpy.linalg

# Utilizar una función del módulo importado

print(numpy.linalg.det([[1, 2], [3, 4]]))  # -2.0

# Importar un módulo de un paquete con un alias

import numpy.linalg as npl

# Utilizar una función del módulo importado con el alias

print(npl.det([[1, 2], [3, 4]]))  # -2.0
