# filter filtra los elementos de una lista usando un determinado criterio

lista = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

mayor_cero = list(filter(lambda x: x > 0, lista))
print(mayor_cero)
