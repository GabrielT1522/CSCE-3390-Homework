# ************************************************************
# *                                                          *
# * CSCE 3390            Spring 2023         Gabriel Torres  *
# *                                                          *
# *                       Homework 2                         *
# *                                                          *
# *                  Date Created: 02/06/2023                *
# ************************************************************

import sys


def change_file_extension(current_file, new_extension, old_extension):
    # Remove "photo" from filename
    current_file = current_file.replace("photo", "")
    # Replace old extension with new extension
    current_file = current_file.replace(old_extension, new_extension)
    return current_file


# Get the name of the input file from the command line
file_name = sys.argv[1]

# Open the input file for reading
inFile = open(file_name, "r")
# Read the contents of the file into a list of filenames
file_list = inFile.read().splitlines()

for i in range(0, len(file_list)):
    # Find the extension of the file in index i
    extension = file_list[i].split(".")[-1]
    print(change_file_extension(file_list[i], "info.txt", "."+extension))
