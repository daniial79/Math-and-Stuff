def simpsons_method (fx, a, b, n):
    """
    fx: the curve we want to approximate it's net area 
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
    summation += (delta_x / 3) * (fx(xi_points.pop(0)) + fx(xi_points.pop()))
    print(xi_points)
    #body of chain (coefiecients = 2 and 4)
    for j in range(len(xi_points)):
        if(j % 2 == 0):
            summation += (delta_x / 3) * (4 * fx(xi_points[j]))
        else:
            summation += (delta_x / 3) * (2 * fx(xi_points[j]))
    
    return f'net area: {summation}'

func = lambda x: x ** 2

print(simpsons_method(func, 1, 3, 4))