import math


def find_x(f, a, b):
    """
    Take lower bound and upper bound and caluclate the x
    Input:
        a: lowe bound
        b: upper bound
        f: function
    Output:
        x: root
    """
    return (a * f(b) - b * f(a)) / (f(b) - f(a))

def false_position(f, a, b, tol = 1e-6):
    """
        False position algorithm for estimating root of a function.
    Input:
        f: function
        a: lower bound
        b: upper bound
        tol: tolerance
    Output:
        x: root
    """
    x = find_x(f, a, b)
    while(abs(x - math.sqrt(2)) >= 1e-2):
        if(f(a) * f(x) < 0):
            b = x
            x = find_x(f, a, b)
        else:
            a = x
            x = find_x(f, a, b)
    
    return x
    
func = lambda x: x ** 2 - 2

print(false_position(func, 1, 1.75))
    