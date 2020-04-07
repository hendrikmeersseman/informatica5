import random
def versleutelen(zin, sleutel):
    random.seed(sleutel)
    uitv = ""
    for letter in zin:
        plaats = random.randint(1, 1000000) % 27
        uitv += chr(ord(letter) + plaats)
    return uitv

def ontsleutelen(zin, sleutel):
    random.seed(sleutel)
    uitv = ""
    for letter in zin:
        plaats = random.randint(1, 1000000) % 27
        uitv += chr(ord(letter) - plaats)
    return uitv


print("Wat wilt u doen, versleutelen of onstleutelen? (typ STOP indien u wilt stoppen)")
invoer = str(input())
while invoer != "STOP":
    if invoer == "versleutelen":
        zin = str(input("Geef de zin die u wilt versleutelen: "))
        sleutel = int(input("Geef sleutel die u wil gebruiken: "))
        print(versleutelen(zin, sleutel)  + " || vergeet de ultrageheime sleutel ({}) niet te noteren en geheim te houden!".format(sleutel))
    elif invoer == "ontsleutelen":
        zin = str(input("Geef de zin die u wilt onsleutelens: "))
        sleutel = int(input("Geef sleutel die u wil gebruiken: "))
        print(ontsleutelen(zin, sleutel))
    invoer = str(input("Wat wilt u doen? "))

