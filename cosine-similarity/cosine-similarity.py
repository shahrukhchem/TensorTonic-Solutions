import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
   
    firstarray=np.array(a)
    secarray=np.array(b)
    if  np.all(firstarray == 0) or np.all(secarray == 0):
        return 0
    first_arr_square= np.square(firstarray)
    sec_arr_square=np.square(secarray)
    first_arr_mag=np.sqrt( np.sum(first_arr_square))
    first_arr_mag=np.sqrt( np.sum(first_arr_square))
    sec_arr_mag=np.sqrt(np.sum(sec_arr_square))
    res=np.sum(firstarray*secarray)
    res=res/first_arr_mag
    res=res/sec_arr_mag
    return res
    # Write code here
   