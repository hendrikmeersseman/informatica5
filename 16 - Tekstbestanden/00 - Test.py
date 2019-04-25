#bestand = open('klas.txt')
#
#lijn = bestand.readline()
#
#while lijn != '':
#   print(lijn)
#    lijn = bestand.readline()
#
#heel goed idee om op tijd bestand te sluiten (zeker bij grotere bestanden!
#bestand is gewoon naam ven een variabele, ook mogelijk:"file,..."
#bestand.close()
###########################################################################
# lijnen = []
#
# with open('klas.txt') as bestand:
#     lijnen = bestand.readlines()
#
# for naam in lijnen:
#     print(naam[:-1])
#
# print('er zitten ' + str(len(lijnen)) + ' personen in de klas')

nieuwe_leerlingen = ['Alice', 'Baptiste']

with open('klas.txt', 'w') as bestand:
    bestand.writelines(nieuwe_leerlingen)
    #bestand.write('\n' + '\n'.join(nieuwe_leerlingen))