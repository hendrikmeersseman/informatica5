tjirps = int(input('Geef aantal tjirps per minuut: '))

temperatuur_F = 50 + ((tjirps - 40) / 4)
temperatuur_C = 10 + ((tjirps - 40) / 7)

print('temperature (Fahrenheit): ' + str(temperatuur_F))
print('temperature (Celsius): ' + str(temperatuur_C))