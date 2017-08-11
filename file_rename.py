import os
def file_rename():
    files = os.listdir(r"/home/ashish/python")

    for file in files:
        os.rename(file,file.translate(None,"0123456789"))
    print files 
file_rename()
