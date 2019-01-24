def ontdubbelen(woord):

    nieuw_woord = ''

    for i in range(0, len(woord)):

        if woord[i] != woord[i - 1]:
            nieuw_woord += woord[i]
    return nieuw_woord


print(ontdubbelen('grootteg'))