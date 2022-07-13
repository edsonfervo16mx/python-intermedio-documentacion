# El uso de map aplica una determinada función a todos los elementos de una entrada o lista.
# Forma: map(funcion_a_aplicar, lista_de_entradas)


lista = [1, 2, 3, 4, 5]
nueva_lista = list(map(lambda x: x**2, lista))

print(lista)
print('*'*10)
print(nueva_lista)


# lista de funciones
def multiplicar(x):
    return (x*x)

def sumar(x):
    return (x+x)

print('*'*10)
funcs = [multiplicar, sumar]
for i in range(5):
    valor = list(map(lambda x: x(i), funcs))
    print(valor)