# reduce es muy útil cuando queremos realizar ciertas operaciones sobre una lista y devolver su resultado

from functools import reduce


lista = [1, 2, 3, 4]

producto = reduce((lambda x, y : x *y), lista)

print(producto)

print('*'*10)

resultado = reduce((lambda x, y: x + y), lista)

print(resultado)