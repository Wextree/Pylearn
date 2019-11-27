import pygal
from learn_pygal.die import Die
# 让骰子不停翻转，然后把结果放在一个列表中打印出来

die = Die()
result = []

# 翻转一百次
for i in range(1000):
    num = die.roll()
    result.append(num)

# 打印
# print(result)

# 计算每个面出现的次数，存放在列表中
count_result = []

for value in range(1, die.num_sizes + 1):
    count = result.count(value)
    count_result.append(count)

# print(count_result)

# 开始绘制直方图
hist = pygal.Bar()

hist.title = "The Result of Rolling D6 1000 Times"
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', count_result)
hist.render_to_file('die_visual.svg')