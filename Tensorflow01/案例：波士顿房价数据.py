"""
    keras:一个高层的神经网络和深度学习库，可以快速搭建神经网络模型，非常易于调试和扩展
    公开数据集：
    boston_housing      波士顿房价数据集
    CIFAR10             10种类别的图片集
    CIFAR100            100种类别的图片集
    MNIST               手写数字图片集
    Fashion-MNIST       10种时尚类别的图片集
    IMDB                电影点评数据集
    reuters             路透社新闻数据集
"""


import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# 加载数据集
boston_housing = tf.keras.datasets.boston_housing
(train_x, train_y),(_,_) = boston_housing.load_data(test_split=0)

# 数据集可视化
plt.figure(figsize=(12,12))
plt.rcParams['font.sans-serif']="SimHei"  # 设置文字为汉字，黑体
titles = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE',
          'DIS', 'RAD', 'TAX', 'PTRATIO', 'B-1000', 'LSTAT', 'MEDV']

for i in range(13):
    plt.subplot(4,4,(i+1))
    plt.scatter(train_x[:,i],train_y)  # 提取每个属性，与房价之间的关系
    plt.xlabel(titles[i])
    plt.ylabel('Price($1000’s)')
    plt.title(str(i+1) + '.' + titles[i] + '- Price')

plt.suptitle('各个属性与房价的关系', x=0.5, y=1.0, fontsize=20)
plt.tight_layout()
plt.show()