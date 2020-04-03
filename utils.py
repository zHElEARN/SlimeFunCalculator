import math


def add(a, b, c):
    if b in a.keys():
        a[b] += c
    else:
        a[b] = c


def calculate(table, needs, exist):
    loop = False
    nextNeed = {}

    # 遍历所有需要的
    for key, value in needs.items():
        # 如果表中有需要的
        if key in table.keys():

            if key in exist:
                print("exist")
                continue

            # 设置成需要继续循环
            loop = True

            # 循环表中获得需要的配方
            for subNeed in table[key].keys():
                # 添加到下一个需要的
                add(nextNeed, subNeed, table[key][subNeed] * value)
        # 如果没有需要的
        else:
            # 把当前有的放进下一个需要的
            add(nextNeed, key, value)

    return [nextNeed, loop]
