import numpy as np


# e为误差
def Jacobi(A, b, x, e, times=100):
    length, width = np.shape(A)
    D = np.mat(np.diag(np.diag(A)))
    L = np.triu(A, 1)
    U = np.tril(A, -1)
    J = -D.I * (L + U)
    H = np.eye(length) - D.I * A
    eig, _ = np.linalg.eig(H)
    spectral_radius = max(abs(eig))
    if spectral_radius < 1:
        print('此方程组收敛,谱半径为', round(spectral_radius, 5))

        x0 = x
        x = J * x + D.I * b
        # x = D.I*(b-(L+U)*x0)
        k = 1
        while k < times:
            if abs(np.max(abs(x - x0), axis=0)) > e:
                x0 = x
                x = J * x + D.I * b
                # x=D.I*(b-(L+U)*x0)
                k += 1
            else:
                print('当精度为', e, '时,Jacobi在%d次内收敛' % k)
                break
        print('Jacobi迭代解为\n', x)


B = np.mat([[1,-1,-2], [-1,10,-2], [-1,-1,5]])
b = np.mat('72;83;42')
x = np.mat('0;0;0')
e = 0.001
times = 100
Jacobi(B, b, x, e, times)
#课本p275 例12.8.1