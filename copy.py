import shutil
import os
srcs = open('allfiles.txt',"r")
indx = 0
for file in srcs.readlines():
    path = file.replace('\n', '')
    indx += 1
    filename = path.split('\\')[-1]
    print()
    if indx < 1011:
        try:
            shutil.copy(path,f"backup/{filename}")
        except:
            print('error')