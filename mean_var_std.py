import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')
    
    matriz = np.array(list).reshape(3,3)

    calculations = {
        'mean': [np.mean(matriz, axis=0).tolist(), np.mean(matriz, axis=1).tolist(), np.mean(matriz).item()],
        'variance': [np.var(matriz, axis=0).tolist(), np.var(matriz, axis=1).tolist(), np.var(matriz).item()],
        'standard deviation': [np.std(matriz, axis=0).tolist(), np.std(matriz, axis=1).tolist(), np.std(matriz).item()],
        'max': [np.max(matriz, axis=0).tolist(), np.max(matriz, axis=1).tolist(), np.max(matriz).item()],
        'min': [np.min(matriz, axis=0).tolist(), np.min(matriz, axis=1).tolist(), np.min(matriz).item()],
        'sum': [np.sum(matriz, axis=0).tolist(), np.sum(matriz, axis=1).tolist(), np.sum(matriz).item()]
    }
    
    return calculations
    