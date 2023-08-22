# -*- coding:utf-8 -*-
import math
def simpr(f, a, b, n):

    h = (b - a) / (2 * n)
    s1 = 0
    s2 = 0
    for k in range(1,n+1):
        x = a + h * (2 * k -1)
        s1 = s1 + f(x)
    for k in range(1,n):
        x = a + h * 2 * k
        s2 = s2 + f(x)
        s = h * (f(a) + f(b) + 4 * s1 + 2 * s2) / 3
        return s

def f(g):

    return math.exp(g) + 10*g - 1

if __name__ == '__main__':
    a = 0.0
    b = 1.0
    n = 5
    sum = simpr(f,a, b, n)
    print ("用复合simpson公式求得积分值为：",sum)

    print ("精确的积分值为：", 3+math.e)
