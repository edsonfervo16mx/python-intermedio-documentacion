from collections import namedtuple
from enum import Enum


class Especies(Enum):
    gato = 1
    perro = 2
    caballo = 3
    lobo = 4
    mariposa = 5
    buho = 6


print(Especies.gato)
# Especies.gato
print(repr(Especies.gato))
# <Especies.gato: 1>
print(type(Especies.gato))
# <enum 'Especies'>
print(Especies.gato.name)
# gato
print(Especies.gato.value)
# 1
print(Especies(1))
# Especies.gato
print(Especies['gato'])
# Especies.gato
