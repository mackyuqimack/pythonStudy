import random

import matplotlib.pyplot as plt

# 完善原始折线图（辅助显示层）
# 需求︰画出某城市11点到12点1小时内每分钟的温度变化折线图，温度范围在15度~18度
# 1.准备数据x,y
x = range(60)
y_shanghai = [random.uniform(15, 18) for i in x]
# 2.创建画布
plt.figure(figsize=(20, 8), dpi=100)
# 3.绘制图像
plt.plot(x, y_shanghai)
# 添加自定义刻度
# plt.xticks(x,**kwargs) x:要显示的刻度值    plt.yticks(y,**kwargs)
# 准备x的刻度说明
x_lable = ["11点{}分".format(i) for i in x]
plt.xticks(x[::5], x_lable[::5])
plt.yticks(range(0, 40, 5))
# 4.显示图像
# 注意: plt.show()会释放figure资源，如果在显示图像之后保存图片将只能保存空图片。
plt.show()
