# La mutabilidad significa que pueden cambiarse los valores
foo = ['hola']
print(foo)
# Output: ['hola']


bar = foo
bar += ['adios']
print(foo)
# Output: ['hola', 'adios']

'''
Evidentemente no se trata de un fallo, sino que lo que estamos viendo es la mutabilidad en acción. Cuando asignas una variable a otra variable que es de tipo mutable, cualquier cambio que hagas sobre la segunda, afectará a la primera y viceversa. 
'''


# Otro ejemplo de mutabilidad
def agrega(num, target=[]):
    target.append(num)
    return target


print(agrega(1))
# Salida: [1]
print(agrega(2))
# Salida: [1, 2]
print(agrega(3))
# Salida: [1, 2, 3]


'''
Tal vez te esperabas otro comportamiento, ya que en cada llamada a agrega estamos creando una lista nueva vacía. 
'''

'''
Otra vez, estamos viendo la mutabilidad en acción. En Python, los "argumentos" por defecto se evalúan una vez que la función ha sido definida, no cada vez que la función es llamada
'''

# Por lo tanto si se requiere que target inicie vacio, se tiene que validar


def add(element, target=None):
    if target is None:
        target = []  # se define dentro del bloque y no como argumento
    target.append(element)
    return target


print(add(1))
print(add(2))
print(add(3))
