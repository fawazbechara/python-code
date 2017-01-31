from modulo import modulo

'''
Wenn a < b dann vertausche a und b
solange wie b > 0
berechne q und r mit a = q∗b+r , wobei 0<=r<b
a := b , b := r
Gib den Wert in a zurueck
'''

def ggT_A2(a, b):
    if a < b:
        # Swap variables
        x = b
        b = a
        a = x
    while b > 0:
        r = modulo(a, b)
        a = b
        b = r
    return a
