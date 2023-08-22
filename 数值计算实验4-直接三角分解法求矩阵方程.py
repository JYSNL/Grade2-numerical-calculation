#课本p273 例12.8.11
import numpy as np


def matrix_deal(matrix):
    lens = len(matrix)
    # 创建两个全零的矩阵，大小与待求解矩阵相同
    matrix_l = np.zeros((lens,lens),dtype=float)
    matrix_u = np.zeros((lens,lens),dtype=float)
    # 将左矩阵对角线元素变为1 将右矩阵首行元素赋值 左矩阵首列赋值
    for i in range(lens):
        matrix_l[i][i] = 1
        matrix_u[0][i] = matrix[0][i]
        matrix_l[i][0] = matrix[i][0]/matrix_u[0][0]
    for i in range(1,lens):
        # 对右矩阵的第i行进行赋值
        matrix_u[i,i:] = matrix[i, i:] - np.sum(matrix_l[i, :i].reshape(i,1) * matrix_u[:i, i:], axis=0)
        # 对左矩阵的第i列进行赋值
        if i == lens-1 :
            continue
        matrix_l[i+1:,i] = (matrix[i+1:,i]-np.sum(matrix_l[i+1:,:i] * matrix_u[:i,i].reshape(1,i),axis=0))/matrix_u[i][i]
    # 返回左右矩阵
    return matrix_l,matrix_u


# 计算线性方程组的解
def answer(matrix_l,matrix_u,matrix_an):
    # 对 L * y = B 的解
    matrix_l = np.hstack([matrix_l,matrix_an])
    m,n = matrix_l.shape
    for i in range(n-1):
        matrix_l[i+1:,:] = matrix_l[i+1:,:]-matrix_l[i]*matrix_l[i+1:,i].reshape(m-i-1,1)
    # 对 U * x = y 的解
    matrix_an = matrix_l[:,-1].reshape(m,1)
    matrix_u = np.hstack([matrix_u,matrix_an])
    for i in range(m-1):
        i = m-i-1
        matrix_u[:i,:] = matrix_u[:i,:] - matrix_u[i]*matrix_u[:i,i].reshape(i,1)/matrix_u[i][i]
    for i in range(m):
        matrix_u[i][-1] = matrix_u[i][-1]/matrix_u[i][i]
        matrix_u[i][i] = 1
    return matrix_u[:,-1].reshape(m,1)


if __name__ == '__main__':
    # 系数矩阵
    matrix_a = np.array([2,2,3,-2,4,-3,-2,-1,1],dtype=float).reshape(3,3)
    # 解
    matrix_b = np.array([5,7,-7],dtype=float).reshape(3,1)
    print('原增广矩阵为:')
    print(np.hstack([matrix_a,matrix_b]))
    matrix_l,matrix_u = matrix_deal(matrix_a)
    matrix_an = answer(matrix_l,matrix_u,matrix_b)
    print('L为:')
    print(matrix_l)
    print('U为:')
    print(matrix_u)
    print('解集为:')
    print(matrix_an)



