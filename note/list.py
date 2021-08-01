"""
列表推导

[表达式1 for k in L if 表达式2 ]
相当于：
List = []
for k in L:
    if 表达式2:
        List.append(表达式1)
"""

evens = [i ** 2 for i in range(10) if i ** 2 % 2 == 0]
print(evens)
