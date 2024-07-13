with open("readme.txt") as file:
    for line in file:
        print(line.upper())

# đọc toàn bộ nội dung file thông qua vòng lặp for đọc từng dòng (line)


with open('readme.txt') as file:
    for line in file:
        print(line.strip())

# Đọc toàn bộ nội dung file và lược bỏ qua khoảng trắng

with open('readme.txt') as file:
    lines = file.readlines()

print(lines)
print('-------------------------')
lines.sort()
print (lines)

# Đọc toàn bộ nội dung file và lưu dưới dạng list để sắp xếp theo alphabet
