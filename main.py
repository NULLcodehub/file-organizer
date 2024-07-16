import os
import sys

def files_list(path):
    files=os.listdir(path)
    print(files)
    

def main():
    line = sys.argv[1]
    print(line,type(line))
    files_list(line)

if __name__ =="__main__":
    main()