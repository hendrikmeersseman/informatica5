def doe_maar_gewoon(woord):
    nieuw_woord = ''
    for i in range(len(woord) - 1):
        if woord[i].lower() == woord[i + 1]:
            nieuw_woord += woord[i].lower()
        else:
            nieuw_woord += woord[i]
    nieuw_woord += woord[-1]
    return  nieuw_woord
print(doe_maar_gewoon('stresSsymptOom'))