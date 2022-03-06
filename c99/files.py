
import os
os.mkdir("folder_1")
os.getcwd()

path = r"path"
print(os.path.exists(path))

file = "file.txt"
root_ext = os.path.splitext(file)
print("Root part: ", root_ext[0], "\nExtension part: " , root_ext[1], "\n")

print(os.listdir())

import shutil
print("Before copying file:")
print(os.listdir(path))

source = r"path\file.txt"
destination = r"path\file(copy).txt"
    
shutil.copy(source,destination)

print("After copying file:")
print(os.listdir(path))

if not os.path.exists(path+r"\folder1"):
    os.mkdir(path+r"\folder_1")

destination2 = r"path\folder_1\file.txt"
shutil.move(source, destination2)

print("After moving file:")
print(os.listdir(path))
