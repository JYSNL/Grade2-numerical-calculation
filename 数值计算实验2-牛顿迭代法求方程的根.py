#课本p268 例12.8.3
import math
def f1(n):
    return (n*n-n-1)/(2*n-1)
def f2(n):
    if abs(n*n-n-1)<1e-8:
        return 1
    else:
        return 0
x = 2
count = 1
n = 100
x1 = x - f1(x)
while(abs(x-x1)>1e-8 and n!=0):
    x = x1
    x1 = x - f1(x)
    print('迭代第' + str(count) + '次,','x=',str(x1))
    count+=1
    n-=1
if n==0:
    print('迭代失败！')
