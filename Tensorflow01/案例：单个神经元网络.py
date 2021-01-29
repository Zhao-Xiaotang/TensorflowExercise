"""  构建一个神经元的网络  """

# import tensorflow as tf
from tensorflow import keras
import numpy as np

#  构建模型
model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')

# 导入数据
xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)

# 拟合模型 500次迭代
model.fit(xs, ys, epochs=500)

# 预测
print(model.predict([10.0]))
