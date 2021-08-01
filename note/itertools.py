"""
itertools 模块是一个标准库，包含了几个在函数式编程中很有用的函数。
一种类型的函数是无限迭代器。
count 函数从一个值无限增加。
cycle 函数无限次迭代（例如列表或字符串）。
repeat 函数重复一个对象，无论是无限还是特定的次数。
"""

from itertools import count

for i in count(3):
    print(i)
    if i >= 11:
        break

'''
itertools 中有许多功能可以在迭代器上运行，类似于映射和过滤。
例如：
takewhile - 当判定函数（返回值为 True 或 False）保持为True时，从迭代中取得项目;
chain - 将几个迭代结合成一个长整数;
accumulate - 以可迭代的方式返回一个正在运行的值。accumulate函数的功能是对传进来的iterable对象逐个进行某个操作（默认是累加，如果传了某个fun就是应用此fun)
'''

from itertools import accumulate, takewhile

print("----")
nums = list(accumulate(range(8)))
print(nums)
print(list(takewhile(lambda x: x <= 6, nums)))

"""
itertool中还有几个组合函数，比如 product 和 permutation。
当你想用一些项目的所有可能的组合来完成任务时使用。
"""
from itertools import product, permutations

print("----")
letters = ("A", "B")
print(list(product(letters, range(2))))
print(list(permutations(letters)))
