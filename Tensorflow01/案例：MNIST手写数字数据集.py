"""
    MNIST手写数字数据集：28*28的灰度图像，存储在28*28的二维数组中
"""

import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

mnist = tf.keras.datasets.mnist
(train_x,train_y), (test_x, test_y) = mnist.load_data()

print("训练集：",len(train_x))
print("测试集：",len(test_x))

# 显示图像
fig = plt.figure('随机显示四个数字', (12,12))
for i in range(4):
    num = np.random.randint(1,60000)
    plt.subplot(1,4,i+1)
    plt.axis('off')
    plt.imshow(train_x[num], cmap='gray')  # cmap是设置色彩模式
    plt.title(train_y[num])

plt.show()