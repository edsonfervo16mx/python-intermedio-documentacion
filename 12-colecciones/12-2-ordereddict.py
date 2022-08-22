'''
OrderedDict
es un diccionario que mantiene ordenadas sus entradas según van siendo añadidas. Es importante saber también que sobreescribir un valor existente no cambia la posición de la llave o key. Sin embargo, eliminar y reinsertar una entrar mueve la llave al final del diccionario.
'''
from collections import OrderedDict

# ejemplo base
colours = {"Rojo": 198, "Verde": 170, "Azul": 160}
for key, value in colours.items():
    print(key, value)

#
print('*'*10)
colores = OrderedDict([("Rojo", 198), ("Verde", 170), ("Azul", 160)])
for key, value in colores.items():
    print(key, value)
