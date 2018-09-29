# invoeren in centen
x = float(input('aantal eurocent : ') )

# berekening (kon ook met r)
d_100 = x // 100
r_100 = x % 100
d_50 = r_100 // 50
r_50 = r_100 % 50
d_20 = r_50 // 20
r_20 = r_50 % 20
d_10 = r_20 // 10
r_10 = r_20 % 10
d_5 = r_10 // 5
r_5 = r_10 % 5
d_2 = r_5 // 2
r_2 = r_5 % 2
d_1 = r_2 // 1

#aantal muntstukken berekenen
aantal_muntstukken = int(d_100 + d_50 + d_20 + d_10 + d_5 + d_2 + d_1)
print(str(int(x)), 'cent kan je omwisselen in ' + str(aantal_muntstukken), 'muntstukken')