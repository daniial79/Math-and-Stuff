def reiman_sum(fx, a, b, n, approach):
    """
    simple algorithm to approximate the area under the curve fx in [a, b] interval
    fx: curve
    a: starting point of interval
    b: ending point of interval
    n: quantity of subintervals (rectangles)
    approach: one on left-endpoint, right-endpoint or midpoint approachs should be selected
    (attention: you have to put r, l or m as approach's value or you will get an error) 
    """
    
    #calculating width of rectangles
    delta_x = (b - a) / n

    #generating subinterval points
    i = a + delta_x
    raw_points_holder = [float(a)]
    while(i <= b):
        raw_points_holder.append(i)
        i += delta_x
    
    #generating xi base on approach
    xi_points = []
    if(approach == 'r' or approach == 'R'):
        raw_points_holder.pop(0)
        xi_points = raw_points_holder.copy()
    elif(approach == 'l' or approach == 'L'):
        raw_points_holder.pop()
        xi_points = raw_points_holder.copy()
    elif(approach == 'm' or approach == 'M'):
        j = 0
        while(j + 1 < len(raw_points_holder)):
            xi_points.append((raw_points_holder[j] + raw_points_holder[j + 1]) / 2)
            j += 1
    else:
        raise Exception('approach argument must be one of r, l or m charachters!!!')

    #calculating the final value
    summation = 0
    for xi in xi_points:
        summation += delta_x * fx(xi)

    return f'net area: {summation}'


func = lambda x: 3 * ((0.85) ** x)
result = reiman_sum(func, 0, 10, 5, 'l')
print(result)