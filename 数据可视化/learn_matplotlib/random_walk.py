from random import choice

class RandomWalk():
    """一个生成随机漫步的数据的类"""

    def __init__(self, num_points=5000):
        self.num_points = num_points
        # 随机漫步开始都是从0
        self.x_values = [0]
        self.y_values = [0]

    @staticmethod
    def get_step():
        derection = choice([-1, 1])
        distance = choice([0, 1, 2, 3, 4])
        step = derection * distance

        return step

    def fill_walk(self):
        """计算随机漫步包含的所有点"""

        # 不断漫步，直到到达指定的长度
        while len(self.x_values)<self.num_points:
            # 决定前进的方向和距离
            x_step = self.get_step()

            y_step = self.get_step()

            # 拒绝原地踏步
            if y_step == 0 and x_step == 0:
                continue

            # 计算下一个点的坐标
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
