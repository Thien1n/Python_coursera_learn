import psutil


# lấy thông tin CPU hiện tại
def check_cpu_percent():
    cpu_usage = psutil.cpu_percent(1)
    print('% current CPU: ',cpu_usage,'%')
    return cpu_usage < 75

# In cảnh báo CPU quá tải
if not check_cpu_percent():
    print('CPU is high')
