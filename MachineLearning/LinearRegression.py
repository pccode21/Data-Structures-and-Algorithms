import numpy as np


# 计算代价函数
def computerCost(X, y, theta):
    m = len(y)
    J = 0
    J = (np.transpose(X * theta - y)) * (X * theta - y) / (2 * m)  # 都转换成列向量
    return J
