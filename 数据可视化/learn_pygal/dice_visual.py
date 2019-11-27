import pygal
from learn_pygal.die import Die
# 让骰子不停翻转，然后把结果放在一个列表中打印出来

die1 = Die()
die2 = Die(10)
result = []

# 翻转一百次
for i in range(1000):
    max_num = die1.roll() + die2.roll()
    result.append(max_num)

# 打印
# print(result)

# 计算每个面出现的次数，存放在列表中
count_result = []

max_numsize = die1.num_sizes + die2.num_sizes
for value in range(2, max_numsize + 1):
    count = result.count(value)
    count_result.append(count)

# print(count_result)

# 开始绘制直方图
hist = pygal.Bar()

hist.title = "The Result of Rolling D6+D6 1000 Times"
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6+D10', count_result)
hist.render_to_file('dice_visual.svg')