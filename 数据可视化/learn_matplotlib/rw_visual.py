import matplotlib.pyplot as plt
from matplotlib.random_walk import RandomWalk


while True:
    # 创建一个实例，把所有的点绘制出来
    rw = RandomWalk(50000)
    rw.fill_walk()

    # 设置绘图窗口的尺寸，默认像素dpi=80
    plt.figure(dpi=300, figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    # 通过渐变表示点产生的先后顺序
    plt.scatter(rw.x_values, rw.y_values, s=1, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none')

    # 标明它们的起点和终点
    plt.scatter(0, 0, edgecolors='none', s=10, c='green')
    plt.scatter(rw.x_values[-1], rw.y_values[-1], edgecolors='none', s=10, c='red')

    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    # plt.savefig('squares_scatter.png', bbox_inches='tight')
    plt.show()

    choice = input("Make another walk?(y/n)")
    if choice == 'n':
        break