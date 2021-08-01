"""
魔术方法是在名称的开始和结尾都有双下划线的特殊方法。
到目前为止，我们唯一遇到的是 __init__，但还有其他几个。
它们被用来创建不能用普通方法表示的功能。

它们的一个常见用途是运算符重载。
这意味着为自定义类定义运算符，允许使用 + 和 * 等运算符。
例子中魔术方法是 __add__ 重载 +。
__add__ 方法允许为我们的类中的 + 运算符定义自定义行为。
正如你所看到的，它添加了对象的相应属性并返回一个包含结果的新对象。
一旦定义了，我们就可以将这个类的两个对象相加。
"""
import random


class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)


first = Vector2D(5, 7)
second = Vector2D(3, 9)
result = first + second
print(result.x)
print(result.y)

"""
常见的魔术方法：
__sub__ 对应 -
__mul__ 对应 *
__truediv__ 对应 /
__floordiv__ 对应 //
__mod__ 对应 %
__pow__ 对应 **
__and__ 对应 &
__xor__ 对应 ^
__or__ 对应 |

表达式 x + y 被翻译成 x.__add__(y)。
然而，如果 x 没有实现 __add__，并且 x 和 y 的类型不同，则调用 y.__radd__(x)。
对于刚刚提到的所有魔法方法，都有等价的方法。
"""


class A:
    def __init__(self, cont):
        self.cont = cont


class B:
    def __init__(self, name):
        self.name = name

    def __radd__(self, other):
        return other.cont + "," + self.name


spam = A("spam")
hello = B("Hello world!")
print(spam + hello)

"""
Python 也为比较运算提供了魔术方法。
__lt__ 对应 <
__le__ 对应 <=
__eq__ 对应 ==
__ne__ 对应 !=
__gt__ 对应 >
__ge__ 对应 >=
如果 __ne__ 没有被实现，它将返回 __eq__ 相反的结果。
其他比较运算符之间没有其他关系。
"""


class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __gt__(self, other):
        for index in range(len(other.cont) + 1):
            result = other.cont[:index] + ">" + self.cont
            result += ">" + other.cont[index:]
            print(result)


spam1 = SpecialString("spam")
eggs2 = SpecialString("eggs")
print(spam1 > eggs2)

"""
有几个神奇的方法使类像容器一样行事。
__len__ 对应 len()
__getitem__ 对应 获取索引
__setitem__ 对应 分配索引值
__delitem__ 对应 删除索引值
__iter__ 对应 迭代对象（例如for循环）
__contains__ 对应 in
"""


class VagueList:
    def __init__(self, cont):
        self.cont = cont

    def __getitem__(self, index):
        return self.cont[index + random.randint(-1, 1)]

    def __len__(self):
        return random.randint(0, len(self.cont) * 2)


vague_list = VagueList(["A", "B", "C", "D", "E"])
print(len(vague_list))
print(len(vague_list))
print(vague_list[2])
print(vague_list[2])
