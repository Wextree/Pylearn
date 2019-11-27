import matplotlib.pyplot as plt

# 利用plot绘制折线图
squres = [1, 4, 9, 16, 25]
input_values = [1, 2, 3, 4, 5]
# linewidth决定了制作的线条的粗细
plt.plot(input_values, squres, linewidth=2)

# 设置图标标题
plt.title("Square Number", fontsize=24)
# 给坐标轴加上标签
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)

plt.show()