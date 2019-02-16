def ik_heb_gemoord(namen, persoon):
    index = namen.index(persoon)
    if index == len(namen) - 1:
        index = 0
    else:
        index += 1
    if len(namen) > 1:
        namen.pop(index)
    if index == len(namen):
        index = 0

    return namen[index], namen

def ik_ben_vermoord(namen, persoon):
    moordenaar = namen[namen.index(persoon) - 1]

    return ik_heb_gemoord(namen, moordenaar)





print(ik_heb_gemoord(['jan', 'piet', 'joris', 'korneel'],'joris'))

print(ik_heb_gemoord(['jan'],'jan'))

print(ik_ben_vermoord(['jan', 'piet', 'joris'],'joris'))
