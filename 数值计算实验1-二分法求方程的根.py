def func(x):
    return x**2-x-1

a=1
b=2
fa=func(a)
fb=func(b)
while a<=b:
    x0=(a+b)/2
    fx0=func(x0)
    if abs(fx0)<10e-6:
        print('x0:',x0,fx0,'<10e-6')
        print(x0,'是用二分法求解方程的根')
        break
    if fa*fx0<0:
        b=x0
        fb=fx0
        print('解在左侧,a:',a,'  b:',b,'  x0:',x0)
    elif fb*fx0<0:
        a=x0
        fa=fx0
        print('解在右侧,a:',a,'  b:',b,'  x0:',x0)



#课本p48，例3.2.2

