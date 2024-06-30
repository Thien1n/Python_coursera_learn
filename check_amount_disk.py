import shutil
import psutil

# Lấy danh sách tất cả các ổ đĩa
partitions = psutil.disk_partitions()

# Duyệt qua danh sách và in ra thông tin về từng ổ đĩa
for partition in partitions:
    device = partition.device #disk_name
    mountpoint = partition.mountpoint
    fstype = partition.fstype #disk_type (ntfs,fat32,..)
    opts = partition.opts
    
    # Lấy dung lượng ổ đĩa
    disk_usage = shutil.disk_usage(mountpoint)
    total = disk_usage.total
    used = disk_usage.used
    free = disk_usage.free
    disk_percent = free/total*100
    free_percent = int(disk_percent)
    
    
    
    print(f"Device: {device}")
    print(f"Mount Point: {mountpoint}")
    print(f"File System Type: {fstype}")
    print(f"Options: {opts}")
    print(f"Total Size: {total/1024**3:.2f} GB")
    print(f"Used: {used/1024**3:.2f} GB")
    print(f"Free: {free/1024**3:.2f} GB")
    print('%Free: ', free_percent,'%')

    # In cảnh báo
    if free_percent > 70:
        print('O dia ',device, 'sap day')
        #neu o dia co dung luong dang su dung nhieu hon 70% tuc la o dia sắp đầy
    
    print()
