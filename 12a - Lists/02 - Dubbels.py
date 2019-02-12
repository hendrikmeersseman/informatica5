def dubbels(lijst):
    nieuwe = []
    for item in lijst:
        if lijst.count(item) > 1 and item not in nieuwe:
            nieuwe.append(item)
    return nieuwe




print(dubbels([1,2,1]))
print(dubbels([(0, 1), 'joris', 4, 'korneel', (1, -1), 1, 1, 'piet', 4, 'joris']))

