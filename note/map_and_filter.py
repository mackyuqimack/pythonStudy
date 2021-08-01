"""
map

内置的函数 map 和 filter 是在列表（或类似的称为迭代的对象）上运行的非常有用的高阶函数。
函数 map 接受一个函数和一个迭代器作为参数，并返回一个新的迭代器，该函数应用于每个参数。
"""


def add_five(x):
    return x + 5


nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))
print(result)

"""
通过使用 lambda 语法，我们可以更容易地获得相同的结果。
"""

nums = [11, 22, 33, 44, 55]

result = list(map(lambda x: x + 5, nums))
print(result)

"""
filter 函数通过删除与谓词（一个返回布尔值的函数）不匹配的项来过滤一个迭代。
filter(function, iterable)
function -- 判断函数。
iterable -- 可迭代对象
"""

nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x % 2 == 0, nums))
print(res)
