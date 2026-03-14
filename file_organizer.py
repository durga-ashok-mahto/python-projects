import os
import shutil

path = "files"

for file in os.listdir(path):
    if file.endswith(".jpg"):
        shutil.move(path+"/"+file, path+"/images/"+file)

    elif file.endswith(".txt"):
        shutil.move(path+"/"+file, path+"/text/"+file)
