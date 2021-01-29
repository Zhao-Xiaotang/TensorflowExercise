"""
    鸢尾花数据集世经典的用于分类的数据集
    Pandas库：用于数据统计、分析的，高效、方便的操作大型数据集

"""

# get_file(fname, origin, cache_dir) 自带下载文件的函数,返回值为下载文件的绝对路径

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



# 下载鸢尾花数据集
TRAIN_URL = 'http://download.tensorflow.org/data/iris_training.csv'
train_path = tf.keras.utils.get_file('iris_training.csv', TRAIN_URL)

# 读取文件 pd.read_csv(train_path, head=0, names 自定义列标题)
COLUMN_NAMES = ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Species']
df_iris=pd.read_csv(train_path, names=COLUMN_NAMES, header=0)
print(type(df_iris))  # 结果为dataframe类型

"""
    Pandas二维数据基本操作：
    DataFrame也有 ndim、shape、size
    head(n)     读取前n行数据
    tail(n)     读取后n行数据
    describe()  显示二维数据的统计信息
    转化为Numpy  np.array(dataframe)/values/.as_matrix
       
"""

print(df_iris.head())
print(df_iris.describe())

# 转化为Numpy对象
iris = np.array(df_iris)

# 数据可视化
fig = plt.figure('Iris Data', figsize=(15, 3))
plt.suptitle('Anderson\'s Iris Data Set')
for i in range(4):
    plt.subplot(1,4,i+1)
    if i == 0:
        plt.text(0.3,0.5,COLUMN_NAMES[0], fontsize=15)
    else:
        plt.scatter(iris[:,i], iris[:,0], c=iris[:,4], cmap='brg')

    plt.xlabel(COLUMN_NAMES[i])
    plt.ylabel(COLUMN_NAMES[0])

plt.tight_layout(rect=[0,0,1,0.9])
plt.show()