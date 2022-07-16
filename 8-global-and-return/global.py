# uso de una funcion base

def suma(valor1, valor2):
    return valor1 + valor2


resultado = suma(3, 5)
print(resultado)


# uso del global, para crear una variable global dentro del ambito de la funcion

def suma(valor1, valor2):
    global result
    result = valor1 + valor2


suma(7, 9)
print(result)
