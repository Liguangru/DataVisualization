import matplotlib.pyplot as plt

"""可以在图表中显示中文"""
plt.style.use('seaborn')
plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文，‘SimHei’是字体名称
plt.rcParams['axes.unicode_minus'] = False  # 为了坐标轴负号正常显示。

x_values = range(1, 1100)
y_values = [x**2 for x in x_values]

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)  # s设置点的尺寸，并由浅到深显示数据

"""设置图表标题并给坐标轴加上标签"""
ax.set_title("平方数", fontsize=24)
ax.set_xlabel("值", fontsize=14)
ax.set_ylabel("值的平方", fontsize=14)

"""设置每个坐标轴的取值范围"""
ax.axis([0, 1200, 0, 1100000])

"""设置刻度标记的大小"""
ax.tick_params(axis='both', which='major', labelsize=14)

"""显示图表"""
plt.show()

"""自动保存图表"""
# plt.savefig('name', bbox_inches='tight')  # bbox_inches='tight' 是裁剪掉多余的空白部分
