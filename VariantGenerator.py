import numpy as np
import pandas as pd

def generate_stracture(COURSE_PATH = ''):

    ## TODO Импортить питоновские файлы грамотно, сделать цикл по всем бд-питоновским файлам

    from BaseNotebooks.All_LR import Tasks_db
    tasks_num = []
    var_num = []

    for week in Tasks_db:
        tasks_num.append(len(week))
        for task_key in week.keys():
            var_num.append((len(week[task_key])))

    return  tasks_num, var_num

def __GenerateVariantsDistribution(random_seed_parametr = 0,student_path = 'students.xlsx', structure_path = 'structure.txt'):
    """
    Generate variant distribution with random seed
    :param random_seed_parametr: parametr to np.random.seed
    :param student_path: path to students list
    :param structure_path: path to course structure
    :return: none
    """
    np.random.seed(random_seed_parametr)
    try:
        Students = pd.read_excel(student_path)
        students_number = len(Students)

        Course_structure, variants_numbers = generate_stracture()

        Number_of_weaks = len(Course_structure)

        number_of_distribution = 0
        for WeakNumber in range(Number_of_weaks):
            for TaskNumber in range(Course_structure[WeakNumber]):
                Students['Week {0} Task {1}'.format(WeakNumber + 1, TaskNumber + 1)] = np.random.randint(
                    variants_numbers[number_of_distribution], size=students_number)
                number_of_distribution += 1

        writer = pd.ExcelWriter('StudentsWithVariants.xlsx')
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
    :param list_disrtibution: must be list of list. For example, [[1,2],[1]] shows thaht course has 2 weeks
    and the first week has 2 tasks with 1 and 2 variants and the second week has 1 task with 1 variants
    :param random_seed_parametr: parametr to np.random.seed
    :param student_path: path to students list
    :param students_with_variants_path: path to students list with variants
    """
    if Check_New_Students(student_path, students_with_variants_path):
        __GenerateVariantsDistribution(random_seed_parametr,student_path, students_with_variants_path)
        SortByName()
if __name__ == '__main__':
    GenerateVariantsDistribution()

