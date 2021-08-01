"""
类是使用关键字 class 和一个包含类方法的缩进块创建的。
__init__ 方法是一个类中最重要的方法。
这是在创建类的实例（对象）时使用类名称作为函数调用的。
所有的方法都必须以 self 作为自己的第一个参数，虽然它没有被明确地传递，但是 Python 为自己添加了自变量;
在调用方法时，不需要包含它。在一个方法定义中，self 指的是调用该方法的实例。
"""


class Cat:
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs


felix = Cat("ginger", 4)
print(felix.color)
print("felix:", felix.__dict__)  # dict是用来存储对象属性的一个字典，其键为属性名，值为属性的值.
# 在上面的例子中，__init__ 方法接受两个参数并将它们分配给对象的属性。__init__ 方法被称为类构造函数。

"""
类可以定义方法来为其添加功能。
请记住，所有的方法必须有 self 作为他们的第一个参数。
这些方法使用与属性相同的点语法进行访问。
"""


class Dog:
    legs = 4

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print(self.name + "," + self.color + "," + "Woof!")


print("----")
fido = Dog("Fido", "brown")
print(fido.name)
fido.bark()
# 类还可以具有通过在类的主体内分配变量而创建的类属性。这些可以从类的实例或类本身访问。
print(Dog.legs)
