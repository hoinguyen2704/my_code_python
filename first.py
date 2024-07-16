import math
def is_number(n):
    try:
        float(n)
        return True
    except ValueError:
        return False
def is_SNT(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def is_armstrong(n):
    temp = n
    sum = 0
    k=0
    while temp > 0:
        k+=1
        temp //= 10
    temp=n
    while temp>0:
        digit = temp % 10
        sum += digit ** k
        temp//=10
    return sum == n
def binary_step(x):
    if not is_number(x):
        print(f"x must be a number")
        return
    if x<0:
        return 0
    else:
        return 1

def sigmoid(x):
    if not is_number(x):
        print(f"x must be a number")
        return
    return 1/ (1+ math.e **(-x))

def Elu(x):
    if not is_number(x):
        print(f"x must be a number")
        return
    if x>=0:
        return x
    else:
        return 0.01*((math.e**(x))-1)