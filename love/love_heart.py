from math import *

def main():
    text = input("请输入心的内容（英文）：")
    height = 20
    width = 60

    gh = int(height * 1.2)
    gw = int(width * 1.2)
    hh = gh // 2
    hw = gw // 2
    th = height / 4
    tw = width / 4
    output =[[' ']*gw for i in range(gh)]

    for x in range(-hw,gw-hw):
        try:
            f = round((sqrt(abs(x/tw)*2-(x/tw)**2)+1)*th)
            g = round((asin(abs(x/tw)-1)-pi/2+1)*th)
            for y in range(g, f+1):
                output[hh-y][x+hw] = text[(x-y)%len(text)]
        except ValueError:
            pass

    for x in output:
        print(''.join(x))

    hold = input("爱你~~~~")

if __name__ == '__main__':
    main()