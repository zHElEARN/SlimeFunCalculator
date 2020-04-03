import math


def add(a, b, c):
    if b in a.keys():
        a[b] += c
    else:
        a[b] = c


def calculate(table, needs, exist):
    a = False
    need = {}
    for i, j in [(i, needs[i]) for i in needs.keys()]:
        if i in table.keys():
            a = True
            for k in table[i].keys():
                add(need, k, table[i][k] * j)
        else:
            add(need, i, j)

    print()
    return [need, a]
