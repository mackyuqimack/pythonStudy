"""
元组解包允许你将一个可迭代的元素（通常是一个元组）分配给变量。
"""
# 交换变量的值可以通过 a, b = b, a，因为 b, a 在右边形成元组（b, a），然后解包。
numbers = (1, 2, 3)
a, b, c = numbers
print(a)
print(b)
print(c)

"""
以星号（*）开头的变量将从迭代中取出所有其他变量剩余的值。
"""
a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(d)
