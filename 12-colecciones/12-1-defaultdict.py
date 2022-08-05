from collections import defaultdict

grupos = (
    ('Primero', 'A'),
    ('Segundo', 'A'),
    ('Tercero', 'A'),
    ('Cuarto', 'A'),
    ('Quinto', 'A'),
    ('Sexto', 'A'),
    ('Tercero', 'B'),
)

ciclo = defaultdict(list)

for index, item in grupos:
    ciclo[index].append(item)


print(ciclo)
# Output defaultdict(<class 'list'>, {'Primero': ['A'], 'Segundo': ['A'], 'Tercero': ['A', 'B'], 'Cuarto': ['A'], 'Quinto': ['A'], 'Sexto': ['A']})


# otros ejemplos y detalles del uso de defaultdict
records = [
    ('wh01', 'lt001', 'leased', 5),
    ('wh02', 'lt002', 'leased', 5),
    ('wh03', 'lt003', 'propio', 10),
    ('wh01', 'lt004', 'leased', 5),
    ('wh02', 'lt005', 'leased', 5)
]

data = defaultdict(list)
for warehouse, lote, tipo, cantidad in records:
    data[warehouse].append((lote, tipo, cantidad))
