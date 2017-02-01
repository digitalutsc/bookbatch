# case sensitive
import sys, os, shutil, glob

def batch_rename(src):
    """ src->String - string representation of the directory containing items to be renamed.

       The function works by looking at objects in the directory and seeing if they are a directory or a file. Files are renamed to OBJ.ext, while batch_rename is called again on directories. 
        
        CAREFUL this function takes all files found recursively and renames them to OBJ.whatever. No checks of file type are done"""
    for f in glob.glob(src+"/*"):
        if os.path.isdir(f):
            batch_rename(f)
        else:
            d = f[:f.rfind("/")] + "/OBJ." + f.split(".")[1]
            print f,d
            shutil.move(f,d)

def number_folders(src):
    """ src ->String - string representation of the directory containing items to be renamed.

        This function works by looking for all of the folders in the given directory. There are then in the order given, renamed to numbers 0 to X where X is the number of folders. The folder names are padded to 3 digits (ex. 002, 021, 123)
        
        CAREFUL, this function takes all folders in the given folder and renames them to a numbered sequence. There is no recursion or checking of any kind """
    count = 0
    for f in glob.glob(src+"/*"):
        if os.path.isdir(f):
            d = f[:f.rfind("/")]+"/%03d"%(count)
            print f,d
            count += 1
            shutil.move(f,d)

def copytree(src, dst, symlinks=False, ignore=None):
    if not os.path.exists(dst):
        os.makedirs(dst)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        # print s, d
        # print "JOIN", os.path.join(d, item)
        if os.path.isdir(s):
            copytree(s, d, symlinks, ignore)
        else:
            # os.makedirs(os.path.join(d, item))
            if not os.path.exists(d) or os.stat(src).st_mtime - os.stat(dst).st_mtime > 1:
                sweetfoldername = os.path.splitext(d)[0]
                if not os.path.exists(sweetfoldername):
                    os.mkdir(sweetfoldername)
                if d.endswith(".tif") or d.endswith(".tiff"):
                    shutil.copy2(s, sweetfoldername)
                    # print "jpg", os.path.splitext(d)[0]
                elif d.endswith(".xml"):
                    shutil.copy2(s, sweetfoldername) #if there's just xml and no matching it takes out the extension
                else:
                    print "NOT FOR INGEST", d

src = str(sys.argv[1])
dst = str(sys.argv[2])

print("Copying into a nested tree")
copytree(src, dst)
print("Batch renaming objects")
batch_rename(dst)
print("Renaming folders")
number_folders(dst)



# ***********************************************************************************************
# ***********************************************************************************************
# ***********************************************************************************************
# ***********************************************************************************************
# os.listdir (just the list), copytree (copies tree folder structure), shutil copy (copies files)
# os.path.exists will also return True if there's a regular file with that name.
# os.path.isdir will only return True if that path exists and is a directory.
#finally figured it out by adding another if path exists sweetfoldername.  yay!

# updated bookbatch to use from the command line.  use this script in the command line:  python bookbatch2.py oGG_003-sys.argv[1] gundepy/GGBOOK-oGG_003-sys.argv[2]

#to try and do it recursively, and to make a new folder
# for num in {1..1000}; do for dir in /Users/dsuuser/Desktop/kim/gunde/STEP1-DONEimagemagick/hey2/*; do (mkdir /Users/dsuuser/Desktop/kim/gunde/STEP1-DONEimagemagick/gundepy/$num && python /Users/dsuuser/Desktop/kim/gunde/STEP1-DONEimagemagick/bookbatch2.py $dir /Users/dsuuser/Desktop/kim/gunde/STEP1-DONEimagemagick/gundepy/$dir); done


# for dir in /Users/dsuuser/Desktop/kim/gunde/STEP1-DONEimagemagick/hey2/*; do python /Users/dsuuser/Desktop/kim/gunde/STEP1-DONEimagemagick/bookbatch2.py $dir /Users/dsuuser/Desktop/kim/gunde/STEP1-DONEimagemagick/gundepy/{A..Z}; done


#trying to rename all images to OBJ and xml to MODS....still in progress to figure it out
# for f in test/*; find . -iname "*.tif" -exec rename *.tif OBJ.tif '{}' \;
