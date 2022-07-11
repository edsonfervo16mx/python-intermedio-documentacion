# Uso de *args es pasar multiples parametros en una funcion
def my_func_with_argv(f_arg, *argv):
    print('primer argumento normal: ', f_arg)
    for index, item in enumerate(argv):
        print(index)
        print(item)

# Uso de *kwargs es pasar multiples argumentos de tipo clave-valor
def my_func_with_kwargs(**kwargs):
    for key, value in kwargs.items():
        print('{0},{1}'.format(key, value))

# Para usar los 3 tipos de argumentos, se debe de usar en el siguiente orden
def my_func_main(f_arg, *argv, **kwargs):
    print('Primer argumento: ', f_arg)
    for index, item in enumerate(argv):
        print(item)
    for key, value in kwargs.items():
        print('{0},{1}'.format(key, value))

#
print('-'*10)
my_func_with_argv('python', 'javascript', 'php')
#
print('-'*10)
my_func_with_kwargs(country='Argentina', puntos=6500, top=8)
countries = {
    "country": "Mexico",
    "puntos": 9000,
    "top": 4,
}
#
print('-'*10)
kwargs = {"arg3": 3, "arg2": "dos", "arg1": 5}
my_func_main('item0', 'item1', 'item2', kwargs)
