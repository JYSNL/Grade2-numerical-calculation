import numpy as np


# 高斯赛德尔迭代法
def Gauss_Seidel(n, A, B, x0, x, eps, k):
    times = 1
    while times < k:
        for i in range(n):
            temp = 0
            temps = x0.copy()
            for j in range(n):
                if i != j:
                    temp += x0[j] * A[i][j]
            x[i] = (B[i] - temp) / A[i][i]
            x0[i] = x[i].copy()
        error = max(abs(x - temps))
        times += 1
        if error < eps:
            print("精确度等于{0}时，高斯赛德尔迭代法需要迭代{1}次收敛".format(eps, times))
            return (x, times)
        else:
            x0 = x.copy()
    print("在最大迭代次数内不收敛", "最大迭代次数后的结果为", x)
    return None


def main():
    n = 3
    A = np.array([[10,-1,-2], [-1,10,-2], [-1,-1,5]])
    B = np.array([7,83,42])
    x0 = np.array([1.0, 1, 1])
    x = np.array([0.0, 0, 0])
    eps = 10 ** (-4)
    k = 100  # 最大迭代次数
    Gs = Gauss_Seidel(n, A, B, x0, x, eps, k)
    print(Gs)


if __name__ == '__main__':
    main()
