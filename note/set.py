"""
集合是数据结构，类似于列表或字典。集合使用花括号或 set 函数创建。
它们与列表共享一些功能，例如使用 in 来检查它们是否包含特定项目。
"""
# num_set = {1, 2, 3, 4, 5}
# word_set = set(["spam", "eggs", "sausage"])
#
# print(3 in num_set)
# print("spam" not in word_set)

"""
集合可以使用数学运算进行组合。
联合运算符 | 结合两个集合形成一个包含两个集合任一项目的新集合。
相交运算符＆ 获得两个集合共有的项目
差运算符 - 获取第一集合中的项目，但不是第二集合中的项目。
对称差分运算符^ 获取任集合中非共有的项目。
"""

first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first | second)
print(first & second)
print(first - second)
print(second - first)
print(first ^ second)
