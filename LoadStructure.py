import os
import numpy as np
import json

def count_var(f):
    var_num = 0
    with open(f, 'r', encoding="utf8") as json_file:
        data_tasks = json.load(json_file)
    var_num = len(data_tasks)
    return var_num


def load_structure(course_directory):
    #weeks_num = 0  
    tasks_num = []
    var_num = []
    directories = [d for d in os.listdir(course_directory) 
                   if os.path.isdir(os.path.join(course_directory, d))]
    #weeks_num = len(directories)
    for d in directories:
        task_directory = os.path.join(course_directory, d) 
        file_names = [os.path.join(task_directory, f) 
                      for f in os.listdir(task_directory) 
                      if f.endswith(".json")] 
        tasks_num.append(len(file_names))
        for f in file_names:
            var_num.append(count_var(f))
    return tasks_num, var_num

CURR_PATH = os.curdir
COURSE_PATH = "Course"
COURSE_PATH = os.path.join(CURR_PATH, COURSE_PATH)
str1, str2 = load_structure(COURSE_PATH)
str1 = ' '.join(str(i) for i in str1)
str2 = ' '.join(str(i) for i in str2)
with open("structure.txt", 'w', encoding="utf8") as output_file:
    output_file.write(str1 + '\n' + str2)


