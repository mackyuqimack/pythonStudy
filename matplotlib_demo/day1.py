import random
import matplotlib.pyplot as plt

# 完善折线图（图像层）
# 需求：再添加一个城市的温度变化
# 收集北京当天温度变化情况，温度1度到3度
# 1.准备数据x,y
x = range(60)
y_shanghai = [random.uniform(15, 18) for i in x]
y_beijing = [random.uniform(1, 3) for i in x]
# 2.创建画布
plt.figure(figsize=(20, 8), dpi=100)
# 3.绘制图像
plt.plot(x, y_shanghai, color="r", linestyle="--", label="上海")
plt.plot(x, y_beijing, color="b", linestyle="-.", label="北京")
# 显示图例
plt.legend()

# 添加自定义刻度
# plt.xticks(x,**kwargs) x:要显示的刻度值    plt.yticks(y,**kwargs)
# 准备x的刻度说明
x_lable = ["11点{}分".format(i) for i in x]
plt.xticks(x[::5], x_lable[::5])
plt.yticks(range(0, 40, 5))
# 添加网格
plt.grid(linestyle="--", alpha=0.5)
# 添加描述
plt.xlabel("时间变化")
plt.ylabel("温度变化")
plt.title("上海、北京11点到12点每分钟温度变化状况")
# 4.显示图像
# 注意: plt.show()会释放figure资源，如果在显示图像之后保存图片将只能保存空图片。
plt.show()
