
def accurate_position(coordinate):
    """
    根据 x 和 y 坐标的变化序列，对坐标进行一系列的精确定位
    z索引号表示x,y坐标，索引上的值代表其上的电容值
    :param coordinate: a list with int num
    :return: a num
    """
    sum_index = 0
    # 计算值乘以坐标的总数，最后要除以列表和
    i = 0
    for values in coordinate:
        sum_index += values * i
        i += 1

    # 使用round()函数来控制小数点后两位
    return round(sum_index/sum(coordinate), 2)

def cluster(coordinate_x, coordinate_y):
    """
    分簇，把序列截分成一个或者两个高峰部分，然后传给精确定位获得坐标
    :param coordinate_x: a list with int num to show x
    :param coordinate_y: a list with int num to show y
    :return: 一个包含坐标元组的列表
    """

    # 用两个列表储存x和y可能的值
    x_lst = []
    y_lst = []
    # 用一个标志来表示是否有两个高峰，有的话为对应index的值，没有为-1
    global x_flag, y_flag
    x_flag = -1
    y_flag = -1
    for x_index in range(1, len(coordinate_x)-1):
        # 由于最多只有两个点，所以即使有也只有一个极小值，或者有两个一样的值，那么这个点对应的索引就可以用来分簇
        if (coordinate_x[x_index] < coordinate_x[x_index-1] and coordinate_x[x_index] <= coordinate_x[x_index+1]) :
            x_flag = x_index
            break
    if x_flag == -1:
        x_lst.append(accurate_position(coordinate_x))
        x_lst.append(accurate_position(coordinate_x))
    else:
        x_lst.append(accurate_position(coordinate_x[:x_flag]))
        x_lst.append(accurate_position(coordinate_x[x_index+1:]))
    for y_index in range(1, len(coordinate_y) - 1):
        # 由于最多只有两个点，所以即使有也只有一个极小值，那么这个点对应的索引就可以用来分簇
        if (coordinate_y[y_index] < coordinate_y[y_index - 1] and coordinate_y[y_index] <= coordinate_y[y_index + 1]):
            y_flag = y_index
            break
    if y_flag == -1:
        y_lst.append(accurate_position(coordinate_y))
        y_lst.append(accurate_position(coordinate_y))
    else:
        y_lst.append(accurate_position(coordinate_y[:y_flag]))
        y_lst.append(accurate_position(coordinate_y[y_index+1:]))

    # 对两组列表进行排序，规定zoom的方向确定
    x_lst.sort()
    y_lst.sort()

    return list(zip(x_lst, y_lst))

def Zoom(tpl):
    """
    利用触屏两点的坐标变化来确定放大、缩小和不变三种状态
    :param tpl: 一个元组，里面是 x 和 y 变化的元组序列
    :return: 三个状态（-1：缩小，0：不变，1：放大）的列表
    """

    # 计算距离放在一个列表，看距离变化
    distance = []
    status = []
    for index in range(len(tpl)):
        lst = cluster(*tpl[index])
        distance.append(pow(lst[0][0]-lst[1][0], 2) + pow(lst[0][1]-lst[1][1], 2))
    for index in range(len(distance)-1):
        if distance[index] < distance[index+1]:
            status.append(1)
        elif distance[index] > distance[index+1]:
            status.append(-1)
        else:
            status.append(0)
    return status

if __name__ == '__main__':
    # x =(([0, 6, 137, 84, 9, 4], [1, 4, 45, 25, 2, 2, 13, 52, 58, 15, 4]),)
    x = (([1, 20, 45, 60, 70, 39, 70, 90, 30, 20], [3, 6, 50, 90, 110, 36, 25, 45, 60, 74, 80, 100]),
         ([1, 20, 45, 60, 70, 39, 70, 90, 30, 20], [0, 40, 70, 81, 100, 56, 8, 5, 89, 0]),
         ([1, 20, 45, 60, 70, 39, 70, 90, 30, 20], [3, 6, 50, 90, 110, 36, 25, 45, 60, 74, 80, 100]))
    status = Zoom(x)
    for value in status:
        if value == 1:
            print("Bigger!")
        elif value == -1:
            print("Smaller!")
        else:
            print("Same!")