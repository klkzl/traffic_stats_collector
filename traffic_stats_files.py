import os
import re

def directory_function(path):
    filelist = os.listdir(path)
    # print(filelist)
    return filelist


def extract_function(file):
    my_file = open(file, "r")
    time = round(float(my_file.readline(17)))
    my_file.close()
    my_file = open(file, "r")
    separate_lines = my_file.readlines()
    sum = 0
    new_list = []
    i = 0
    for row in separate_lines:
        single_db_line = []
        separate_values = row.split()
        if time == round(float(separate_values[0])):
            single_db_line.append(round(float(separate_values[0])))
            single_db_line.append(separate_values[5])
            i = i+1
            single_db_line.append(i)
            x =((re.findall("\d+",separate_values[8])))
            size =float(x[0])
            sum = sum+size
            single_db_line.append(sum)
            time = round(float(separate_values[0]))
        else:
            new_list.append(time)
            new_list.append(separate_values[5])
            new_list.append(i)
            new_list.append(sum)
            x = ((re.findall("\d+", separate_values[8])))
            size = float(x[0])
            sum = size
            i = 1
            time = round(float(separate_values[0]))

    result = new_list+single_db_line
    return result

    # print(result)
    my_file.close()
