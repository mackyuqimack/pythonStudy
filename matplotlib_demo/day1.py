import matplotlib.pyplot as plt

# 1.准备数据
movie_name = ['雷神3：诸神黄昏', '正义联盟', '寻梦环游记']
first_day = [10587.6, 10062.5, 1275.7]
first_weekend = [36224.9, 34479.6, 11830]
x = range(len(movie_name))
# 2.创建画布
plt.figure(figsize=(20, 8), dpi=100)
# 3.绘制图像
plt.bar(x, first_day, width=0.2, label="首日票房")
plt.bar([i + 0.2 for i in x], first_weekend, width=0.2, label="首周票房")
# 显示图例
plt.legend()
# 修改刻度
plt.xticks([i + 0.1 for i in x], movie_name)
# 添加网格
plt.grid(linestyle="--", alpha=0.5)
plt.title("电影票房收入对比")
# 4.显示图像
plt.show()