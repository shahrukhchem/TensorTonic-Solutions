import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    if sum(p)!=1:
        raise ValueError
    expprob=0
    for u, v in zip(x, p):
         expprob+=u*v
        
        
    # Write code here
    return  expprob
