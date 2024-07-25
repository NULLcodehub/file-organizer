import os
import sys
import shutil
from dictinary import dictionary_list as dl

myList=dl("data.txt")


def list_file(path):
    # files_list=os.listdir(path)
    # print(files_list)
    # extention_files=[file for file in files_list if os.path.isfile(files_list)]
    # print(extention_files)
    
    file_list=[]
    for item in os.listdir(path):
        item_path=os.path.join(path,item)
        
        if os.path.isfile(item_path):
            myList.append(item)
    
    
    
    # for file in files_list:
    #     myList.append(file)
            
    # print(files_list)
    myList.print_data()
   
    
def main():
    files_path= sys.argv[1]
    
    list_file(files_path)
    


if __name__ =="__main__":
    main()