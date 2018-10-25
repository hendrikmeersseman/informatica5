#invoer
a1 = int(input('a1: '))
a2 = int(input('a2: '))
a3 = int(input('a3: '))
v1 = int(input('a1: '))
v2 = int(input('a2: '))

#sorteren
sa1 = max(a1, a2, a3)
sa2 = a1 + a2 + a3 - sa1 - min(a1, a2, a3)

sv1 = max(v1,v2)
sv2 = min(v1,v2)
#winnaar bepalen
if sa1 > sv1 and sa2 > sv2:
    mes = 'annvaller verliest 0 legers, verdediger verliest 2 legers'
elif sa1 <= sv1 and sa2 <= sv2:
    mes = 'annvaller verliest 2 legers, verdediger verliest 0 legers'
else:
    mes = 'annvaller verliest 1 leger, verdediger verliest 1 leger'

#uitvoer
print(mes)