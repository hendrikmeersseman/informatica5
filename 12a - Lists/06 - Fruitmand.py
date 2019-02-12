def fruitstuk_toevoegen(fruit_in_mand, fruit):
    index = 0
    alreeds = 0
    while fruit_in_mand[index] != fruit and index < len(fruit_in_mand) - 1:
        index += 1
    if fruit_in_mand[index] == fruit:
        alreeds = 1
    if not alreeds:
        for element in fruit_in_mand:
            if len(element) == len(fruit):
                fruit_in_mand.remove(element)
                fruit_in_mand.append(fruit)
                alreeds = 1
    if not alreeds:
        fruit_in_mand.append(fruit)
    fruit_in_mand.sort(key=lambda s: len(s))
    return fruit_in_mand

def maak_fruitmand(lijst):
    uitv = lijst[0].split()
    for element in lijst:
        uitv = fruitstuk_toevoegen(uitv, element)
    return uitv

#############################################################
print(fruitstuk_toevoegen(['kiwi'],'peer'))
print(fruitstuk_toevoegen(['bes', 'peer', 'framboos', 'sinaasappel'],'appel'))

print(maak_fruitmand(['kiwi', 'peer', 'kiwi', 'peer', 'kiwi']))