import random
import matplotlib.pyplot as plt

# 完善折线图（图像层）
# 需求：将北京和上海分开显示
# 1.准备数据x,y
x = range(60)
y_shanghai = [random.uniform(15, 18) for i in x]
y_beijing = [random.uniform(1, 3) for i in x]
# 2.创建画布
# plt.figure(figsize=(20, 8), dpi=100)
figure, axes = plt.subplots(nrows=1, ncols=2, figsize=(20, 8), dpi=80)
# 3.绘制图像
axes[0].plot(x, y_shanghai, color="r", linestyle="--", label="上海")
axes[1].plot(x, y_beijing, color="b", linestyle="-.", label="北京")
# 显示图例
axes[0].legend()
axes[1].legend()

# 添加自定义刻度
# plt.xticks(x,**kwargs) x:要显示的刻度值    plt.yticks(y,**kwargs)
# 准备x的刻度说明
x_lable = ["11点{}分".format(i) for i in x]
axes[0].set_xticks(x[::10])
axes[0].set_xticklabels(x_lable[::10])
axes[0].set_yticks(range(0, 40, 5))
axes[1].set_xticks(x[::5])
axes[1].set_xticklabels(x_lable[::5])
axes[1].set_yticks(range(0, 40, 5))
# 添加网格
axes[0].grid(linestyle="--", alpha=0.5)
axes[1].grid(linestyle="--", alpha=0.5)
# 添加描述
axes[0].set_xlabel("时间变化")
axes[0].set_ylabel("温度变化")
axes[0].set_title("上海11点到12点每分钟温度变化状况")
axes[1].set_xlabel("时间变化")
axes[1].set_ylabel("温度变化")
axes[1].set_title("北京11点到12点每分钟温度变化状况")
# 4.显示图像
# 注意: plt.show()会释放figure资源，如果在显示图像之后保存图片将只能保存空图片。
plt.show()
