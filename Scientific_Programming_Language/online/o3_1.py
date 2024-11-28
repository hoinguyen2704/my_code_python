import matplotlib.pyplot as plt
import numpy as np
import math
import random as rand
x= np.linspace(start=-10, stop= 10, num=10, endpoint=True)
y= np.random.random(10)*100
f_x = 3*x**3 + - 3*x**2 + 3*x -3
from turtle import color
font ={'family': 'segoe UI', 'size':20, 'color': ' green'}
plt.subplot(1,2,1)
plt.plot(x, y, color='red', ms=10)
plt.xlabel('x', loc='center')
plt.ylabel('y', loc='bottom')
plt.title("tọa độ các điểm ngẫu nhiên")
# plt.show()

plt.subplot(1,2,2)
plt.plot(x, f_x, color = 'green', marker ='o', ms= 1, mec= 'r', mfc ='g')
plt.xlabel('x', loc='center')
plt.ylabel('3*x**3 + - 3*x**2 + 3*x -3', loc='bottom')
plt.title('f(x)')
plt.autoscale(True, axis='both')
plt.show()