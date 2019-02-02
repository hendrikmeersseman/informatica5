tijd_vertrek_h = int(input('Geef uur van vertrek: '))
tijd_vertrek_m = int(input('Geef minuut van vertrek: '))
tijd_aankomst_h = int(input('Geef uur van aankomst: '))
tijd_aankomst_m = int(input('Geef minuut van aankomst: '))
tijd_vertrek2_h = int(input('Geef uur van vertrek2: '))
tijd_vertrek2_m = int(input('Geef minuut van vertrek2: '))
tijd_aankomst2_h = int(input('Geef uur van aankomst2: '))
tijd_aankomst2_m = int(input('Geef minuut van aankomst2: '))

# tijd berekenen bij vriendin

tijd_bij_vriendin_h = tijd_vertrek2_h - tijd_aankomst_h
if tijd_bij_vriendin_h < 0:
    tijd_bij_vriendin_h += 24
tijd_bij_vriendin_m = tijd_vertrek2_m - tijd_aankomst_m
if tijd_bij_vriendin_m < 0:
    tijd_bij_vriendin_m += 60
    tijd_bij_vriendin_h += 1
#tijd volledige trip berekenen

tot_tijd_h = tijd_aankomst2_h - tijd_vertrek_h
if tot_tijd_h < 0:
    tot_tijd_h += 24
tot_tijd_m = tijd_aankomst2_m - tijd_vertrek_m
if tot_tijd_m < 0:
    tot_tijd_m += 60
    tot_tijd_h += 1
#tijd 1 reis

reis_h = (tot_tijd_h - tijd_bij_vriendin_h) / 2
if reis_h < 0:
    reis_h += 24
reis_m = (tot_tijd_m - tijd_bij_vriendin_m) / 2
if reis_m < 0:
    reis_m += 60
    reis_h += 1

# juiste tijd berekenen

juiste_tijd_h = tijd_vertrek2_h + reis_h
if juiste_tijd_h > 24:
    juiste_tijd_h -= 24
juiste_tijd_m = tijd_vertrek2_m + reis_m
if juiste_tijd_m > 60:
    juiste_tijd_m -= 60
#uitvoer

print(int(juiste_tijd_h))
print(int(juiste_tijd_m))
