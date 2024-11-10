a = dict({'2022605434':1.4, '715201079':2.4, 'BHD202':7.4, 'MEDIA201':3.4, 'ADC12':2.8})
b= {key: value for key, value in a.items() if (value >= 2.5 and value <= 3.5) }
print(f'danh sách sinh viên có điểm [2.5, 3.5] \n{b}')
if a.get('715201121') is None:
    a['715201121'] = 8.9
    print(f'đã thêm 1 sinh viên \n{a}')
a= {key: value for key, value in a.items() if not value < 2}
print(f'danh sách sau khi xóa các hs có điểm < 2 \n{a}')