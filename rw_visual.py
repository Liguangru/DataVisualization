import matplotlib.pyplot as plt
from random_walk import RandomWalk

"""可以在图表中显示中文"""
plt.style.use('classic')
plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文，‘SimHei’是字体名称
plt.rcParams['axes.unicode_minus'] = False    # 为了坐标轴负号正常显示。

"""只要程序处于活动状态就不断模拟随机漫步"""
while True:
    """创建一个RandomWalk实例"""
    rw = RandomWalk()
    rw.fill_walk()

    """将所有的点都绘制出来"""
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9), dpi=500)  # 可以设置画布尺寸和分辨率
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)
    # edgecolors='none'会删除每个点的黑色轮廓，点的颜色逐渐从浅到深

    """突出起点和终点"""
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)   # 使用绿色绘制起点（0，0），并且更大
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)  # 使用红色绘制终点，并更大

    """隐藏坐标轴"""
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk?(y/n): ")
    if keep_running == 'n':
        break
