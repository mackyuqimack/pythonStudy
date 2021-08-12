import matplotlib.pyplot as plt

# 需求：电影拍片分布状况
# 1.准备数据
movie_name = ['雷神3：诸神黄昏', '正义联盟', '东方快车谋杀案', '寻梦环游记', '全球风暴', '降魔传', '追捕', '七十七天', '密战', '狂兽', '其它']
place_count = [60605, 54546, 45819, 28243, 13270, 9945, 7679, 6799, 6101, 4621, 20105]
# 2.创建画布
plt.figure(figsize=(20, 8), dpi=100)
# 3.绘制饼图
plt.pie(place_count, labels=movie_name, colors=['b', 'r', 'g', 'y', 'c', 'm', 'y', 'k', 'c', 'g', 'y'],
        autopct="%1.2f%%")
plt.axis("equal")
# 显示图例
plt.legend()
# 添加描述
plt.title("电影排片分布状况")
# 4.显示图像
plt.show()
