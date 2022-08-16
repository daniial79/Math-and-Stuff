def trapezoidal_method(fx, a, b, n):
    """
    fx: the curve we want to approximate the net area below it
    a: starting point of interval
    b: ending point of interval
    n: quantity of trapezoids
    """
    #generating delta x
    delta_x = (b - a) / n

    #generating xi points
    xi_points = []
    i = a - delta_x
    while (i < b):
        i += delta_x
        xi_points.append(i)
    print(xi_points)
    #calculating summation in two independent steps
    summation = 0
    
    #head and tail
    summation += (delta_x / 2) * (fx(xi_points.pop(0)) + fx(xi_points.pop()))
    print(xi_points)
    #body of chain (coefiecients = 2)
    for j in xi_points:
        summation += (delta_x / 2) * (2 * fx(j))

    return f'net area: {summation}'

func = lambda x: x
print(trapezoidal_method(func, 0, 5, 5))