def geldige_zet(zet):
    if 2 <= len(zet) <= 3 and max(zet) in 'abcdefgh' and min(zet) in '12345678':
        if len(zet) == 2 and max(zet) == zet[0]:
            return True
        elif zet[0] in 'KDTLP':
            return True
    return False

def geldige_zetten(zetten):
    for i in range(len(zetten)):
        if not geldige_zet(zetten[i]):
            return False
    return True







print(geldige_zetten(('f8', 'XZJM', 'Pa3', 'Pf3')))
print(geldige_zetten(('Ta1', 'e5', 'h8', 'f7', 'Db7', 'Lg3')))