s= 'hello '
q = 'hello world ha'
print(s in q)
p = s+ q
print(p)
p = p.replace('ha', 'ba')
print(p)
list_str= p.split()
dict_str = {key: value for key, value in zip(range(len(list_str)), list_str)}
print(dict_str)
dict_str2 = {key:value for key, value in enumerate(list_str)}
print(dict_str2)
dict_str3 = dict(map(lambda i: (i, list_str[i]), range(len(list_str)) ))
print(dict_str3)
