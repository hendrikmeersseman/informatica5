#invoer
a = int(input('geef a: '))
b = int(input('geef b: '))
#exponent
e = 0

#berekening
som_1 = (a + b) * pow(10, e)
e += 1
som_2 = (a + b) * pow(10, e)
e += 1
som_3 = (a + b) * pow(10, e)
e += 1
som_4 = (a + b) * pow(10, e)
e += 1
som_5 = (a + b) * pow(10, e)
e += 1

#uitvoer
print('{:6d} + {:<6d} = {:<6d}'.format(a, b, som_1))
a *= 10
b *= 10
print('{:6d} + {:<6d} = {:<6d}'.format(a, b, som_2))
a *= 10
b *= 10
print('{:6d} + {:<6d} = {:<6d}'.format(a, b, som_3))
a *= 10
b *= 10
print('{:6d} + {:<6d} = {:<6d}'.format(a, b, som_4))
a *= 10
b *= 10
print('{:6d} + {:<6d} = {:<6d}'.format(a, b, som_5))