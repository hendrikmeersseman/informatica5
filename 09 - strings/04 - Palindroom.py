def is_palindroom(woord):
    for i in range(len(woord)):
        if woord[i] != woord[-(i + 1)]:
            return False
    return True
