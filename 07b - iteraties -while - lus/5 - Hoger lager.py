from random import random, randint, seed
seed(1)
teraden = randint(1,100)
geraden = randint(1,100)
if geraden < teraden:
    lg, gg = geraden, 100
else:
    lg, gg = 1, geraden
aantal = 0
print(teraden, geraden)
while teraden != geraden:
    geraden = randint(lg, gg)
    if geraden < teraden:
        lg = geraden
    else:
        gg = geraden
    geraden = randint(lg, gg)
    print(geraden)
    print(lg,gg)
    aantal += 1
print('computer had', aantal, 'pogingen nodig om het getal', teraden, 'te raden.')
