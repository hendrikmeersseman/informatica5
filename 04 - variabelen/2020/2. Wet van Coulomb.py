#gegevens
k,q_1, q_2 = 8.99 * 10**9, 2 * 10**(-6), 10**(-6)

#invoer
r = float(input('geef afstand: ')) * 10**(-2)

#bewerking
f = k * (q_1 * q_2)/ (r**2)

print(f)

