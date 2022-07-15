# Los sets se comportan como las listas, con la diferencia de que no pueden contener elementos duplicados.

lista = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n', 'n', 'n', 'c', 'z']

no_duplicados = set(lista)

duplicados = set([item for item in lista if lista.count(item) > 1])

print(no_duplicados)
print(duplicados)


print('*'*10)

# interseccion

set1 = set(['amarillo', 'rojo', 'azul', 'verde', 'negro'])
set2 = set(['rojo', 'marrón'])


print(set2.intersection(set1))
# Salida: set(['rojo'])

print('*'*10)
# diferencia

print(set2.difference(set1))
# Salida: set(['marrón'])

print(set1.difference(set2))
# Salida: set(['negro', 'amarillo', 'azul', 'verde'])

print('*'*10)

# creando set
set1 = {'red', 'blue', 'green'}
print(type(set1))
# Salida: <type 'set'>