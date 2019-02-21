def beweeg(invoer, richting):
    invoer = list(invoer)
    if richting == '<':
        invoer[0] -= 1
    elif richting == '>':
        invoer[0] += 1
    elif richting == '^':
        invoer[1] += 1
    elif richting == 'v':
        invoer[1] -= 1
    return tuple(invoer)

def teruggekeerd(bewegingen):
    bewegingen.sort()
    return (bewegingen[0] == '^' and bewegingen[1] == 'v') or (bewegingen[0] == '<' and bewegingen[1] == '>')

def laatste_levende_positie(lijst):
    nieuw, index = beweeg((0, 0), lijst[0]), 1
    while index < len(lijst) and not teruggekeerd(lijst[(index - 1):index + 1]):
        nieuw = beweeg(nieuw, lijst[index])
        index += 1
    x, y = nieuw
    return index, x, y

###################################################################################################################
print(beweeg((7, 3), '^'))
print(teruggekeerd(['^', 'v']))
print(teruggekeerd(['>', '<']))
print(laatste_levende_positie(['v', '>', 'v', '<', '^', '^']))
print(laatste_levende_positie(['^', 'v']))