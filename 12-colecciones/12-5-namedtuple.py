'''
Las namedtuple es un tipo que convierte las tuplas en contenedores bastantes utiles para tareas simples
'''
from collections import namedtuple

persona = ("Juan", "Perez")
print(persona)

# Error por que no se permite reasignar valores a una tupla
# persona[0] = "Maria"
# print(persona)


########
# namedtuple es ligero para la creacion de objetos
Objecto = namedtuple("Animal", "nombre edad tipo")
perro = Objecto(nombre="Firulais", edad=4, tipo="Bull Dog")
print(Objecto)
print(perro)
print(perro.nombre)
print(perro.edad)
print(perro.tipo)

#########
# se permite el acceso por indice
print("-----")
print(perro[0])
print(perro[1])
print(perro[2])

#########
# Convertir namedtuple en diccionario
print("-----")
print(perro._asdict())
# {'nombre': 'Firulais', 'edad': 4, 'tipo': 'Bull Dog'}
