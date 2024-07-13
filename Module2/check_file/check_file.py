import os
import datetime

# tạo file
path = 'C:/Users/Public/Readme.txt'

with open(path,'w') as file:
    file.write('welcome to my channel 3Tshare')
    
# lấy thông tin file size
# file= 'Readme.txt'
file = path
if os.path.isfile(file):
    print(os.path.isfile(file))
    print(os.path.getsize(file))
else:
    print(os.path.isfile(file))
    print("File not found")

# lấy thông tin chỉnh sửa cuối cùng mà người có thể đọc được
timestamp = os.path.getmtime(file)
last_time_edit = datetime.datetime.fromtimestamp(timestamp)
print(last_time_edit)
