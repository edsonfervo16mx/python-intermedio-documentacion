# Los decoradores son funciones que modifican la funcionalidad de otras funciones.

# Usando funciones como objetos

from datetime import datetime


def my_func(text=''):
    return 'Hola ' + text


saludo = my_func()

print(saludo)

otro_saludo = my_func(text='Hector')
print(otro_saludo)

print('*'*10)
# definiendo funciones dentro de funciones


def conversacion():
    print('Estas en una conversacion')

    def saludo():
        return 'Hola, estoy saludando'

    def despedida():
        return 'Bye, nos vemos luego'

    print(saludo())
    print(despedida())
    print('esto fue una coversacion')


conversacion()

print('*'*10)
# devolviendo funciones desde funciones


def enviar_correo(nombre=''):

    def bienvenido(nombre):
        return 'Hola mucho gusto ' + nombre + ', esperemos que disfrutes nuestro servicio'

    def saludo():
        return 'Gracias por registrarte, esperemos que disfrutes nuestro servicio'

    if nombre:
        return bienvenido
    else:
        return saludo


envio = enviar_correo()
print(envio())


print('*'*10)
# usando funciones como argumento


def hola():
    return 'Hola'


def hazEstoAntesDeHola(func):
    print('Hacer algo antes de llamar a func')
    print(func())


hazEstoAntesDeHola(hola)


print('*'*10)

# tu primer decorador
# Un decorador recibe como parametro una funcion, y requiere de ser ejecutada dentro de una funcion


def my_decorador(func):
    def my_funcion_de_envoltura():
        print('Mi funcion de envoltura')
        func()
    return my_funcion_de_envoltura


@my_decorador
def mostrar():
    print('Mostrando mensaje en pantalla')


mostrar()

print('*'*10)

# decorador con argumentos


def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print('Pasaron' + str(time_elapsed.total_seconds()) + 'segundos')
    return wrapper


@execution_time
def my_demo_func():
    for item in range(1, 100):
        print(item)


my_demo_func()
