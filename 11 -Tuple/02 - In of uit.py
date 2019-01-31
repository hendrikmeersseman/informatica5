from math import sqrt

def binnen_of_buiten(M, c, p):
    #straal berekenen: d(m,c)
    r = sqrt(pow(M[0] - c[0], 2) + pow(M[1] - c[1], 2))
    #afstand (M,p)
    afstand = sqrt(pow(M[0] - p[0], 2) + pow(M[1] - p[1], 2))

    #if afstand == r
    if afstand == r:
        mes = 'op'
    elif afstand < r:
        mes = 'binnen'
    else:
        mes = 'buiten'
    return mes, round(afstand, 4)
