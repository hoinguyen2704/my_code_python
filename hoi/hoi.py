import time
password = ""
passw = ""
while passw != password:
    passw = input("enter your password: ")
    if passw != password:
        print("mật khẩu sai!!\n")
    else:
        print("****--------------------------------------------------***")

for i in range(0,109,10):
	print("just a moment...loading..." + str(i) + "%" )
	time.sleep(0.4)
print("\nbạn đã đăng nhập thành công\n")

with open("D:\\OneDrive\\Documents\\code\\python\\hoi\\text3.txt", "r") as file:
		line = file.read()

for x in line:
	print(x, end = "")
	time.sleep(0.0000001)