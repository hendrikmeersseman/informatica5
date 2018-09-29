#invoer
sol = float(input('Aantal sol: '))

#Bewerking
tot_sec = float(sol * 88775.244)
dagen = tot_sec // 86400
r = tot_sec % 86400
uren = r // 3600
r %= 3600
minuten = r // 60
r %= 60


#resultaat
print(str(int(sol)), 'sol =', str(int(dagen)), 'dagen,', str(int(uren)), 'uren,', str(int(minuten)), 'minuten en', str(int(r)), 'seconden')
