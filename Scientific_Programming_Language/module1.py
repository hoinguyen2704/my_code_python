import module2
def USD(n):
    return n*module2.dic.get("USD")
def EUR(n):
    return n*module2.dic.get("EUR")
def RUB(n):
    return n*module2.dic.get("RUB")
def plus(*x):
    sum=0
    for i in x:
        sum+=i
    return sum