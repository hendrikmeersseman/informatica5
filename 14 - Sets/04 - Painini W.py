def verzamel(speler, stickerboek, dubbels):
    x = len(stickerboek)
    y = len(dubbels)
    spelerdict = {speler}
    stickerboek.add(speler)
    erin = 0
    algedaan = 0

    if len(stickerboek) == x:
        sleutel = 1
        for key, value in dubbels.items():
            if spelerdict.issubset(value) and algedaan != 1:
                sleutel = key

                if value == spelerdict and algedaan != 1:
                    sleutel += key
                    algedaan += 1
                else:
                    erin += 1
        if erin > 1:
            erin = erin/2
        if erin == len(dubbels):
            dubbels[1] = spelerdict
        else:
            dubbels.pop(sleutel - 1)
            dubbels[sleutel] = spelerdict
    return stickerboek, dubbels



print(verzamel('Weber',{'Staelens', 'Bosmans', 'Weber', 'Scifo'},{1: {'Scifo'}, 4: {'Bosmans'}}))