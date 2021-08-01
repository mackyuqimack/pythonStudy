"""
属性提供了一种自定义实例属性访问的方法。
它们是通过将属性装饰器放在一个方法上面创建的，这意味着当访问与方法同名的实例属性时，方法将被调用。
属性的一种常见用法是使属性为只读。
"""


class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @property
    def pineapple_allowed(self):
        return False


pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True

"""
属性也可以通过定义 setter/getter 函数来设置。
setter 函数设置相应的属性值。
getter 函数获取相应的属性值。
要定义一个 setter，你需要使用一个与属性相同名字的装饰器，后面跟着 .setter。
这同样适用于定义 getter 函数。
"""


class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
        self._pineapple_allowed = False

    @property
    def pineapple_allowed(self):
        return self._pineapple_allowed

    @pineapple_allowed.setter
    def pineapple_allowed(self, value):
        if value:
            password = input("Enter the password: ")
            if password == "123":
                self._pineapple_allowed = value
            else:
                raise ValueError("Alert! Intruder!")


pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True
print(pizza.pineapple_allowed)
