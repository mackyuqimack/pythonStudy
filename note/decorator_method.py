"""
装饰者 是修改其他函数的功能的函数。装饰器有助于让我们的代码更简短。
当您需要扩展您不想修改的函数功能时，这是很理想的。
这个模式可以随时用来包装任何功能。
Python通过预先用装饰器名称和 @symbol 预定义函数定义来提供支持，以便在装饰器中包装函数。
如果我们正在定义一个函数，我们可以使用@符号来“装饰”它：
"""


def decor(func):
    def wrap():
        print("============")
        func()
        print("============")

    return wrap


@decor
def print_text():
    print("Hello world!")


# 一个函数可以有多个装饰器。
print_text()
