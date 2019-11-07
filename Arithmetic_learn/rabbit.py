
# 记录洞口的状态，1是狐狸激怒去过，0是狐狸没有进去过
pole_status = [0,0,0,0,0,0,0,0,0,0]

# 记录狐狸现在在哪个洞口，默认一开始是10号口
pole = 10

# 设置一个循环，执行一千次，模拟狐狸进去洞口
for i in range(1,1001):
    pole = (pole-1+i) % 10
    pole_status[pole] = 1

# 通过遍历洞口的状态来看兔子藏在哪
i = 0
while True:
    if pole_status[i] == 0:
        break
    i += 1

print("兔子藏在%d号洞口" %(i+1))

s = input("输入任意键退出...")