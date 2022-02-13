import numpy as np

def ppi(h_px, v_px, d_inch):
    return np.sqrt(np.square(h_px) + np.square(v_px)) / d_inch

def ppi_from_pixel_distance(pixel_distance):
    return 25.4 / pixel_distance

# 人眼最小的可视角度为1角分，60角分为1度
# 三角函数计算时单位为弧度
minimum_sight_angle = np.pi / 180 / 60

fixed_value = np.tan(minimum_sight_angle / 2)


def pixel_distance_from_ppi(ppi):
    return 25.4 / ppi

def pixel_distance(view_distance):
    return 2 * view_distance * 10 * fixed_value

def view_distance(pixel_distance):
    return pixel_distance / (2 * fixed_value) / 10

if __name__ == '__main__':
    # print(fixed_value)
    print('屏幕参数计算器')
    print('1 给定分辨率和对角线尺寸计算ppi')
    print('2 给定观看距离计算最佳ppi')
    print('3 给定分辨率和对角线尺寸计算最短观看距离')
    print('4 给出ppi和缩放倍率，计算实际显示大小和设计目标大小的差值\n')
    value = int(input('请输入所需的功能对应的序号\n'))
    
    match value:
        case 1:
            h_px = int(input('请输入横向像素数量：'))
            v_px = int(input('请输入纵向像素数量：'))
            d_inch = float(input('请输入屏幕对角线的长度，单位为英寸：'))
            # 变量result会自动导包
            value = ppi(h_px, v_px, d_inch)
            print('分辨率为{}x{}的{}寸屏幕，它的ppi约为{:.2f}'
            .format(h_px, v_px, d_inch, value))
        case 2:
            distance = float(input('请输入观看距离，单位为厘米：'))
            value = ppi_from_pixel_distance(pixel_distance(distance))
            print('观看距离为{:.1f}厘米时，最佳ppi约为{:.2f}'.format(distance, value))
        case 3:
            h_px = int(input('请输入横向像素数量：'))
            v_px = int(input('请输入纵向像素数量：'))
            d_inch = float(input('请输入屏幕对角线的长度，单位为英寸：'))
            ppi_value = ppi(h_px, v_px, d_inch)
            value = view_distance(pixel_distance_from_ppi(ppi_value))
            print('分辨率为{}x{}的{}寸屏幕，最短（近）观看距离约为{:.2f}厘米'
            .format(h_px, v_px, d_inch, value))
        case 4:
            physical_ppi = int(input('请输入屏幕的物理ppi：'))
            scaling_factor = int(input('请输入缩放倍率，范围为100以上的整数，例如150%的缩放倍率就填150：'))
            value = 96 * scaling_factor / physical_ppi
            print('ppi为{}的屏幕，windows下缩放倍率为{}%时，UI的实际显示大小相当于目标大小的{:.2f}%'
            .format(physical_ppi, scaling_factor, value))
            pass
        case _:
            print('输入的序号有误')