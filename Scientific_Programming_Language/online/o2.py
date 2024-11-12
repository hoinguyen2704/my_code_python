import pandas as pd
import numpy as np
#1
file_path = './dataBaiO2.txt'
with open(file_path, 'r', encoding ='utf8') as f:
    n, m = list(map(int,f.readline().split()))
    a=[]
    for i in range(n):
        k= f.readline().split()
        for col in range (m):
            if k[col] != '?' :
                k[col]= float(k[col])
        a.append(k)
#/1
#2
print(f'n= {n}\tm= {m}')
# for i in range(len(a)):
#     print(f'{a[i]}')

x= [col[:-1] for col in a]
x= np.array([ [float(value) if value != '?' else np.nan for value in row] for row in x])

# for i in range(len(x)):
#     print(f'{x[i]}')
y= list(map(int,[col[-1] for col in a]))
y=np.array(y)
#/2
# for i in range(len(y)):
#     print(f'{y[i]}')
# print(type(y))
#3
key, counter = np.unique(y, return_counts=True)
dict_counter = dict(zip(key, counter))
print(f'mảng y có {len(dict_counter)} giá trị khác nhau')
for key, value in dict_counter.items():
    print(f'{key} : {value}')
#/3

#4
# avg_list =[]
# for j in range(m -1):
#     avg_list.append(sum( [col[j] for col in x if col[j] != '?']) /len(x) )
# avg_list = np.array(avg_list)
# avg_list = np.array()
avg_list = np.nanmean(x, axis =0)
avg_format = np.array(list(map(lambda x: int(x*10)/10, avg_list )))
print(f'avg_list = {avg_list}')
indexs = np.where(np.isnan(x)) # trả về 1 tuple chứa 2 mảng (số hàng, số cột)
print(indexs)
x[indexs] = avg_format[indexs[1]]
for i in range(len(x)):
    print(f'{x[i]}')

with open('out.txt', 'w',encoding='utf8') as f_out:
    # x= x.astype(list)
    f_out.write(f'n= {str(n)}\ttm= {str(m)}\n')
    for i in range(len(x)):
        f_out.write(f"{' '.join(map(str, x[i]))}\n")