import os
import re

def find_sub(pathdir, find_word, replace_word): 
    for filep in os.scandir(pathdir):
        if filep.is_dir():
            if len(os.listdir(filep.path)) == 0: # empty folder
                continue
            else:
                find_sub(filep.path+'/', find_word, replace_word)
        else:
    # FOR PERSONAL USE elif os.path.splitext(filep.path)[1] == '.html' or os.path.splitext(filep.path)[1] == '.css' or os.path.splitext(filep.path)[1] == '':
            with open(filep.path, 'r+') as f:
                text = f.read()
                while re.findall(find_word, text): # while find_word is present, continue to modify the file
                    text = re.sub(find_word, replace_word, text)
                f.seek(0)
                f.write(text)

path = input("path to the folder -> ")
if path[len(path)-1] != '/':
    path += '/'
find_word = input("insert the word/phrase that will be modified -> ")
replace_word = input("insert the replace word/phrase -> ")
# print(path)
# filepath = os.scandir(path+'/')
find_sub(path, find_word, replace_word)


