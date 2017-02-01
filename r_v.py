import glob, sys, shutil, os
# Takes a directory of files and copies them to another directory and changes the trailing 'r' or 'v' to the other one

def swappy(src,dst):

    for f in glob.glob(src+"/*"): # Start with the verso to reverso
        if not os.path.isdir(f):
            d = f[f.rfind("/"):]
            if "r.tif" in f:
                d = d.replace("r","v")
            elif "v.tif" in f:
                d = d.replace("v","r")
            d = dst + d
            print f,d
        shutil.copy(f,d)

swappy(sys.argv[1],sys.argv[2])
#shutil.copy(f,
