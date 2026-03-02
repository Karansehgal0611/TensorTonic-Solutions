import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function that supports:
    - scalars (int/float/np.number) -> returns scalar
    - 1D Python lists -> returns 1D list
    - 2D Python lists (list of lists) -> returns 2D list
    """
    
    if isinstance(x, (int, float, np.number)):
        return 1.0 / (1.0 + np.exp(-x))

    if isinstance(x, list):
        if not x:  
            return []

       
        if isinstance(x[0], list):
            result = []
            for row in x:
                
                result.append([1.0 / (1.0 + np.exp(-val)) for val in row])
            return result

        return [1.0 / (1.0 + np.exp(-val)) for val in x]

    if isinstance(x, np.ndarray):
        return 1.0 / (1.0 + np.exp(-x))

    
    raise TypeError(f"Unsupported type for sigmoid: {type(x)}")