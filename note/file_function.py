"""
使用文件
要确保文件在使用后始终关闭，避免浪费资源是一种好的做法。一个方法是使用 try 和 finally 。
"""
try:
    f = open("newfile.txt")
    print(f.read())
finally:
    print("即使发生错误，这可以确保文件始终关闭。")
    f.close()

"""
一个替代方法是使用语句。这将创建一个临时变量（通常称为f），该变量只能在 with 语句的缩进块中访问。
"""
with open("newfile.txt") as f:
    print(f.read())
