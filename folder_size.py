import os

# folder whose size is to be calculated
print("Enter folder path")
path = os.path.abspath(input())
total=0
for folder, subfolders, files in os.walk(path):
    for file in files:
        total += os.stat(os.path.join( folder,file  )).st_size
    
print(str(total)+' bytes')
