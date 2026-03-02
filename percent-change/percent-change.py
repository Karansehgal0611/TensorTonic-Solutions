def percent_change(series):
    """
    Compute the fractional change between consecutive values.
    """
    n = len(series)
    if n < 2:
        return None

    result = []
    for i in range(n-1):
        if series[i] == 0 :
            result.append(0.0)
            continue
        next = (series [i+1] - series[i]) / series[i]
        result.append(next)

    return result
        
