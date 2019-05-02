def behoort_tot_taal(tekst, taal):
    lijst = set(tekst)
    lijst.discard(' ')
    return lijst.issubset(taal) and lijst != set()

def is_onleesbaar(tekst, taal):
    lijst = set(tekst)
    lijst.discard(' ')
    if len(taal.difference(lijst)) < len(lijst):
        return False
    return True

def perfect_woord(tekst, taal):
    lijst = set(tekst)
    lijst.discard(' ')
    if lijst == set():
        return False
    return taal.issubset(lijst)



print(behoort_tot_taal('do well',{'o', 'd', 'e', 'l', 'w', 'r', 'h'}))
print(behoort_tot_taal('ambigu',{'o', 'd', 'e', 'l', 'w', 'r', 'h'}))
print(perfect_woord('do well',{'o', 'd', 'e', 'l', 'w', 'r', 'h'}))

