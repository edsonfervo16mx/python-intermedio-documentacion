'''
Los enumerados permite asignar indices a elementos
'''

# Enumerate nos permite indicar el primer elemento del indice

mi_lista = ['Antonio', 'Oscar', 'Pedro', 'Juan', 'Carlos']
for indice, valor in enumerate(mi_lista, 5):
    print(indice, valor)


'''
5 Antonio
6 Oscar
7 Pedro
8 Juan
9 Carlos
'''

# Otro ejemplo
print('--------------')
mi_listado = ['Ibias', 'Pesoz', 'Tineo', 'Boal']
lista_contador = list(enumerate(mi_listado, 1))
print(lista_contador)
# Salida: [(1, 'Ibias'), (2, 'Pesoz'), (3, 'Tineo'), (4, 'Boal')]
