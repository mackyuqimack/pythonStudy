"""
生成器是一种可迭代的类型，如列表或元组。
与列表不同的是，它们不允许使用任意索引，但是它们仍然可以通过 for 循环迭代。
可以使用 函数 和 yield 语句来创建它们。
"""


def countdown():
    i = 5
    while i > 0:
        yield i
        i -= 1


for i in countdown():
    print(i)
