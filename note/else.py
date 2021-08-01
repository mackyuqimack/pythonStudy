"""
else 语句与 if 语句一起使用最为普遍，但它也可以遵循 for 或 while 循环，从而赋予它不同的含义。
使用 for 或 while 循环，如果循环正常结束（当 break 语句不会导致循环退出时），则会调用其中的代码。
"""
# 第一个 for 循环正常执行，导致打印 “Unbroken 1”。
# 第二个循环由于中断而退出，这就是为什么 else 语句不被执行。
for i in range(10):
    if i == 999:
        break
else:
    print("Unbroken 1")

for i in range(10):
    if i == 5:
        break
else:
    print("Unbroken 2")

"""
else 语句也可以和 try/except 语句一起使用。
在这种情况下，只有在 try 语句中没有发生错误时才会执行其中的代码。
"""

try:
    print(1)
except ZeroDivisionError:
    print(2)
else:
    print(3)

try:
    print(1 / 0)
except ZeroDivisionError:
    print(4)
else:
    print(5)
