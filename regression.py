import numpy as np
from statistics import mean
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
style.use('fivethirtyeight')

df = pd.read_csv('Book1.csv')
xs = np.array(df['DATE'])
ys = np.array(df['CASES'])

def best_fit_line(xs,ys):
    meanXY = mean(xs)*mean(ys)
    meanxy = mean(xs*ys)
    meanX2 = mean(xs)*mean(xs)
    meanx2 = mean(xs*xs)
    m1 = meanXY - meanxy
    m2 = meanX2 - meanx2
    m = m1/m2
 
    return m
m= best_fit_line(xs,ys)

def intercept(xs,ys,m):
    b=mean(ys)-m*(mean(xs))
    return b

b= intercept(xs,ys,m)
regression_line = [(m*x)+b for x in xs]

predict_x = 48
predict_y = (m*predict_x)+b
print(predict_y)


plt.scatter(predict_x,predict_y,color='g')

plt.plot(xs,ys,color='r')

plt.plot(xs,regression_line)
plt.scatter(xs,ys)
plt.show()
