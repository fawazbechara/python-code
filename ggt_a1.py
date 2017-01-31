def ggT_A1(a, b):
    while a != b:
        if a > b:
            a -= b
        # Falls b groesser als a
        else:
            b -= a
    return a
