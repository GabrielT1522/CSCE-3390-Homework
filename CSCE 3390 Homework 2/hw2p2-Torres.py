# ************************************************************
# *                                                          *
# * CSCE 3390            Spring 2023         Gabriel Torres  *
# *                                                          *
# *                       Homework 2                         *
# *                                                          *
# *                  Date Created: 02/06/2023                *
# ************************************************************

import sys
# Open and read the file inputted by the user
#sys.argv[1] = "students.txt"
file_name = "students.txt"


def process_input_file(file_name):
    inFile = open(file_name, "r")
    student_dict = {}
    for line in inFile:
        line.rstrip().split()
        student_ID = line[0]
        student_first_name = line[1]
        student_last_name = line[2]
        student_major = line[3]
        student_num_of_courses = int(line[4])
        student_courses_list = []
        for course in range():
            student_courses_list.append((line[course]))
        student_dict
    return student_dict






            


