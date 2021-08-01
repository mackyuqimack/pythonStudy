# 1、按照默认顺序，不指定位置

print("{} {}".format("hello", "world"))

# 2、设置指定位置，可以多次使用

print("{0} {1} {0}".format("hello", "or"))

# 3、使用字典格式化

person = {"name": "W3Cschool", "age": 5}

print("My name is {name} . I am {age} years old .".format(**person))

# 4、通过列表格式化

stu = ["W3Cschool", "linux", "MySQL", "Python"]

print("My name is {0[0]} , I love {0[1]} !".format(stu))

# 最后一种格式化字符串的方法是使用以f开头的字符串，称之为f-string，它和普通字符串不同之处在于，字符串如果包含{xxx}，就会以对应的变量替换：

r = 2.5
s = 3.14 * r ** 2
print(f'The area of a circle with radius {r} is {s:.2f}')
# The area of a circle with radius 2.5 is 19.62
# 上述代码中，{r}被变量r的值替换，{s:.2f}被变量s的值替换，并且:后面的.2f指定了格式化参数（即保留两位小数），因此，{s:.2f}的替换结果是19.62。
