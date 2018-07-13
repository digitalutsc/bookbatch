# case sensitive
import sys, os, shutil, glob

src = "/home/test/Desktop/book/GG-098"

# Get the listing of the folder in the natural sort order
file_list = os.system("ls -v " + src + " > temp.txt")

# Put the output of the command into a list
hdl = open("temp.txt", 'r')
file_list = hdl.readlines()
hdl.close()
os.remove("temp.txt")

for item in file_list:
    item = item.rstrip()
    print item



