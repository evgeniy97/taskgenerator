import numpy as np
import pandas as pd

def GenerateVariantsDistributionOld(random_seed_parametr = 0,student_path = 'students.xlsx', structure_path = 'structure.txt'):
    """
    Generate variant distribution with random seed
    :param random_seed_parametr: parametr to np.random.seed
    :param student_path: path to students list
    :param structure_path: path to course structure
    :return: none
    """
    np.random.seed(random_seed_parametr)
    Students = pd.read_excel(student_path)
    students_number = len(Students)
    with open(structure_path) as file:
        Course_structure = list(map(int, file.readline().split()))
        variants_numbers = list(map(int, file.readline().split()))

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

def __GenerateVariantsDistribution(
        list_disrtibution, random_seed_parametr=0, student_path='students.xlsx',
        students_with_variants_path='StudentsWithVariants.xlsx'):
    """
    generate variant distrbution
    :param list_disrtibution: must be list of list. For example, [[1,2],[1]] shows thaht course has 2 weeks
    and the first week has 2 tasks with 1 and 2 variants and the second week has 1 task with 1 variants
    :param random_seed_parametr: parametr to np.random.seed
    :param student_path: path to students list
    :param students_with_variants_path: path to students list with variants
    """

    np.random.seed(random_seed_parametr)
    try:
        Students = pd.read_excel(student_path)
        # Добавляем столбики в табличку и инициализируем их как None
        for week_number in range(len(list_disrtibution)):
            for task_number in range(len(list_disrtibution[week_number])):
                Students['Week {0} Task {1}'.format(1 + week_number, 1 + task_number)] = None
        # Делаем распределние одномерным вектором
        distribution = []
        for week_dist in list_disrtibution:
            for i in week_dist:
                distribution.append(i)
        for student in Students.get_values():
            for i in range(1, len(student)):
                student[i] = np.random.randint(distribution[i - 1])

        writer = pd.ExcelWriter(students_with_variants_path)
        Students.to_excel(writer)
        writer.save()

        # TODO Удалять файл structure.txt
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
        Students_with_variants = pd.read_excel(students_with_variants_path)
        Students_with_variants = Students_with_variants.sort_values(by='Student')
        writer = pd.ExcelWriter(students_with_variants_path)
        Students_with_variants.to_excel(writer, index=False)
        writer.save()
    except:
        print('No Students_with_variants file')
        return None

def GenerateVariantsDistribution(list_disrtibution, random_seed_parametr=0, student_path='students.xlsx',
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
        __GenerateVariantsDistribution(list_disrtibution, random_seed_parametr,student_path, students_with_variants_path)
        SortByName()
if __name__ == '__main__':
    GenerateVariantsDistributionOld()

