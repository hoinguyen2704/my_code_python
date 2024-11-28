from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import math
import random as rand
import math
x= np.linspace(start=-10, stop= 10, num=10, endpoint=True)
y= np.random.random(10)*100

font = {'family': 'segoe UI', 'color': 'green','size':20}
plt.scatter(x, y, color ='red', marker ='o', s=y*10, alpha=0.9)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Random Points')
plt.grid(axis='y', color='green',)
plt.show()
