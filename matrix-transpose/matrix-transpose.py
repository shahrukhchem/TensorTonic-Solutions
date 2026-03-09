import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    nro=len(A)
    ncol=len(A[0])
    B=np.empty((ncol, nro))
    print(nro,ncol)
    for ro  in range(nro):
        for c in range(ncol):
            B[c][ro]=A[ro][c]
    print(B)   
    return np.array(B)# Write code here
    
