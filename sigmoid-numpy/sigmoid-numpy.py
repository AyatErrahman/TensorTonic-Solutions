import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    x = np.array(x, dtype=float)
    # Write code here
    return 1/(1+ np.exp(-x))