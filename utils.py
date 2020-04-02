import math


def add(a, b, c):
    if b in a.keys():
        a[b] += c
    else:
        a[b] = c


def calculate(table, needs):
    a = False
    new = {}
    for i, j in [(i, needs[i]) for i in needs.keys()]:
        if i in table.keys():
            a = True
            for k in table[i].keys():
                add(new, k, table[i][k]*j)
        else:
            add(new, i, j)

    return [new, a]
