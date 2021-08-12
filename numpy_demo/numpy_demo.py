import numpy as np
import random
import time

# 生成一个大数组
python_list = []
for i in range(100000000):
    python_list.append(random.random())

ndarray_list = np.array(python_list)

# 原生pythonlist求和
t1 = time.time()
a = sum(python_list)
t2 = time.time()
d1 = t2 - t1

# ndarray求和
t3 = time.time()
b = np.sum(ndarray_list)
t4 = time.time()
d2 = t4 - t3

print(d1)
print(d2)