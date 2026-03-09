def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    def funcatx(x,a,b,c):
        return a*(x**2)+b*x+c
    def gradientatxold(xold):
        h=0.0001
        gradient=(funcatx(xold+h,a,b,c)-funcatx(xold,a,b,c))/h
        return gradient
        
    # Write code here
    xold=x0
    for i in range(steps):
        xne=xold-gradientatxold(xold)*lr
        xold=xne
    return xne