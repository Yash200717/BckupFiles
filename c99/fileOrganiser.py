
import os
import shutil

source = os.getcwd()
print(source)
list = os.listdir(source)
print(list)

for file in list:
    name,ext = os.path.splitext(file)
    ext = ext[1:]
    if os.path.exists(source + "/" + ext ) :
        src = source + "/" + file
        dst = source + "/" + ext + "/" + file
        shutil.move(src, dst)
    
    else :
        os.makedirs(source + "/" + ext)
        src = source + "/" + file
        dst = source + "/" + ext + "/" + file
        shutil.move(src, dst)
