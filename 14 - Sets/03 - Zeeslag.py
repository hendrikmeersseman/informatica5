def boot_overlappend(nieuwe_boot, bestaand):
    gemeenschappelijk = nieuwe_boot.intersection(bestaand)
    return len(gemeenschappelijk) >= 1

def boot_toevoegen(nieuwe_boot, bestaand):
    if boot_overlappend(nieuwe_boot, bestaand):
        return bestaand
    return bestaand.union(nieuwe_boot)

def vuur(schot, set):
    if schot in set:
        set.discard(schot)
        return True, set
    return False, set


print(boot_toevoegen({'B4', 'A4', 'C4'},{'C4', 'D4', 'E4', 'A2', 'I8', 'F8', 'H8', 'A3', 'G8'}))
print(boot_toevoegen({'F4', 'F5', 'F6', 'F3'},{'C4', 'D4', 'E4', 'A2', 'I8', 'F8', 'H8', 'A3', 'G8'}))
print(boot_overlappend({'B4', 'A4', 'C4'},{'C4', 'D4', 'E4', 'A2', 'I8', 'F8', 'H8', 'A3', 'G8'}))
print(boot_overlappend({'F4', 'F5', 'F6', 'F3'},{'C4', 'D4', 'E4', 'A2', 'I8', 'F8', 'H8', 'A3', 'G8'}))