file= open('text.txt','r')
data=file.read()
for x in data:
    print(x,end = "")
    time.sleep(0.001) #tạm dừng 0.001 giây