from collections import Counter
import sys
from math import ceil
import re
import time
import operator

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

# 这个方法可以将布尔型的值去掉
# filter()函数：用于过滤序列，过滤掉不符合条件的元素，
# 返回一个迭代器对象，如果要转换为列表，可以使用 list() 来转换
def compact(lst):
    return list(filter(bool, lst))

# 统计元音的个数（通过正则表达式）
def count_vowels(str):
    return len(re.findall(r'[aeiou]', str, re.IGNORECASE))

# 通过递归的方式将列表的嵌套展开为单个列表
# extend() 函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）。
def spread(arg):
    ret = []
    for i in arg:
        # 判断两者是否类型相同
        if isinstance(i, list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret

def deep_flatten(lst):
    result = []
    result.extend(
        spread(list(map(lambda x: deep_flatten(x) if type(x) == list else x, lst))))
    return result

# 返回第一个列表的元素，其不再第二个列表内。
def Difference(a, b):
    set_a = set(a)
    set_b = set(b)
    comparison =set_a.difference(set_b)
    return list(comparison)

# 可以在一行内调用多个函数
def add(a, b):
    return  a + b

def subtract(a, b):
    return a - b

# 检查两个列表是否有重复项
def has_duplicates(lst):
    return len(set(lst))!=len(lst)

# 合并两个字典
def merge_dict(a, b):
    c = a.copy()
    c.update(b)
    return c
    # 如果是3.5以上版本还可用
    # return {**a, **b}

# 两个列表转化为字典
def to_dict(a, b):
    return dict(zip(a, b))

# 提取列表中最常见的元素
# key关键字的作用是，对每个元素先使用key指定的function来处理，然后再比较、返回预期的元素。
def most_frequent(lst):
    return max(set(lst), key=lst.count)

# 不需要额外的操作就可以交换两个变量的值
def swap(a, b):
    return b, a

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

    # 取出布尔型的值
    print(compact([0, 1, False, 2, '', 3]))

    # 可以在一行代码中使用不同的运算符对比多个不同的元素
    a = 3
    print(2 < a < 8)
    print(1 == a < 2)

    # 可以将列表链接成单个字符串，且每个元素分割方式为‘，’
    hobbies = ['basketball', 'football', 'swimming']
    print("My hobbies are:" + ",".join(hobbies))

    # 统计元音
    print(count_vowels('foobar'))
    print(count_vowels('gym'))

    # 展开为单个列表
    print(deep_flatten([1, [2], [[3], 4], 5]))

    # 返回独有元素
    print(Difference([1, 2, 3], [1, 2, 4]))

    # 在一行内调用多个函数
    a, b = 4, 5
    print((subtract if a > b else add)(a, b))

    # 检查重复项，有重复项返回True
    x = [1, 2, 3, 4, 5]
    y = [1, 2, 2, 3, 4]
    print(has_duplicates(x))
    print(has_duplicates(y))

    # 合并字典
    a = {'x': 1, 'y': 2}
    b = {'y': 3, 'z': 4}
    print(merge_dict(a, b))

    # 列表变成字典
    keys = ['a', 'b', 'c']
    values = [3, 4, 5]
    print(to_dict(keys, values))

    # 枚举列表的索引和值
    lst = ['a', 'b', 'c', 'd']
    for index, element in enumerate(lst):
        print(index, element)

    # 计算程序所用时间,time.clock将在3.8被移出
    start_time = time.perf_counter()
    sum = 0
    for i in range(100):
        sum += i
    end_time = time.perf_counter()
    cost_time = end_time - start_time
    print(cost_time)

    # 最常见元素
    lst = [1, 2, 3, 3, 4, 4, 4]
    print(most_frequent(lst))

    # 不使用条件语句实现加减乘除，利用字典
    action = {
        '+': operator.add,
        '-': operator.sub,
        '/': operator.truediv,
        '*': operator.mul,
        '**': pow
    }
    print(action['-'](50, 25))

    # 交换值
    a, b = -1, 14
    print(swap(a, b))