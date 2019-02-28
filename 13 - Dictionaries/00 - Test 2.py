



#########################################################################
cirkel = {'middelpunt': [0,0], 'straal': 5}
print(cirkel)

cirkel['middelpunt'][0] = 1
print(cirkel)


for k,v in cirkel.items():
    print(k, v)


#########################################################################
klas = {1: 'arnout', 2: 'thibault', 6: 'Hendrik', 'titularis': 'Mr. Van Der Cruyssen'}

for k,v in klas.items():
    print(k,v)

#########################################################################
fruitmand = {'kiwi': 3, 'bes': 12, 'peer': 5}

for k, v in fruitmand.items():
    print('ik heb ' + str(v) + ' ' + k)
for v in fruitmand.values():
    print(v)

for k in fruitmand.keys():
    print(k)

for fruit in fruitmand:
    print(fruit)