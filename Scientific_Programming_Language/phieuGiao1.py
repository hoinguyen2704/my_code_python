n = int(input("số lượng: "))
dict_product = {}
for i in range(n):
    maHang = input(f"mã hàng hóa {i + 1}: ")
    while maHang in dict_product:
        maHang = input(f"mã hàng đã tồn tại, yêu cầu nhập lại: ")
    soLuong = int(input("số lượng trong kho: "))
    dict_product.update({maHang: soLuong})
print(f"dict sản phẩm: {dict_product}")

m = int(input("số lượng nhà cung cấp: "))
dict_supplier = {}
for i in range(m):
    maNCC = input(f"mã nhà cung cấp {i + 1}: ")
    tenNCC = input(f"tên nhà cung cấp {i + 1}: ")
    dict_supplier[maNCC] = tenNCC
print(f"dict nhà cung cấp: {dict_supplier}")
print()# xuống dòng

if "H001" in dict_product:
    dict_product.update({"H001":200})
else:
    dict_product.update({"H001":int(input("dữ liệu không có\nNhập số lượng hàng hóa H001: "))})

print(f"dict sản phẩm sau khi update H001: {dict_product}")

dict_product = {key: value for key,value in dict_product.items() if value!= 0} #loại bỏ các phần tử có values =0
print(f"dict sản phẩm sau khi update value =0: {dict_product}")

list_key_product = (list(dict_product.keys())) #tách key thành list
list_value_product = (list(dict_product.values())) #tách value thành list
print(f"list keys: {list_key_product}")
print(f"list values: {list_value_product}")