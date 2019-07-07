from time import time
from random import randint
import matplotlib.pyplot as plt


def genereer_rij(aantal):
    rij_1 = []
    for i in range(aantal):
        rij_1.append(randint(0, aantal))
    return rij_1


def insertion_sort(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            i = i - 1
        a[i + 1] = key
    return a

i, n, t_insertion, t_python, t_bubble = 10, [], [], [], []


def bubbel_sort(rij):
    for i in range(0, len(rij) - 1):
        for j in range(len(rij) - 1, i, -1):
            if rij[j] < rij[j - 1]:
                rij[j], rij[j - 1] = rij[j - 1], rij[j]
    return rij



while i < 2000:
    rij_1 = genereer_rij(i)
    rij_2 = rij_1.copy()
    rij_3 = rij_1.copy()
    # insertion sort testen
    start = time()
    rij = insertion_sort(rij_1)
    stop = time()
    t_insertion.append(stop - start)

    # Sorteerfunctie van python testen
    start = time()
    rij_2.sort()
    stop = time()
    t_python.append(stop - start)

    # bubble sort testen
    start = time()
    bubbel_sort(rij_3)
    stop = time()
    t_bubble.append(stop - start)

    n.append(i)
    i += 50

plt.plot(n, t_insertion)
plt.plot(n, t_python)
plt.plot(n, t_bubble)
plt.xlabel('N')
plt.ylabel('T')
plt.title('insertion sort')
plt.gca().legend(('insertion sort', 'python sort', 'bubble sort'))
plt.gcf().canvas.set_window_title('Hendrik Meersseman')
plt.show()
