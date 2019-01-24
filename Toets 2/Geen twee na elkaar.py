def ontdubbelen(woord):
    nieuw = woord[0]
    for i in range(1, len(woord)):
        if woord[i] != woord[i-1]:
            nieuw += woord[i]
    return nieuw

print(ontdubbelen('stressstoornissen'))