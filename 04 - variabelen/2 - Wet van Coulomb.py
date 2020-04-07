q1 = 2.0 * (10 ** -6)
q2 = 1.0 * (10 ** -6)
k0 = 8.99 * (10 ** 9)

# invoer
r = float(input('geef afstand(in cm): '))

#bewerking

fc = k0 * (q1 * q2) / ((r * 10 ** -2) ** 2)
print(fc)