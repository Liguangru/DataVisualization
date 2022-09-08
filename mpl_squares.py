import matplotlib.pyplot as plt


"""可以在图表中显示中文"""
plt.style.use('seaborn')
plt.rcParams['font.sans-serif'] = ['SimHei']     # 显示中文，‘SimHei’是字体名称
# 为了坐标轴负号正常显示。matplotlib默认不支持中文，设置中文字体后，负号会显示异常。需要手动将坐标轴负号设为False才能正常显示负号。
plt.rcParams['axes.unicode_minus'] = False


input_values = [1, 2, 3, 4, 5, 6]
squares = [1, 4, 9, 16, 25, 36]


fig, ax = plt.subplots()  # 变量fig表示整张图片，变量ax表示图片中的各个图表
ax.plot(input_values, squares, linewidth=3)

"""设置图表标题并给坐标轴加上标签"""
ax.set_title("平方数", fontsize=24)
ax.set_xlabel("值", fontsize=14)
ax.set_ylabel("值的平方", fontsize=14)

"""设置刻度标记的大小"""
ax.tick_params(axis='both', labelsize=14)

plt.show()
