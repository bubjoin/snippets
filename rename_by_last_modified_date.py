# Rename by adding number to each name of files and dirs 
# sorted by last modified date in a dir
# 20220109 Arranging and archiving memos and docs
# after studying to deploy a website on Ubuntu PC

import os

dir_name = input('Please input the absolute dir with / at the end : ')

files_and_dirs = os.listdir(dir_name)

files_and_dirs = sorted( files_and_dirs, key = \ 
        lambda x : os.path.getmtime(os.path.join(dir_name, x)))

print(files_and_dirs)

num = 0

for name in files_and_dirs:
    new_name = f'{dir_name}{num}_{name}'
    os.rename(name, new_name)
    num +=1

print('Sorted and renamed')
