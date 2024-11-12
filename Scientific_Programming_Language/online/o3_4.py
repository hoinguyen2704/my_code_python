from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import math
import random as rand
import math

x_bar= np.linspace(start=-10, stop= 10, num=10, endpoint=True)
y_bar= np.random.randint(0, 100, 10)
# plt.figure(figsize=(4, 4))
font = {'family': 'segoe UI', 'color': 'green','size':20}
plt.subplot(1,3,1)
plt.bar(x_bar, y_bar, color ='green', width=1.5, align='center')
plt.xlabel('x')
plt.ylabel('y')
plt.autoscale = True
plt.title('Random Bar Chart')

plt.subplot(1,3,2)
plt.hist(y_bar, bins=30, edgecolor='blue')

plt.subplot(1,3,3)
plt.pie(y_bar,autopct='%1.1f%%')
plt.show()
