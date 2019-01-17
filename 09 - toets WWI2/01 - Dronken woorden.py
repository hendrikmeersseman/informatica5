def dronken_voeren(woord):
    nieuw = woord[0]
    for i in range(1, len(woord)):
        if i % 2 == 0:
            nieuw += woord[i].upper()
        elif nieuw[-1] in 'AEIOU':
            nieuw += woord[i].upper()
        else:
            nieuw += woord[i].lower()

    return nieuw


print(dronken_voeren('Alcoholist'))