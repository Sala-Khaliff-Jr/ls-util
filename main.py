# Purpose : To List Directories
# Author : Sala Khaliff
# Date : 13-MAY-21
import os

def ls():
    '''
    Accepts no arguments, simply lists the contents in current directory
    '''
    files_list = os.listdir('.')
    return sorted(files_list)

if __name__ == '__main__':
    files_list = ls()
    for file_names in files_list:
        print(file_names)
