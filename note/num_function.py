"""
数字函数:

要查找某些数字或列表的最大值或最小值，可以使用 max 和 min 。
要将数字转成绝对值（该数字与0的距离），请使用 abs 。
要将数字四舍五入到一定的小数位数，请使用 round 。
要计算一个列表数字的总和，请使用 sum 。
"""
print(min(1, 6, 3, 4, 0, 7, 1))
print(max([1, 2, 9, 2, 4, 7, 8]))
print(abs(-93))
print(abs(22))
print(sum([1, 2, 3, 4, 5, 6]))

"""
列表函数:

all 和 any 将列表作为参数， 通常在条件语句中使用。
all 列表中所有值均为 True 时，结果为 True，否则结果为 False。
any 列表中只要有一个为 True，结果为 True，反之结果为 False。
enumerate 函数可以用来同时迭代列表的键和值。
"""
nums = [55, 44, 33, 22, 11]
if all([i > 5 for i in nums]):
    print("All larger than 5")
if any([i % 2 == 0 for i in nums]):
    print("At least one is even")
for v in enumerate(nums):
    print(v)
