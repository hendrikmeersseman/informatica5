#invoer
codon = str(input('geef codon: '))

#berekening
if 'AUG' in codon:
    soort_codon = 'start'
elif 'UAG' in codon or 'UGA' in codon or 'UAA' in codon:
    soort_codon = 'stop'
elif len(codon) == 3:
    soort_codon = 'gewoon'
else:
    soort_codon = 'ongeldig'

#uitvoer
print('Het codon', codon, 'is een', soort_codon, 'codon.')