import data_manage
import utils
import sys
import json
import argparse
import math

parser = argparse.ArgumentParser(prog="SlimeFunCalculator", description="粘液科技计算器")

parser.add_argument("--items", type=str, help="要查询的所有物品", required=True)
parser.add_argument("--count", type=str, help="要查询的物品数量", required=True)

args = parser.parse_args()

items = args.items.replace(" ", "").split(",")
count = args.count.replace(" ", "").split(",")

needed = {}

if len(items) != len(count):
    print("Command line parameter error")
    exit(-1)

for i in range(0, len(items)):
    needed[items[i]] = int(count[i])

table = data_manage.get_table()

while utils.calculate(table, needed)[1]:
    needed = utils.calculate(table, needed)[0]
    # print(needed)

print("Raw data: {}".format(str(needed)))
for (key, value) in needed.items():
    if value > 64:
        if value != (math.floor(value / 64) * 64):
            print(
                "{}: {}组{}个".format(
                    key,
                    math.floor(value / 64),
                    int(value - (math.floor(value / 64) * 64)),
                )
            )
        else:
            print("{}: {}组".format(key, math.floor(value / 64)))
    else:
        print("{}: {}个".format(key, math.ceil(value)))
