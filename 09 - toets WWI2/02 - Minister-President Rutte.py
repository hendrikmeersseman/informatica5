def tel_woorden(zin):

    aantal_spaties = 1

    for letter in zin:
        if letter == ' ':
            aantal_spaties += 1

    return aantal_spaties

def langste_zin(zin):
    test = zin[:zin.find('.')]
    max = tel_woorden(test)
    zin = zin[zin.find('.') + +2:]
    while zin.find('.') != -1:
        test = zin[:zin.find('.')]
        woorden = tel_woorden(test)
        if woorden > max:
            max = woorden
        zin = zin[zin.find('.') + +2:]
    return max



print(langste_zin('Ze weet al welke ze wil.'))
print(langste_zin('De kaaimantaks zou de financiële sluiproutes naar belastingsparadijzen droogleggen. Veel woorden maar weinig daden, lijkt me, afgaand op wat hier is gezegd. Kortom, de belastingparadijzen en het einde van de belastingparadijzen zijn niet aan de orde. Tenzij de regering alsnog orde op zaken stelt. Maar in lopende zaken is dat niet vanzelfsprekend.'))