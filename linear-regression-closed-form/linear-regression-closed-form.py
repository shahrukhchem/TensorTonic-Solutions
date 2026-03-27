import numpy as np

def linear_regression_closed_form(X, y):
    """
    Compute the optimal weight vector using the normal equation.
    """
    X=np.array(X)
    y=np.array(y)
    XT=X.T
    xtx=np.matmul(XT,X)
    xtxin=np.linalg.inv(xtx)
    xtxinxt=np.matmul(xtxin,XT)
    ans=np.matmul(xtxinxt,y)
    return ans