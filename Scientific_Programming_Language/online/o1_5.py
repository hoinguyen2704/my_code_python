from ast import Delete


dict_5 ={
    'n':1500,
    'CLUSTERS':3,
    'ITER':1000,
    'METHOD':'DCA CLUSTERING',
    'MEASURE':'ECLUDIAN',
    'YEARS':9,
    'MAX':200
}
print(f'dict ban đầu')
for key, value in dict_5.items():
    print(f'{key}: {value}')

dict_5['MEASURE'] ='MANHATAN'
print(f'\ndict sau khi chỉnh sửa')
for key, value in dict_5.items():
    print(f'{key}: {value}')

# print('giá trị của method: %s'%(dict_5.get('METHOD')))
# print('giá trị của method: {}'.format(dict_5.get('METHOD')))

print(f'\ngiá trị của method: {dict_5.get("METHOD")}')

if dict_5.get('LOSS FUNCTION') is None:
    dict_5['LOSS FUNCTION'] = 'SOFT MAX'
print(f'\ndict sau khi thêm giá trị')
for key, value in dict_5.items():
    print(f'{key}: {value}')

del dict_5['YEARS']
print(f'\ndict sau khi xóa')
for key, value in dict_5.items():
    print(f'{key}: {value}')

s= input(f'input something: ')
if s.isnumeric(): s= int(s)

if s in dict_5.values():
    print(f'\nđã tìm thấy giá trị {s} trong dict')
else:
    print(f'\nkhông tìm thấy giá trị {s} trong dict')
set_value = set(dict_5.values())
print(type(set_value))
list_value = list(dict_5.values())
print(type(list_value))
