import os
import sys
import shutil


def list_file(path):
    files_list=os.listdir(path)
    extention_list=[]
    
    for exe in files_list:
        if exe.split('.')[1] not in extention_list:
            extention_list.append(exe.split('.')[1])
            
    print(files_list)
    print (extention_list)
    




# def files_list(path):
#     files_list=os.listdir(path)
    
#     jpg_files=[jpg for jpg in files_list if jpg.split(".")[1] == 'jpg']
#     png_files=[png for png in files_list if png.split('.')[1] == 'png']
#     print(jpg_files)
#     print(png_files)
    

def main():
    line = sys.argv[1]
    print(line,type(line))
    # files_list(line)
    list_file(line)

if __name__ =="__main__":
    main()