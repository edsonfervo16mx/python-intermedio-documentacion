from collections import Counter

colours = (
    ('Covadonga', 'Amarillo'),
    ('Pelayo', 'Azul'),
    ('Xavier', 'Verde'),
    ('Pelayo', 'Negro'),
    ('Covadonga', 'Rojo'),
    ('Amaya', 'Plata'),
)

favs = Counter(name for name, colour in colours)
print(favs)
# Salida: Counter({
#    'Covadonga': 2,
#    'Pelayo': 2,
#    'Xavier': 1,
#    'Amaya': 1
# })


# Contar las lineas mas comunes de un fichero

f = open('datos.txt', 'rb')
line_count = Counter(f)
print(line_count)
