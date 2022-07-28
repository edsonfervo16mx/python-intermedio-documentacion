# Clase sin el uso de __slots__

class MiClase(object):
    def __init__(self, nombre, identificador):
        self.nombre = nombre
        self.indentificador = identificador
        # self.iniciar()

# Clase con el uso de __slots___


class MyClass(object):
    __slots__ = ['nombre', 'identificador']

    def __init__(self, nombre, identificador):
        self.nombre = nombre
        self.identificador = identificador
        # self.iniciar()


'''
El segundo código reducirá el uso de RAM. En alguna ocasiones se han reportado reducciones de hasta un 40 o 50% usando esta técnica.
Ya que el slot reserva el espacio justo de memoria para su procesamiento
'''
