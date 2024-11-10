from zmq import NULL


a = set({'2022605434', '715201079', 'BHD202', 'MEDIA201', 'ADC12'})
b= set({'2022605434', '715201079', 'AIC2', 'MEDIA'})
print(type(a))
print(a)
print(type(b))
print(b)
intersections = a.intersection(b)
if intersections is not NULL:
    print(f'sinh viên đăng ký học cả 2 môn')
    print(f'{intersections}')
else:
    print(f'không có phần tử trùng nhau')
unions = a.union(b)
print(f'danh sách tổng hợp sinh viên đăng ký ở 2 bàn\n{unions}')

differences = a.difference(b)

print(f'danh sách sinh viên đăng ký bàn 1 nhưng không đăng ký ở bàn 2\n{differences}')