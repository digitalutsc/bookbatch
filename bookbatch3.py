#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import shutil
import natsort

def copy_and_overwrite(source_path, target_path):
    """
    Copy the content of the source folder into target folder
    Parameters:
      source_path - full path of the source directory
      target_path - full path of the target directory
    """

    if os.path.exists(target_path):
        shutil.rmtree(target_path)
    shutil.copytree(source_path, target_path)


def rename_target_files(target_path):
    """
    Rename the files so they can be sorted using natural sort
    Parameters:
      target_path - path to which we have copied the source path
    """

    for (root, dirs, files) in os.walk(target_path):
        for file_path in files:

            new_file_name = file_path.replace(' ', '_').lower()
            original_file = os.path.join(target_path, file_path)
            new_file = os.path.join(target_path, new_file_name)
            os.rename(original_file, new_file)

def get_natsort_filelist(source_path):
    """
    Get the listing of the folder in the natural sort order
    Parameters:
      target_path - path to which we have copied the source path
    """

    # Put the output of the command into a list
    file_list = os.system('ls -v ' + source_path + ' > temp.txt')

    hdl = open('temp.txt', 'r')
    file_list = hdl.readlines()
    file_list = natsort.natsorted(file_list)
    hdl.close()
    os.remove('temp.txt')

    return file_list


def put_in_own_folder(folder_path):
    """
    Put each image file in its own folder and rename it as OBJ
    Parameters:
      target_path - folder path where files are processed to
    """

    # Get the sorted list of files (order is important for paging)
    file_list = get_natsort_filelist(folder_path)

    page_count = 1
    for file_name in file_list:
        file_name = file_name.rstrip()
        file_extension = os.path.splitext(file_name)[1]
        if file_extension not in ('.tif', '.tiff'):
            print("WARNING: The following file is not an image file.  It will not be part of the pages. " + file_name)
            continue

        # create the directory
        page_folder_path = os.path.join(folder_path, '%03d'%page_count)
        page_count = page_count + 1
        os.makedirs(page_folder_path)

        # Rename the file
        file_path = os.path.join(folder_path, file_name)
        print("Processing " + file_path)
        new_file_path = os.path.join(page_folder_path, 'OBJ'+ file_extension)
        shutil.move(file_path, new_file_path)


src = str(sys.argv[1])
dst = str(sys.argv[2])

print("Copy the content of the source folder into target folder")
copy_and_overwrite(src, dst)

print("Rename the files so they can be sorted using natural sort")
rename_target_files(dst)

print("Put each image file in its own folder and rename it as OBJ")
put_in_own_folder(dst)

			