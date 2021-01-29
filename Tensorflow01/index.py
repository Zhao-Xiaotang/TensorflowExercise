"""  Tensorflow入门实战  """

"""
    NumPy : Numeric Python
    介绍：NumPy是一种高效的科学计算函数库，提供了数组和矩阵的常用操作。
"""


import numpy as np

# array([列表/元组]) 创建数组
"""
    numpy要求数组中的所有元素必须是同一个类型
    数组常用属性：ndim     数组的维数
               shape    数组的大小
               size     数组元素个数
               dtype    数组中元素的类型
               itemsize 数组中每个元素的字节数

    创建特殊数组： np.arange(start=0, stop, step, dtype)     创建数字序列数组
                np.ones(shape, dtype)                     创建全1数组
                np.zeros(shape, dtype)                    创建全0数组
                np.eye(shape)                             创建单位矩阵
                np.linspace(start, stop, num)             创建等差数列
                np.logspace(start, stop, num, base)       创建等比数列
    
"""
a = np.array([0, 1, 2, 3], dtype=np.int64)
print(type(a))
print(a.shape)  # 返回一个元组，显示大小为4

b = np.eye(3)
print(b)


"""  
    数组运算：1、可以使用切片的方式访问数组。
            2、np.reshape(shape)     不改变当前数组，安装shape创建新数组
            3、np.resize(shape)      改变当前数组，按照shape创建数组  
                注意：两种修改形状都要保证前后元素数量相等，设置为shape为-1时，代表自行计算
            4、numpy支持数组之间的四则运算，幂运算等，数据类型不同时，会自动转换为精度更高的类型
    
    数组对象的矩阵运算：1、* 矩阵乘法
                    2、np.transpose() 求转置
                    3、np.linalg.inv() 求逆
            
    其他运算：1、sum(矩阵，,axis)  对数组中的元素求和，axis为轴
            2、prod()           计算所有元素的乘积
            3、diff()           计算数组相邻元素之间的差
            4、sqrt()           计算各元素的平方根
            5、exp()            计算各元素的指数值
            6、abs()            取各元素的绝对值
            
    特殊运算：1、stack()      矩阵的堆叠        
    
            
            
"""

c = np.array([[0,1,2,3],
              [4,5,6,7],
              [9,10,11,12]])
print(c[0:2, 0:2])  # 截取结果为0，1，4，5
print(c[0:2, 0:2].shape)  # 返回的结果是一个（2，2）数组
# print(c.reshape(4,4))  # 报错，不能随便改

print(c.transpose())  # 求转置


# 矩阵的堆叠
a = np.array([1,2,3,4])
b = np.array([5,6,7,8])

print(np.stack((a,b),axis=0))
print(np.stack((a,b),axis=1))

"""
    Numpy中的矩阵对象:
    np.matrix(字符串/列表/元组/数组)， 可简写为mat
    矩阵运算：1、*    相乘
            2、.T   转置
            3、.I   求逆
"""
a = np.mat('1,2,3 ; 4,5,6')
print(a)  # 结果正确

m = np.mat([[1, 2, 3],[4, 5, 6]])
n = np.array([[1, 2, 3],[4, 5, 6]])

print(type(m))  # 类型为matrix
print(type(n))  # 类型为ndarray

print(m.T)  # 转置
print(m.I)  # 求逆

"""
    numpy.random                        随机数模块
    np.random.rand()                    在[0,1)均匀分布的数组
    np.random.uniform(low,high,size)    在[0,1)区间均匀分布的数组，浮点数
    np.random.randint(low,high,size)    在[0,1)区间均匀分布的数组，整数
    np.random.randn()                   产生标准正太分布的数组
    np.random.normal(loc,scale,size)    产生正态分布的数组
    
    np.random.shuffle(序列)              洗牌函数，打乱数组，防止过拟合
"""

print(np.random.randint(2,3, (3,3)))

arr = np.arange(10)
print(arr)

np.random.shuffle(arr)  # 每次执行都会再次打乱
print(arr)

