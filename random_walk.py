from random import choice


class RandomWalk:
    """一个生成随机漫步数据的类"""

    def __init__(self, num_points=5000):
        """初始化随机漫步的属性"""
        self.num_points = num_points

        """所有随机漫步都始于（0， 0）"""
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """计算随机漫步包含的所有点"""

        """不断漫步，直到列表达到指定的长度"""
        while len(self.x_values) < self.num_points:

            """决定前进方向以及沿这个方向前进的距离"""
            x_direction = choice([1, -1])            # 向左走还是向右走

            x_distance = choice([0, 1, 2, 3, 4])     # 包含0，可以使得移动更加灵活
            x_step = x_direction * x_distance        # x_step为正向右移动，为负向左移动，为0则垂直移动

            y_direction = choice([1, -1])            # 向上走还是向下走

            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance        # y_step为正向上移动，为负向下移动，为0则水平移动

            """拒绝原地踏步"""
            if x_step == 0 and y_step == 0:          # 如果x和y都为0将会原地踏步，拒绝原地踏步，让其进入下一个循环
                continue

            """计算下一个点的x和y值"""
            x = self.x_values[-1] + x_step           #-1指的是最后的一个值
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
