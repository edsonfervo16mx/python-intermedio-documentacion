# Uso de *args es pasar multiples parametros en una funcion
def my_func(f_arg, *argv):
    print('primer argumento normal: ', f_arg)
    for index, item in enumerate(argv):
        print(index)
        print(item)

# Uso de *kwargs es pasar multiples argumentos de tipo clave-valor


def my_func2(**kwargs):
    for key, value in kwargs.items():
        print('{0},{1}'.format(key, value))


my_func('python', 'javascript', 'php')
my_func2(country='Argentina', puntos=6500, top=8)
countries = {
    "country": "Mexico",
    "puntos": 9000,
    "top": 4,
}

my_func2(country=countries)
