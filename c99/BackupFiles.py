import os
import shutil

source = r"C:\Users\Yashveer Singh\Desktop\python\c99"
destination = r"C:\Users\Yashveer Singh\Desktop\python\c99\folderA"

source = source + '/'
destination = destination + '/'

if not os.path.exists(destination) :
    os.mkdir(destination)

list_of_files = os.listdir(source)
for file in list_of_files:
    shutil.copy((source+file), destination)