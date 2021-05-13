import matplotlib.pyplot as plt
import numpy as np
# * - coding: utf-8 - *-
# импорт математической библиотеки
from math import *
x_0=float(input("Введите начальное значение x"))
x_k=float(input("Введите конечное значение x"))
n_1=int(input("Введите число разбиений"))
y_0=float(input("Введите начальное значение y"))
c=float(input("Введите значение константы c"))
y2=0
y3=0
x = np.linspace(x_0, x_k, n_1)
ylist = []
lst = []
ulist = []
def du (x_0,y_0):
        return  1/(cos(x_0))-y_0*tan(x_0)
h= (x_k-x_0) /n_1
#Аналитический метод
for i in range (0,n_1):
       y3=c*cos(x_0)+sin(x_0)
       x1=x_0+h
       x_0=x1
       ylist.append(y3)
x_0=float(input("Введите начальное значение х"))
#Метод Эйлера
for i in range (0,n_1):
       y1=y_0+h*du (x_0,y_0)
       x1=x_0+h
       x_0=x1
       y_0=y1
       lst.append(y1)
y_0=float(input("Введите начальное значение y"))
x_0=float(input("Введите начальное значение х"))
for i in range (0,n_1):
        k1=h*du (x_0,y_0)
        k2=h*du (x_0+h/2,y_0+k1/2)
        k3=h*du (x_0+h/2,y_0+k2/2)
        k4=h*du (x_0+h,y_0+k3)
        y2=y_0+ (k1+2*k2+2*k3+k4) /6
        x_0=x_0+h
        y_0=y2
        ulist.append(y2)
plt.plot(x, ylist ,"g-", label="аналитический")
plt.plot(x, lst ,"b-", label="метод Эйлера")
plt.plot(x, ulist ,"r-", label="метод Рунге-Кутта 4-го порядка")
plt.legend()
plt.show()
