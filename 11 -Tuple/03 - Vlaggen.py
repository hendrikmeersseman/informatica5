def vlag(richtin, kleuren):
    if richtin == 'verticaal':
        mes = kleuren[0]
        for i in range(1, len(kleuren)):
            mes += ' | ' + kleuren[i]
    else:
        mes = kleuren[0]
        for i in range(1, len(kleuren)):
            mes += '\n-' + '\n' + kleuren[i]
    return mes