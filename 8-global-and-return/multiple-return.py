# use global en multiple return

from collections import namedtuple
from paramiko import Agent


def perfil():
    global nombre
    global edad
    nombre = 'Fernando'
    edad = 30


perfil()
print(nombre)
print(edad)


print('*'*10)
# multiple return


def profile():
    name = 'Edson'
    age = 31
    return name, age


datos = profile()
print(datos)


print('*'*10)

# multiple return con namedtuple para returnar un objeto


def vehiculo():
    Auto = namedtuple('Auto', ['name', 'modelo'])
    return Auto(name="Pelayo", modelo=1970)


car = vehiculo()
print(car.name)
print(car.modelo)
