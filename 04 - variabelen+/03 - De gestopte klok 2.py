vertrek_h = int(input())
vertrek_m = int(input())
aankomst_h = int(input())
aankomst_m = int(input())
vertrek_h2 = int(input())
vertrek_m2 = int(input())
aankomst_h2 = int(input())
aankomst_m2 = int(input())

#totaal berekenen
totaal_u = aankomst_h2 - vertrek_h
if totaal_u < 0:
    totaal_u += 24
totaal_m = aankomst_m2 - vertrek_m
if totaal_m < 0:
    totaal_u -= 1
    totaal_m += 60

#vriendin
vriendin_u = vertrek_h2 - aankomst_h
if vriendin_u < 0:
    vriendin_u += 24
vriendin_m = vertrek_m2 - aankomst_m
if totaal_m < 0:
    totaal_u -= 1
    totaal_m += 60

route_u = (totaal_u - vriendin_u) / 2
route_m = (totaal_m - vriendin_m) / 2




tijd_u = vertrek_h2 + route_u
if tijd_u > 24:
    tijd_u -= 24
tijd_m = vertrek_m2 + route_m
if tijd_u - int(tijd_u) != 0:
    tijd_u = int(tijd_u)
    tijd_m += 30
if tijd_m >= 60:
    tijd_m -= 60
    tijd_u += 1

print(int(tijd_u))
print(int(tijd_m))