
# 手套配对方案
# 手套类

class gloves:
    def __init__(self):
        self.name = "选择手套"
        # 各种颜色的手套数量，单位是双
        self.red = 5
        self.yellow = 4
        self.green = 2

    def start(self):
        print("----------------------%s-----------------------" %self.name)
        # 无论何时都是最少需要两只手套
        print("最少选2只手套就能配对")
        # 用来计数最多用多少只手套可恶意配对
        count = 0

        # 取所有手套的单只，再加任意颜色一只变一定配对
        count += self.red + self.yellow + self.green + 1
        print("最多选%d只手套能配对" %count)


class socks:
    def __init__(self):
        self.name = "丢失的袜子"
        # 定义袜子的数量，单位是双
        self.num = 5
    def start(self):
        print("----------------------%s-----------------------" % self.name)
        # 计算刚好取到一对的概率，由于是对立事件，直接用1去减就好
        good = 2 * self.num/(self.num * 2 * (2 * self.num - 1))
        bad = 1 - good
        # 对应的数学期望，根据题意后期取整数
        expection = int(4 * good + 3 * bad)

        print("最佳情况发生的概率是%f" %good)
        print("最差情况发生的概率是%f" %bad)

        print("平均状况下指望留下%d双袜子" %expection)






if __name__ == '__main__':
    gloves = gloves()
    gloves.start()

    print()
    socks = socks()
    socks.start()

    pause = input("输入任意键退出...")
