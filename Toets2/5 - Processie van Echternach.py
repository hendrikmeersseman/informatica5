plaats, voor, achter = 0, 2, 1

for i in range(int(input())):
    if i % 2 == 0:
        plaats += voor
        voor += 2
    else:
        plaats -= achter
        achter += 1
print(plaats)

