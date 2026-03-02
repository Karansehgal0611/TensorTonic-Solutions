def exponential_moving_average(values, alpha):
    """
    Compute the exponential moving average of the given values.
    """
    n = len(values)
    prev = values[0]
    result = []
    result.append(prev)

    for i in range(1,n):
        current = alpha * values[i] + (1 - alpha) * prev
        result.append(current)
        prev = current

    return result
        
    # Write code here