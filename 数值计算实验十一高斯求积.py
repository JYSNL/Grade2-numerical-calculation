from scipy.special import roots_legendre
def f(x):
    return x**4-2*x+1

N = 3 #取3个样本点
a,b = 0,2 #积分上下限
x,w = roots_legendre(N)
xp = x*(b-a)/2+(b+a)/2
wp = w*(b-a)/2

s = 0
for i in range(N):
    s+=wp[i]*f(xp[i])
print(s)
