"""
Python 允许具有不同数量的参数的函数。
使用 *args 作为函数参数，可以将任意数量的参数传递给该函数。参数可以作为函数主体中的元组参数访问。
例如:
"""


# 参数 *args 必须位于命名参数之后。
# 名字 args 只是一个惯例，你可以选择使用另一个自定义的名字。
def function(named_arg, *args):
    print(named_arg)
    print(args)


function(1, 2, 3, 4, 5)
"""
默认值
给函数指定的参数可以通过给它们一个默认值使其成为可选的参数。
指定默认值的参数，必须在未指定默认值参数之后。
例如：
"""


# 在传入参数的情况下，默认值将被忽略。
# 如果参数未传入，则使用默认值。
def function(x, y, fruit="apple"):
    print(fruit)


function(1, 2)
function(3, 4, "banana")

"""
函数参数
**kwargs（代表关键字参数）允许你处理尚未预先定义的命名参数。
关键字参数返回一个字典，其中键是参数名称，值是参数数值。
例如：
"""


# a 和 b 是我们传递给函数调用的参数的名称。
# **kwargs 返回的参数不包含在 *args 中。
def my_func(x, y=7, *args, **kwargs):
    print(kwargs)


my_func(2, 3, 4, 5, 6, a=7, b=8)
