import random

path='C:/Users/Public/'

# randome tên file
random_num = round(random.random(),1)
name = 'readme'+ str(random_num) +'.txt'

# tạo file mới + sau đó ghi lần lượt
file = open(path+name,'x')
file = open(path+name,'w')
file.write('Noi dung bat ky')
file.close()

# random tên file
random_num = round(random.random(),1)
name = 'readme'+ str(random_num) +'.txt'

# tự tạo file với tham số 'w' rồi ghi luôn
name = '3Tshare'+str(random_num)+'.txt'
file = open (path+name,'w')
file.write('Hello World')
file.close()

# random tên file
random_num = round(random.random(),1)
name = 'readme'+ str(random_num) +'.txt'

# sử dụng with + r
with open(path+name,'w') as file:
    file.write('Welcome to my channel')


# chúng ta có tất cả 3 files sau khi chạy xong đoạn scrips này
