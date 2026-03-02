import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    if len(y_pred) != len(y_true):
        return None
    y_p = np.array(y_pred)
    y_t = np.array(y_true)
    return np.mean((y_p - y_t)**2)
    # Write code here
    pass
