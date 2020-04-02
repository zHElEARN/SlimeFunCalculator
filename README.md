# SlimeFunCalculator | 粘液科技材料计算器

**现在合成表暂不完整！ 可以提交 Pull Request 来补充合成表！**

## 用法

提供你需要合成的物品和物品的数量

程序会返回需要的材料！

### Usage

```shell
❯ python main.py -h
usage: SlimeFunCalculator [-h] --items ITEMS --count COUNT

粘液科技计算器

optional arguments:
  -h, --help     show this help message and exit
  --items ITEMS  要查询的所有物品
  --count COUNT  要查询的物品数量
```

## Example

```shell
❯ python main.py --items=电动马达,电磁铁 --count=4,4
地狱岩: 256个
锌粉: 16个
铜粉: 73.0个
红石粉: 8个
铁粉: 88个
铝粉: 8个
```
