def volgend_collatz_getal(n):
    if n % 2 == 0:
        getal =  int(n / 2)
    else:
        getal =  int(n * 3 + 1)
    return getal

def collatz(n):
    aantal = 1
    while n != 1:
        n = volgend_collatz_getal(n)
        aantal += 1
    return aantal