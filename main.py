import data_manage
import utils

table = data_manage.get_table()


needed = {'GPS发射器': 10}

while utils.calculate(table, needed)[1]:
    needed = utils.calculate(table, needed)[0]
    # print(needed)

for (key, value) in needed.items():
    print("{}: {}个".format(key, value))
