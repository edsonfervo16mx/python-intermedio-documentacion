# Los operadores ternarios son más conocidos en Python como expresiones condicionales.
# Estos operadores evalúan si una expresión es verdadera o no.

# condition_if_true if condition else condition_if_false


es_bonito = True
estado = "Es bonito" if es_bonito else "No es bonito"

print(estado)


print('*'*10)
# otra forma
# (if_test_is_false, if_test_is_true)[test]

estado = True
motor = ('Apagado', 'Encendido')[estado]
print(motor)

print('*'*10)

# Otro ejemplo 

acceso = True
validar = 1 if acceso else 0
print(validar)

print('*'*10)

# Otro ejemplo 

texto = None
msg = texto or 'No disponible'
print(msg)