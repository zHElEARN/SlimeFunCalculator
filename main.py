import data_manage
import utils
import sys
import json
import argparse

# 定义argparse解析器
parser = argparse.ArgumentParser(prog="SlimeFunCalculator", description="粘液科技计算器")

# 设置命令行参数
parser.add_argument("--items", type=str, help="要查询的物品", required=True)
parser.add_argument("--count", type=str, help="要查询的物品数量", required=True)
parser.add_argument("--exist", type=str, help="已有的物品", required=False, default="QWQ")

# 解析命令行
args = parser.parse_args()

# 将需要查询的物品和物品数量解析成列表
items = args.items.replace(" ", "").split(",")
count = args.count.replace(" ", "").split(",")
exist = []

# 如果不是默认值
if args.exist != "QWQ":
    # 则转换成列表
    exist = args.exist.replace(" ", "").split(",")

needed = {}

# 如果长度不相等
if len(items) != len(count):
    print("Command line parameter error")
    exit(-1)

# 将需要的设置成字典
for i in range(0, len(items)):
    needed[items[i]] = int(count[i])

# 获得表
table = data_manage.get_table()

# 获得数据
while utils.calculate(table, needed, exist)[1]:
    needed = utils.calculate(table, needed, exist)[0]
    # print(needed)

print("Raw data: {}".format(str(needed)))

# 处理数据
for (key, value) in needed.items():
    if value >= 64:
        if value % 64 != 0:
            print(
                "{}: {}组{}个".format(
                    key,
                    int(value // 64),
                    int(value % 64),
                )
            )
        else:
            print("{}: {}组".format(key, int(value // 64)))
    else:
        print("{}: {}个".format(key, int(value)))
