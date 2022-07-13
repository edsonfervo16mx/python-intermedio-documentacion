# Contador
def funcion_generadora(x):
    for i in range(x):
        yield i


for item in funcion_generadora(10):
    print(item)

print('*'*10)

# serie fibonacci
def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

for item in fibon(10):
    print(item)

print('*'*10)
# Gestionando generadores
gen = funcion_generadora(5)
print(next(gen))
print(next(gen))
# Genera un Traceback si el generador se sale del rango 