#invoer
hoeveel = int(input('Hoeveel basen? '))
allebasen = ''
aantal = 0

#berekening
for i in range(hoeveel):
    base = str(input('Geef base: '))
    if base not in allebasen:
        allebasen += base + ' '
        aantal += 1

mv = aantal > 1
mes = 'De DNA-keting bevat ' + str(aantal) + ' verschillende' * mv \
      + ' soort' + 'en' * mv + ' base' +'n' * mv + ': ' +  allebasen
#uitvoer
print(mes)



# if aantal == 1:
#     mes = 'De DNA-keting bevat 1 soort base: ' + allebasen
# else:
#     mes = 'De DNA-keting bevat ' + str(aantal) + ' verschillende soorten basen: ' + allebasen