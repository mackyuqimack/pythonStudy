"""
<b>继承</b>提供了一种在类之间共享功能的方法。
想象几个类，Cat，Dog，Rabbit等。虽然它们在某些方面可能有所不同（只有 Dog 可能有 bark 方法），但它们可能在其他方面相似（都具有 color 和 name 的属性）。
这种相似性可以通过使它们全部从包含共享功能的超类 Animal 中继承来表示。
要从另一个类继承一个类，请将超类名放在类名后面的括号中。

从另一个类继承的类称为子类。
被继承的类被称为超类。
如果一个类继承了另一个具有相同属性或方法的类，它的属性和方法将覆盖它们。
"""


class Wolf:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("Grr...")


class Dog(Wolf):
    def bark(self):
        print("Woof")


husky = Dog("Max", "grey")
husky.bark()

"""
继承也可以是间接的。一个类B继承类A，而类C也可以继承类B。
但是，不允许循环继承。
"""


class A:
    def method(self):
        print("A method")


class B(A):
    def another_method(self):
        print("B method")


class C(B):
    def third_method(self):
        print("C method")


c = C()
c.method()
c.another_method()
c.third_method()

"""
super 函数是一个与父类继承相关的函数。它可以用来在对象的超类中找到具有特定名称的方法。
super().spam() 是调用超类的 spam 方法
"""


class A:
    def spam(self):
        print(1)


class B(A):
    def spam(self):
        print(2)
        super().spam()


B().spam()
