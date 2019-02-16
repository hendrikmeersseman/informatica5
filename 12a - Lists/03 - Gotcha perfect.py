def ik_heb_gemoord(lijst, moordenaar):
    #slachtoffer schrappen
    index_moordenaar = lijst.index(moordenaar)
    index_slachtoffer = (index_moordenaar + 1) % len(lijst)
    # 0 / 4, rest = 0
    # 1 / 4, rest = 1
    lijst.pop(index_slachtoffer)
    #lijst[index_slachtoffer : index_slachtoffer + 1] = []
    # nieuw doel aan moordenaar geven
    index_moordenaar = lijst.index(moordenaar)
    index_doel = (index_moordenaar + 1) % len(lijst)
    return lijst[index_doel], lijst


print(ik_heb_gemoord(['jan', 'piet', 'joris', 'korneel'],'joris'))
print(ik_heb_gemoord(['jan', 'piet', 'joris', 'korneel'],'korneel'))