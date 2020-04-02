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

    for i, j in [(i, new[i]) for i in new.keys()]:
        if type(j) == type(0.0):
            new[i] = math.ceil(j)

    # new

    return [new, a]
