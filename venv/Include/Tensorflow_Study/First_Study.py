import tensorflow as tf
import os
import cProfile
import numpy as np
if __name__ == '__main__':
    # 默认开启立即计算
    print(tf.executing_eagerly())
    x=[[2.]]
    m=tf.matmul(x,x)
    # 启用了eager.execution,会立即计算，返回给python，方便调试
    # 不需要构建计算图，
    # NumPy 运算接受 tf.Tensor 参数。
    # tf.math 运算会将 Python 对象和 NumPy 数组转换为 tf.Tensor 对象
    # tf.Tensor.numpy 方法会以 NumPy ndarray 的形式返回该对象的值
    print('heelo,{}'.format(m))
    a=tf.constant([
        [1,2],
        [3,4]
    ])
    print(a)
    # 广播机制
    b=tf.add(1,a)
    print(b)
    # knock乘积,元素相乘
    print(a*b)
    c=np.multiply(a,b)
    print(c)
    # 转换成numpy
    print(a.numpy())