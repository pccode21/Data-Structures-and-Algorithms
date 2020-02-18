import numpy as np


# 计算代价函数
def computerCost(X, y, theta):
    m = len(y)
    J = 0
    J = (np.transpose(X * theta - y)) * (X * theta - y) / (2 * m)  # 计算代价J，np.transpose都转换成列向量
    return J


# 梯度下降算法
def gradientDescent(X, y, theta, alpha, num_iters):  # num_iters 表示迭代次数
    """
    迭代是重复反馈过程的活动，其目的通常是为了逼近所需目标或结果。
    每一次对过程的重复称为一次“迭代”，而每一次迭代得到的结果会作为下一次迭代的初始值。
    alpha(α)为学习速率，控制梯度下降的速度，一般取0.01,0.03,0.1,0.3.....
    """
    m = len(y)
    n = len(theta)
    temp = np.matrix(np.zeros((n, num_iters)))  # 暂存每次迭代计算的theta，转化为矩阵形式
    # np.zeros((n,num_iters)) 返回 n 行 num_iters 列，并用 0 填充的新数组
    J_history = np.zeros((num_iters, 1))  # 记录每次迭代计算的代价值
    for i in range(num_iters):  # 遍历迭代次数
        h = np.dot(X, theta)  # 计算内积，matrix（矩阵）可以直接乘
        temp[:, i] = theta - ((alpha/m) * (np.dot(np.transpose(X), h - y)))  # 梯度的计算
        # 数组切片 [:,i] 逗号“,”分隔各个维度，“:”表示各个维度内的切片，只有:表示取这个维度的全部值
        # [:,i] 取所有行的第i列数据
        theta = temp[:, i]
        J_history[i] = computerCost(X, y, theta)  # 调用计算代价函数
        print('.', end=' ')
    return theta, J_history
