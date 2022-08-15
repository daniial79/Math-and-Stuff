def bisection(f, a, b, tol = 1e-6):
    """
    Bisection algorithm for estimating roots of a function.
    Input:
        f: function
        a: lower bound
        b: upper bound
        tol: tolerance
    Output:
        x: root
    """
    x = (a + b) / 2
    while(f(x) >= tol):
        if(f(a) * f(x) < 0):
            b = x
            x = (a + b) / 2
        else:
            a = x
            x = (a + b) / 2
    return x

func = lambda x: x ** 3 - 2 * (x ** 2) + 2 * x - 1 

print(bisection(func , 0.2, 1.6))
print(func(0.9))