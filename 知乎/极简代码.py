from collections import Counter
import sys
from math import  ceil

# 重复元素判定，set()函数可以消除列表中的重复元素
# 有重复元素返回False，没有返回True
def all_unique(lst):
    return len(lst) == len(set(lst))

# 判断两个字符串的组成元素是否一致，是返回True
# Counter()统计字符串中各个字符的数量，返回一个字典
def anagram(first, second):
    return  Counter(first) == Counter(second)

# 检查变量占用的内存
def cost_area(variable):
    print(sys.getsizeof(variable))

# 字节占用，检测字符串占用的字节数
def byte_size(string):
    return (len(string.encode("utf-8")))

# 给定具体的大小，定义一个函数以按照这个大小切割列表
# map() 会根据提供的函数对指定序列做映射。
# 第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
# ceil() 函数返回数字的上入整数。
def chunk(lst, size):
    return list(
        map(lambda x: lst[x * size:x * size + size],
            list(range(0, ceil(len(lst)/size))))
    )


# 测试主函数
if __name__ == '__main__':
    # 检查是否有重复元素
    x = [1, 1, 2, 3, 3, 4]
    y = [1, 2, 3, 4]
    print(all_unique(x), all_unique(y))

    # 判断两个字符串 的组成元素
    first = 'sdxc23'
    second = 's2dx3c'
    print(anagram(first, second))

    # 判断变量占用的内存
    x = 30
    cost_area(x)

    # 字节占用
    print(byte_size("☺"))
    print(byte_size("hello world"))

    # 大写第一个字母
    print('my program is you'.title())

    # 切割列表
    print(chunk([1, 2, 3, 4, 5], 2))