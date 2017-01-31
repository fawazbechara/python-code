def eratosthenes(n):
    prims = list(range(2, n + 1))
    for i in range(2, n):
        for k in range(2, n):
            prod = i * k
            if prod in prims:
                prims.remove(prod)
    return prims
