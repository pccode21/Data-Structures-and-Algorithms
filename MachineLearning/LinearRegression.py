import numpy as np
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties
import os

os.chdir(r'.\Data-Structures-and-Algorithms\MachineLearning')  # 创建工作路径
font = FontProperties(fname=r'c:\windows\fonts\simsun.ttc', size=14)  # 解决windows环境下画图汉字乱码问题


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


# 归一化feature
def featureNormaliza(X):
    X_norm = np.array(X)  # 将 X(列表)转化为numpy数组对象，才可以进行矩阵的运算
    # 定义所需变量
    mu = np.zeros((1, X.shape[1]))  # X.shape[1]表示读取X的第二维度的长度,也就是列的长度
    sigma = np.zeros((1, X.shape[1]))
    mu = np.mean(X_norm, 0)  # 求每一列的平均值（0指定为列，1代表行）
    sigma = np.std(X_norm, 0)  # 求每一列的标准差（0指定为列，1代表行）
    """
    简单来说，标准差是一组数值自平均值分散开来的程度的一种测量观念。
    一个较大的标准差，代表大部分的数值和其平均值之间差异较大；
    一个较小的标准差，代表这些数值较接近平均值
    """
    for i in range(X.shape[1]):  # 遍历列
        X_norm[:, i] = (X_norm[:, i] - mu[i]) / sigma[i]  # 归一化
    return X_norm, mu, sigma


# 加载txt和csv文件
def loadtxtAndcsv_data(fileName, split, dataType):
    return np.loadtxt(fileName, delimiter=split, dtype=dataType)


# 画每次迭代代价的变化图
def plotJ(J_history, num_iters):  # J_history是迭代值，num_iters是迭代次数
    x = np.arange(1, num_iters+1)
    # numpy.arange（[ start，] stop，[ step，] dtype = None ）返回给定间隔内的均匀间隔的值
    # 返回的是数组
    # 间隔的开始。间隔包括该值。默认起始值​​为0
    # 间隔结束，该间隔不包括该值
    plt.plot(x, J_history)
    plt.xlabel('迭代次数', fontproperties=font)  # 注意指定字体，要不然出现乱码问题
    plt.ylabel('代价值', fontproperties=font)
    plt.title('代价随迭代次数的变化', fontproperties=font)
    plt.show()


# 画二维图，看一下归一化效果
def plot_X1_X2(X):
    plt.scatter(X[:, 0], X[:, 1])  # 画散点图，X轴表示data.csv中第一列的归一化值，Y轴表示data.csv中第二列的归一化值
    plt.show()


def linearRegression(alpha=0.03, num_iters=800):
    print('加载数据...\n')
    data = loadtxtAndcsv_data('data.csv', ',', np.float64)  # 读取数据
    # Python的浮点数通常是64位浮点数，几乎等同于
    # 64位浮点数提供了更大但不精确的可能值范围
    X = data[:, 0:-1]  # X对应0到倒数第2列
    print(np.array(X), type(np.array(X)), X.shape[1])
    print(np.mean(np.array(X), 0))  # 输出每一列的平均值
    print(np.std(np.array(X), 0))  # 输出每一列的标准差
    y = data[:, -1]  # y对应最后一列
    m = len(y)  # 总的数据条数
    col = data.shape[1]  # data的列数
    X, mu, sigma = featureNormaliza(X)  # 归一化
    plot_X1_X2(X)  # 画二维散点图看一下归一化效果
    X = np.hstack((np.ones((m, 1)), X))  # 在X前加一列 1
    # numpy.hstack（tup ）水平（按列）顺序堆叠数组
    # np.ones((m, 1))返回给定形状和类型的新数组，表示填充m行一列 1
    print('\n执行梯度下降算法....\n')
    theta = np.zeros((3, 1))
    print(y)
    y = y.reshape(-1, 1)   # 将行向量转化为列，表示任意行 1列
    # reshape（行，列）可以根据指定的数值将数据转换为特定的行数和列数，这个好理解，就是转换成矩阵。
    # 跟进numpy库官网的介绍，这里的-1被理解为unspecified value，意思是未指定为给定的
    # -1在这里应该可以理解为一个正整数通配符，它代替任何整数。随机分配数据
    print(y)
    theta, J_history = gradientDescent(X, y, theta, alpha, num_iters)
    plotJ(J_history, num_iters)
    return mu, sigma, theta   # 返回均值mu,标准差sigma,和学习的结果theta


# 测试学习效果（预测）
def predict(mu, sigma, theta):
    result = 0
    # 注意归一化
    predict = np.array([2001, 3])
    norm_predict = (predict-mu) / sigma
    final_predict = np.hstack((np.ones((1)), norm_predict))  # 在 norm_predict 前加一列 1
    # numpy.hstack（tup ）水平（按列）顺序堆叠数组
    # np.ones((1))返回给定形状和类型的新数组，表示填充一列 1
    print(norm_predict)
    print(final_predict)
    result = np.dot(final_predict, theta)  # 预测结果
    return result


# 测试linearRegression函数
def testLinearRegression():
    mu, sigma, theta = linearRegression(0.03, 800)
    print("\n计算的theta值为：\n", theta)
    print("\n预测结果为：%f" % predict(mu, sigma, theta))


if __name__ == '__main__':
    testLinearRegression()
