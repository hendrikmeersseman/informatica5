woord = str(input('Geef geheim woord: '))
bedrag = int(input('Wat is de prijs? '))
letter = str(input('Geef letter: '))
alleletters = ''

while letter in woord and 'letter' not in alleletters:
    alleletters += letter
    letter = str(input('Geef letter: '))
geld = len(alleletters) * bedrag

print(geld)