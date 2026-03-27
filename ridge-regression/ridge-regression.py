def ridge_regression(X, y, lam):
    """
    Compute ridge regression weights using the closed-form solution.
    """
    X=np.array(X)
    y=np.array(y)
    xt=X.T
    xtx=np.matmul(xt,X)
    lamisize=xtx.shape
    I=np.identity(lamisize[0])
    result = xtx+I * lam
    res=np.linalg.inv(result)
    res2=np.matmul(res,xt)
    res3=np.matmul(res2,y)
    return res3
    