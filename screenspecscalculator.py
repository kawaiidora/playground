import numpy as np

def ppi(h_px, v_px, d_inch):
    return np.sqrt(np.square(h_px) + np.square(v_px)) / d_inch

# 人眼最小的可视角度为1角分，60角分为1度
# 三角函数计算时单位为弧度
minimum_sight_angle = np.pi / 180 / 60

fixed_value = np.tan(minimum_sight_angle / 2)

if __name__ == '__main__':
    print('屏幕参数计算器')
    print('1 给定分辨率和对角线尺寸计算ppi')
    print('2 给定观看距离计算最佳ppi')
    print('3 给定分辨率和对角线尺寸计算最短观看距离\n')
    print('4 给出ppi和缩放倍率，计算实际显示大小和设计目标大小的差值\n')
    
    value = int(input('请输入所需的功能对应的序号\n'))
    match value:
        case 1:
            h_px = int(input('请输入横向像素数量'))
            v_px = int(input('请输入纵向像素数量'))
            d_inch = float(input('请输入屏幕对角线的长度，单位为英寸'))
            print('分辨率为{}x{}的{}寸屏幕，它的ppi约为{:.2f}'
            .format(h_px, v_px, d_inch, ppi(h_px, v_px, d_inch)))
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case _:
            print('输入的序号有误')