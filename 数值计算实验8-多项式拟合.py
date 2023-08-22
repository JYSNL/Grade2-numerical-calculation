# coding=utf-8
import numpy as np
x=[2,4,6,8]       #自变量
y1=[2,11,28,4] #构造测试数据y1并加入随机干扰值(因变量)
print(y1)
coef=np.polyfit(x,y1,1) #按一次多项式拟合
print(coef)
yn=np.poly1d(coef)      #拟合的多项式
print(yn(x))                   #计算拟合值，和y1对比，比较接近
'''                                                                                                                                            
# coding=utf-8
import numpy as np
x=np.arange(1,21)       #自变量
y1=3*x+x+np.random.rand(20) #构造测试数据y1并加入随机干扰值(因变量)
print(y1)
coef=np.polyfit(x,y1,2) #按一次多项式拟合
print(coef)
yn=np.poly1d(coef)      #拟合的多项式
print(yn(x))                   #计算拟合值，和y1对比，比较接近'''

