aantal = int(input('Hoeveel gevangenen zijn dood? '))
totaal = 0
for i in range(aantal):
    letter = ord(str(input('Geef letter: ')))
    nummer = letter - 65
    totaal += 2 ** nummer

print('Fles #' + str(totaal) + ' is vergiftigd.')
