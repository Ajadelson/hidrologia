def vel(n):
    aux = n/30
    v = 0
    if aux < 0.75:
        v = 0.014481346 + 0.251821558 * aux
    else:
        v = -0.009653654 + 0.283874973 * aux
    return v
