import numpy as np

def calculate(list):
    numb_list = np.array(list)

    if len(numb_list) == 9:

        new_array = numb_list.reshape(3,3)

        promedio = [(np.mean(new_array, axis=0)).tolist(),(np.mean(new_array, axis=1)).tolist(),(np.mean(new_array)).tolist()]
        varianza = [(np.var(new_array, axis=0)).tolist(),(np.var(new_array, axis=1)).tolist(),(np.var(new_array)).tolist()]
        desviacion = [(np.std(new_array, axis=0)).tolist(),(np.std(new_array, axis=1)).tolist(),(np.std(new_array)).tolist()]
        maximo = [(np.max(new_array, axis=0)).tolist(),(np.max(new_array, axis=1)).tolist(),(np.max(new_array)).tolist()]
        minimo = [(np.min(new_array, axis=0)).tolist(),(np.min(new_array, axis=1)).tolist(),(np.min(new_array)).tolist()]
        suma = [(np.sum(new_array, axis=0)).tolist(),(np.sum(new_array, axis=1)).tolist(),(np.sum(new_array)).tolist()]

        calculations = {
            "mean": promedio,
            "variance": varianza,
            "standard deviation": desviacion,
            "max": maximo,
            "min": minimo,
            "sum": suma
        }

        return calculations
    
    else:
        raise ValueError ("List must contain nine numbers.")
