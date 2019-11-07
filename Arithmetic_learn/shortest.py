import os

class Postpath:
    def __init__(self):
        # 存放邮局对应的点
        self.input_file_name = './input1.txt'
        # 用于输出最短距离合
        self.output_file_name = './output1.txt'
        # 用于计算最短路径和，初值为0
        self.sum = 0

    def start(self):
        with open(self.input_file_name, 'r') as f:
            num = int(f.readline())
            # 创建三个列表分别存x坐标，y坐标和点的位置
            x_list = []
            y_list = []
            point_list = []
            for point in range(num):
                # 取出每一行的内容并且用空格分割
                point = f.readline().split(' ')
                x = int(point[0])
                y = int(point[1])
                x_list.append(x)
                y_list.append(y)
                point_list.append((x, y))
            # 对x和y两个列表排序，以达到取中位数的目的
            x_list.sort()
            y_list.sort()
            x_mid = x_list[int(len(x_list) / 2)]
            y_mid = y_list[int(len(y_list) / 2)]
            for x, y in point_list:
                self.sum += abs(x - x_mid) + abs(y - y_mid)
        # 开始写入output1文件
        with open(self.output_file_name, 'w') as x:
            x.write(str(self.sum))
        print("邮局选址问题：使得最短距离的邮局地址坐标为：（%d, %d），最短距离为%d" %(x_mid, y_mid, self.sum))


class OilPipeline:
    def __init__(self):
        # 定义输出文件和输入文件
        self.input_file_name = './input1.txt'
        self.output_file_name = './output2.txt'
        # 用于计算最小长度和，初值为0
        self.sum = 0

    def start(self):
        with open(self.input_file_name, 'r') as f:
            num = int(f.readline())
            y_list = []
            for point in range(num):
                point = f.readline().split()
                y_list.append(int(point[1]))

            y_list.sort()
            y_mid = y_list[int(len(y_list)/2)]
            # 计算最短路径和
            for y in y_list:
                self.sum += abs(y_mid - y)

        with open(self.output_file_name, 'w') as x:
            x.write(str(self.sum))

        print("输油管道问题：使得最小长度的y坐标是%d，最短的距离为%d" %(y_mid, self.sum))

if __name__ == '__main__':
    s1 = Postpath()
    s1.start()

    s2 = OilPipeline()
    s2.start()
    pause = input("输入任意键退出...")
