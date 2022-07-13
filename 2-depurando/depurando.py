# python -m pbd depurando.py
import pdb

def run(a):
    print('Start loop')
    pdb.set_trace()
    print('*'*10)
    for item in range(0,int(a)):
        print("inicio")
        pdb.set_trace()
        print(item)
        print('final')
    print('*'*10)
    breakpoint() # 3.7+
    print('Success')



if __name__ == '__main__':
	run(5)

# pdb.set_trace() or breakpoint() en python 3.7+
'''
c -> continúa la ejecución
w -> muestra el contexto de la línea que se esta ejecutando
a -> imprime la lista de argumentos para la función actual
s -> ejecuta la primera línea y para en cuanto sea posible
n -> continúa la ejecución hasta la siguiente línea en la función actual o hasta que se retorna
'''
