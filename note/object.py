"""
对象的生命周期由对象的创建，操作和销毁几个部分组成。
对象的生命周期
第一阶段是它所属的类的定义。
下一个阶段是调用 __init__ 时实例的实例化。内存被分配来存储实例。
在调用 __init__ 方法之前，Python首先调用 __new__ 方法。
这之后，对象就可以使用了。
"""


class Cls:
    # def __new__(cls, string):
    #     super().__new__(cls)
    #     print("hello world" + string)

    def __init__(self, name):
        self.name = name
        print("我是构造方法")

    def __del__(self):
        print("删除了")


t = Cls("小李")
