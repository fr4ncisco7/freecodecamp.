from statistics import variance
import numpy

def calculate(list):
    if len(list) != 9:
          raise ValueError("List must contain nine numbers.")
    list = numpy.array(list)
    list = list.reshape(3, 3)

    dicionario = {
        'mean': [numpy.mean(list, axis=0).tolist(),
        numpy.mean(list, axis=1).tolist(),
        numpy.mean(list).tolist()] ,

        'variance': [numpy.var(list, axis=0).tolist(),
        numpy.var(list, axis=1).tolist(),
        numpy.var(list).tolist()],

        'standard deviation': [numpy.std(list, axis=0).tolist(), 
                               numpy.std(list, axis=1).tolist(),
                               numpy.std(list).tolist()],

        'max': [numpy.max(list, axis=0).tolist(),
        numpy.max(list, axis=1).tolist(),
        numpy.max(list).tolist()],

        'min': [numpy.min(list, axis=0).tolist(),
        numpy.min(list, axis=1).tolist(),
        numpy.min(list).tolist()],

        'sum': [numpy.sum(list, axis=0).tolist(),
        numpy.sum(list, axis=1).tolist(),
        numpy.sum(list).tolist()]
    
    }

    return dicionario
        
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8]
resultado = calculate(lista)
for c, i in resultado.items():
        print(f'{c}: {i}')
