import numpy as np
import pandas as pd
import os

def __create_ALL_LR(COURSE_PATH = 'BaseNotebooks'):

    path = os.path.join(os.getcwd(), COURSE_PATH)
    tree = os.walk(path) # tree is a generator, so us next
    files = next(tree)
    py_list = [j for j in files[2] if j[-3:] == '.py'] # get only python files

    with open(path + '\All_LR.py', 'w', encoding="utf8") as output_file:

        source = ''
        for i in py_list:
            source += ("import {0}.{1} as {1}".format(COURSE_PATH, i[:-3]) + '\n')
        source += 'Tasks_db = ['
        for i in py_list:

            source += ("{0}.Tasks_db".format(i[:-3]) + '\n')
            source += ']'
        output_file.write(source)
    print('Create ' + path + '\All_LR.py')

def __generate_stracture(COURSE_PATH = 'BaseNotebooks'):
    from BaseNotebooks.All_LR import Tasks_db # TODO удалять этот файл
    tasks_num = []
    var_num = []

    for week in Tasks_db:
        tasks_num.append(len(week))
        for task_key in week.keys():
            var_num.append((len(week[task_key])))

    print('DELETE ' + os.path.join(os.getcwd(), COURSE_PATH) + '\ALL_LR.py')
    os.remove(os.path.join(os.getcwd(), COURSE_PATH) + '\ALL_LR.py')

    return  tasks_num, var_num

def __GenerateVariantsDistribution(random_seed_parametr = 0,student_path = 'students.xlsx'
                                   , students_with_variants_path='StudentsWithVariants.xlsx'):
    """
    Generate variant distribution with random seed
    :param random_seed_parametr: parametr to np.random.seed
    :param student_path: path to students list
    :return: none
    """
    np.random.seed(random_seed_parametr)
    try:
        Students = pd.read_excel(student_path)
        students_number = len(Students)

        __create_ALL_LR()
        Course_structure, variants_numbers = __generate_stracture()

        Number_of_weaks = len(Course_structure)

        number_of_distribution = 0
        for WeakNumber in range(Number_of_weaks):
            for TaskNumber in range(Course_structure[WeakNumber]):
                Students['Week {0} Task {1}'.format(WeakNumber + 1, TaskNumber + 1)] = np.random.randint(
                    variants_numbers[number_of_distribution], size=students_number)
                number_of_distribution += 1

        writer = pd.ExcelWriter(students_with_variants_path)
        Students.to_excel(writer)
        writer.save()
    except:
        print('File with students doesnot exist')

def Check_New_Students(student_path='students.xlsx', students_with_variants_path='StudentsWithVariants.xlsx'):
    try:
        Students = pd.read_excel(student_path)
    except:
        print('File with students doesnot exist')
        return None
    try:
        Students_with_variants = pd.read_excel(students_with_variants_path)
    except:
        print('No Students_with_variants file')
        return True
    if len(Students) != len(Students_with_variants):
        return True
    else:
        return False

def SortByName(students_with_variants_path='StudentsWithVariants.xlsx'):
    try:
        Students_with_variants = pd.read_excel(students_with_variants_path)
        Students_with_variants = Students_with_variants.sort_values(by='Student')
        writer = pd.ExcelWriter(students_with_variants_path)
        Students_with_variants.to_excel(writer, index=False)
        writer.save()
    except:
        print('No Students_with_variants file')
        return None

def GenerateVariantsDistribution(random_seed_parametr=0, student_path='students.xlsx',
                                 students_with_variants_path='StudentsWithVariants.xlsx' ):
    """
    generate variant distrbution, and sorted it
    :param random_seed_parametr: parametr to np.random.seed
    :param student_path: path to students list
    :param students_with_variants_path: path to students list with variants
    """
    if Check_New_Students(student_path, students_with_variants_path):
        __GenerateVariantsDistribution(random_seed_parametr,student_path, students_with_variants_path)
        SortByName()
if __name__ == '__main__':
    #__generate_stracture()
    GenerateVariantsDistribution()

