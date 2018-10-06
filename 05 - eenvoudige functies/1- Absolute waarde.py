#invoeren waarden
x = float(input('x: '))
y = float(input('y: '))

#bewerkingen
ll = abs(abs(x) - abs(y))
rl = abs(x - y)

#uitvoer
print('{:.4f} ≤ {:.4f}'.format(ll, rl))
