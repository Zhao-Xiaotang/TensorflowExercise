"""  Tensorflow入门实战  """

"""
    Matplotlib绘图基础：绘制图表的第三方库，可以快速、方便的生成高质量的图标
    特点：1、使用figure对象进行绘图，相当于画布
         2、figure可以划分子图，使用subplot
"""

import matplotlib.pyplot as plt
import numpy as np


"""
    figure对象：figure(num, figsize, dpi, facecolor, edgecolor, frameon)
    num：图形编号或名称，取值为数字/字符串
    figsize：绘图对象的宽和高，单位为英寸
    dpi：绘图对象的分辨率，缺省值为80
    facecolor：背景颜色
    edgecolor：边框颜色
    frameon：是否显示边框
    
    划分子图：subplot(行数,列数,子图序号)
        当三个参数都小于10的时候，可以省略逗号,如plt.subplot(221)
        前两个参数只是划分，并没有创建子图
        
"""

def pyplotExercise():
    fig = plt.figure()

    plt.subplot(221)
    plt.title('子标题1')
    plt.subplot(222)
    plt.title('子标题2', loc='left', color='b')
    plt.subplot(223)
    plt.title('子标题3', fontsize=12, rotation=30)

    # 添加文字
    plt.rcParams['font.sans-serif'] = 'SimHei'
    # plt.rcdefaults() 恢复默认设置
    plt.suptitle('这是全局标题', fontsize=15, color='red', backgroundcolor='yellow')

    plt.tight_layout()  # 自动调整子图布局，防止重叠，可设置rect=[left, bottom, right, top] 调整子图范围
    plt.show()
    pass

def plotScatter():
    # 绘制散点图 scatter(x, y, scale 数据点大小, color 颜色, marker 样式, label 图例文字)
    plt.rcParams['font.sans-serif']="SimHei"  # 设置文字为汉字，黑体
    plt.rcParams['axes.unicode_minus'] = 'false'  # 防止负号显示错误

    # 生成数据
    n = 1024
    x = np.random.normal(0,1,n)
    y = np.random.normal(0,1,n)

    # 若想增加数据，再加上即可
    x2 = np.random.uniform(-4,4,(1,n))
    y2 = np.random.uniform(-4,4,(1,n))

    # 绘制散点图
    plt.scatter(x, y, color='blue', marker='*', label='正态分布')
    plt.scatter(x2, y2, color='yellow', marker='o', label='均匀分布')

    """
        text(x,y,fontsize, color) 在图片上增加文字
        坐标轴设置：1、xlabel(x,y,s,fontsize,color)  设置x轴标签
                  2、ylabel(x,y,s,fontsize,color)  设置y轴标签
                  3、xlim(xmin,xmax)               设置x轴坐标范围
                  4、ylim(ymin,ymax)               设置x轴坐标范围
                  5、tick_params(labelsize)        设置刻度文字的字号
    """
    # plt.text(2.5, 2.5, '均 值：0\n标准差：1')

    # 设置x、y轴范围
    plt.xlim(-4,4)
    plt.ylim(-4, 4)

    # 设置x、y轴标签
    plt.xlabel('横坐标x', fontsize=14)
    plt.ylabel('纵坐标x', fontsize=14)

    plt.legend()  # 显示图例
    plt.title('标准正态分布', fontsize=15)
    plt.show()

    pass

def plotLineChart():
    # 绘制折线图 plot(x, y, color, marker, label, linewidth 折现宽度, markersize 数据点大小)
    plt.rcParams['font.sans-serif'] = "SimHei"  # 设置文字为汉字，黑体
    plt.rcParams['axes.unicode_minus'] = 'false'  # 防止负号显示错误

    # 生成数据
    n = 24
    y1 = np.random.randint(27, 37, n)
    y2 = np.random.randint(40 ,60, n)

    plt.plot(y1, label='温度')
    plt.plot(y2, label='湿度')

    plt.xlim(0,23)
    plt.ylim(20,70)
    plt.xlabel('小时',fontsize=12)
    plt.ylabel('测量值', fontsize=12)

    plt.title('24小时温度/湿度统计',fontsize=16)

    plt.legend()
    plt.show()
    pass

def plotBarChart():
    # 绘制柱形图 bar(left x序列, height y序列, width 柱形宽度, facecolor, edgecolor, label)
    plt.rcParams['font.sans-serif'] = "SimHei"  # 设置文字为汉字，黑体
    plt.rcParams['axes.unicode_minus'] = 'false'  # 防止负号显示错误

    # 数据
    y1 = [32,25,16,30,24,45,40,33,28,17,24,20]
    y2 = [-23,-35,-26,-35,-45,-43,-35,-32,-23,-17,-22,-28]

    plt.bar(range(len(y1)), y1, width=0.8, facecolor='green', edgecolor='white',label='统计量1')
    plt.bar(range(len(y2)), y2, width=0.8, facecolor='red', edgecolor='white', label='统计量2')

    plt.title('柱状图', fontsize=20)

    plt.legend()
    plt.show()
    pass

# pyplotExercise()
# plotScatter()
# plotLineChart()
# plotBarChart()