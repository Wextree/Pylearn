import matplotlib.pyplot as plt
x_values = list(range(1, 1001))
y_values = [i**2 for i in x_values]

# 利用scatter绘制散点图，默认是蓝色点和黑色轮廓，edgecolor是轮廓，c是颜色（可以使用RGB）
# 演示以y轴渐变，cmap表示映射，查看映射表 http://matplotlib.org/
plt.scatter(x_values, y_values, s=1, edgecolors='none', c=y_values, cmap=plt.cm.Blues)

plt.title("Square Number", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 参数which的值为 'major'、'minor'、'both'，分别代表设置主刻度线、副刻度线以及同时设置，默认值为'major'
plt.tick_params(axis='both', which='major', labelsize=14)

# 让程序自动将图标保存在文件中，第一个参数调路径和名称，第二个参数指定将图表多余的空白区域裁剪掉
# plt.savefig('squares_plot.png', bbox_inches='tight')
plt.show()