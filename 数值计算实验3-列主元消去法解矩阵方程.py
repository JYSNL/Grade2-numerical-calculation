#课本p271 例12.8.9
import numpy as np                  #本次仅需要用到这一个库
#a = input('需要计算的方程组为：')
a = np.array([[2,2,3,5],[-2,4,-3,7],[-2,-1,1,-7]])      #双括号   a即要计算的
i = a.shape[0]                       #得到a的行数
j = a.shape[1]                       #得到a的列数
print(i)
print(j)
X = []                               #建立一个X空列表，便于放入所得解
print(X)

for z in range(0, j - 2):  # 1.当z从第1列到j-1列循环，每一次循环中，都是针对所在列，先排序，后消元（以下对应这两部分） 2.z还代表循环次数
    for x in range(z, i):  # x从z行到第最后一行循环，每次循环扔掉上次循环的第一行，因为每次的第一行都用来存储每次的最大
        n = np.argmax(abs(a[x:i, z]))  # n为剩下的几行中，绝对值最大的值所在行的索引
        print(n + x)  # ***索引再加x，因为n为剩下的几行中的索引，而我们接下来的交换针对所有行
        a[[x, n + x], :] = a[[n + x, x], :]  # 数组特殊的交换数值方式，吃亏
        print(a)

    for y in range(1 + z, i):  # 之所以从1+z，开始，最开始的z循环不仅仅是列，也是循环次数，每循环一次，向下移动一列
        k = a[z, z] / a[y, z]  # 充分理解这个式子
        print(k)
        a[y,] = a[z,] - k * a[y,]
print(a)
# for w in range(j-2,-1,-1):           #这里从倒数第二列开始向前循环   列！  注意：步长默认为1，所以改成-1
w = j - 1
g = 0
for q in range(i - 1, -1, -1):  # i为矩阵行数  这里是从最后一行开始向上循环   行！
    w = w - 1
    h = 2 - q  # 注意！这里的2，在不同的方程组是不一样，这是3元，所以2

    if h == 0:
        X.append(a[q, j - 1] / a[q, w])
        print(X)
    else:
        for n in range(0, h):  # e+1决定让n循环几次
            g = g + a[q, 2 - n] * X[n]
            print(g)
        X.append((a[q, j - 1] - g) / a[q, w])  # 公式
        print(X)
        g = 0  # 很重要，容易遗漏！推一推就好
