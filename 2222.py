# -*- coding: UTF-8 -*-
#coding=utf-8

import matplotlib.pyplot as plt
import numpy as np 
# linspace 第一个参数序列起始值, 第二个参数序列结束值,第三个参数为样本数默认50
x = np.linspace(0, 3 * np.pi, 100)#在指定的间隔内返回均匀间隔的数字，0-3π之间取100个点
y = np.sin(x)#对x取正弦

plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.subplot(1,2,1)#一个FIGURE图形生成一行两列两个子图
plt.title(r'$f(x)=sin(x)$') #命名f(x)=sin(x)
plt.plot(x, y)#x为x轴数据, y为y轴数据
#plt.show()

x1 = [t*0.375*np.pi for t in x]#x1=t*0.375*np.pi
y1 = np.sin(x1)#将x1放入sinx函数求y1
plt.subplot(1,2,2)#一个FIGURE图形生成一行两列两个子图，subplot(1,2,2)后面一个2表示当前激活第二个子图。
# plt.title(u"测试2") #注意：在前面加一个u
plt.title(r'$f(x)=sin(\omega x), \omega = \frac{3}{8} \pi$') #命名两个图像的标题
plt.plot(x1, y1)#x1以x为轴，y1以y为轴
plt.show()#显示图像