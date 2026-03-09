import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    x=np.array(x)
    shp=x.shape
    onearr=np.ones(shp)
    den=np.add(onearr, np.exp(-1*x)) 
    
    return 1/den