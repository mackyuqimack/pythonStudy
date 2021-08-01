"""
到目前为止，我们所看到的对象的方法被一个类的实例所调用，然后被传递给方法的 self 参数。
类方法是不同的 - 它们被一个类所调用，类方法传递的 参数是 cls 。
类方法用 classmethod 装饰器标记。
"""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    @classmethod
    def new_square(cls, side_length):
        return cls(side_length, side_length)


# new_square 是一个类方法，在类上调用，而不是在类的实例上调用。它返回类 cls 的新对象。
square = Rectangle.new_square(5)
print(square.calculate_area())

"""
静态方法与类方法类似，只是它们没有任何额外的参数。
它们用 staticmethod 装饰器标记。
"""


class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @staticmethod
    def validate_topping(topping):
        if topping == "pineapple":
            raise ValueError("No pineapples!")
        else:
            return True


# 除了可以从类的一个实例调用它们之外，静态方法的行为与纯函数类似。
ingredients = ["cheese", "onions", "spam"]
if all(Pizza.validate_topping(i) for i in ingredients):
    pizza = Pizza(ingredients)
