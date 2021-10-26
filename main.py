import psutil, datetime
#process and system utilities

def cpu():
    print("CPU cores count: ",psutil.cpu_count())
    for i in range(3):
        print("CPU utilization [%]: ",psutil.cpu_percent(interval=1))
    
def memory():
    mem = psutil.virtual_memory()
    print("Memory used [%]: ",mem.percent)
    print("Memory available [%]: ",100-mem.percent)

def disks():
    d = psutil.disk_usage('/')
    print("Disk 1 used [%]: ",d.percent)

def network():
    net = psutil.net_io_counters(pernic=True)
    print("Nerwork data:\n",net)

def users():
    info = psutil.users()
    print("User name: ",info[0].name)
    boot = psutil.boot_time()
    print("Boot time: ",boot)
    formated = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
    print(formated)

if __name__ == '__main__':
    #while(True):
        cpu()
        memory()
        disks()
        network()
        users()
