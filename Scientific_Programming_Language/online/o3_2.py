import matplotlib.pyplot as plt
import numpy as np
import math
import random as rand
import math
x= np.linspace(-2*math.pi, 2*math.pi, int( (4*math.pi) / (math.pi/15)), endpoint='True' )
y= np.sin(x)

font = {'family': 'segoe UI', 'color': 'green','size':20}
plt.plot(x, y, color ='green', marker ='*', ms='10', mec ='b', mfc ='r' )
plt.xlabel('x')
plt.ylabel('y= sin(x)')
plt.title("đồ thị y= sin(x)")
plt.show()