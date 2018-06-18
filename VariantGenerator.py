import numpy as np
import pandas as pd

def GenerateVariantsDistribution(random_seed_parametr = 0,student_path = 'students.xlsx', structure_path = 'structure.txt'):
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
        for TaskNumber in range(1, Course_structure[WeakNumber] + 1):
            Students['Week {0} Task {1}'.format(WeakNumber + 1, TaskNumber)] = np.random.randint(
                variants_numbers[number_of_distribution], size=students_number)
            number_of_distribution += 1

    writer = pd.ExcelWriter('StudentsWithVariants.xlsx')
    Students.to_excel(writer)
    writer.save()

if __name__ == '__main__':
    GenerateVariantsDistribution()


