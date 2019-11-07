"""
这个程序是利用分治法解决单循环比赛的日程安排
主要有以下几个函数，包括了分治法本身
数组的操作函数还有最后的打印函数
输入都是数组名还有对应的数组长度
"""

def tourna(array, n):
    """
    :param array:二维数组表示队伍赛程信息
                a[i][j] = k 表示：第i队和第k队在第j天进行比赛
    :param n: 数组的长度
    :return: 无
    """
    # 递归结束条件：当数组长度为1就不用打比赛了
    if n == 1:
        array[0][0] = 0
        return
    # 如果二分之后不是偶数，加一保证偶数性质
    if n % 2 == 1:
        tourna(array, n+1)
        return
    tourna(array, n/2)
    # 奇偶采取不同处理
    if (n/2) > 1 and (n/2) % 2 == 1:
        oddcopy(array, n)
    else:
        copy(array, n)

def oddcopy(array, n):
    """
    奇数的数组操作办法

    """
    m = int(n/2)
    b = [0] * (n+1)
    # 创建一个新数组，存放i位队伍的对应队伍
    for i in range(0, m):
        b[i] = m + i
        b[i + m] = b[i]
    for i in range(0, m):
        # 轮空的队伍与它相隔的最近一个没有赛程的队伍进行比赛
        for j in range(0, m+1):
            if array[i][j] >= m:
                array[i][j] = b[i]
                array[m+i][j] = (b[i]+m) % n
            else:
                array[m+i][j] = array[i][j] + m
        for j in range(0, m):
            array[i][m+j] = b[i+j]
            array[b[i+j]][m+j] = i


def copy(array, n):
    """
       偶数的数组操作办法

       """
    m = int(n/2)
    for i in range(0, m):
        # 三步操作分别带有：
        # 1.前半队伍安排后半时间的队伍
        # 2.后半队伍安排前半时间的队伍
        # 3.后半队伍安排后半时间的队伍
        for j in range(0, m):
            array[i][j+m] = array[i][j] + m
            array[i+m][j] = array[i][j+m]
            array[i+m][j+m] = array[i][j]

def print_sche(array, n):
    """
    按一定格式打印赛程信息

    """
    print("第一列为队伍编号，第二列开始是第一、二...天对阵的队伍编号：", end="")
    if n % 2 == 1:
        n += 1
    for i in range(0, n):
        print()
        for j in range(0, n):
            print("%d  " %array[j][i], end="")

if __name__ == '__main__':
    n = int(input("请输入球队数量："))
    array = [[0] * (n+1) for i in range(n+1)]
    tourna(array, n)
    print_sche(array, n)
    print()
    pause = input("输入任意键退出...")
