import numpy as np
import pandas as pd
import os


class variantgenerator():
    def __init__(self, seed = 0):
        self.COURSE_PATH = 'BaseNotebooks'
        self.random_seed_parametr = seed
        self.student_path = 'students.xlsx'
        self.students_with_variants_path = 'StudentsWithVariants.xlsx'

    def __create_ALL_LR(self):

        path = os.path.join(os.getcwd(), self.COURSE_PATH)
        tree = os.walk(path) # tree is a generator, so us next
        files = next(tree)
        py_list = [j for j in files[2] if j[-3:] == '.py'] # get only python files

        with open(path + '\All_LR.py', 'w', encoding="utf8") as output_file:

            source = ''
            for i in py_list:
                source += ("import {0}.{1} as {1}".format(self.COURSE_PATH, i[:-3]) + '\n')
            source += 'Tasks_db = ['
            for i in py_list:

                source += ("{0}.Tasks_db".format(i[:-3]) + '\n')
                source += ']'
            output_file.write(source)
        print('Create ' + path + '\All_LR.py')

    def __generate_stracture(self):
        from BaseNotebooks.All_LR import Tasks_db
        tasks_num = []
        var_num = []

        for week in Tasks_db:
            tasks_num.append(len(week))
            for task_key in week.keys():
                var_num.append((len(week[task_key])))

        print('DELETE ' + os.path.join(os.getcwd(), self.COURSE_PATH) + '\ALL_LR.py')
        os.remove(os.path.join(os.getcwd(), self.COURSE_PATH) + '\ALL_LR.py')

        return  tasks_num, var_num

    def __GenerateVariantsDistribution(self):
        """
        Generate variant distribution with random seed
        :param random_seed_parametr: parametr to np.random.seed
        :param student_path: path to students list
        :return: none
        """
        np.random.seed(self.random_seed_parametr)
        try:
            Students = pd.read_excel(self.student_path)
            students_number = len(Students)

            self.__create_ALL_LR()
            Course_structure, variants_numbers = self.__generate_stracture()

            Number_of_weaks = len(Course_structure)

            number_of_distribution = 0
            for WeakNumber in range(Number_of_weaks):
                for TaskNumber in range(Course_structure[WeakNumber]):
                    Students['Week {0} Task {1}'.format(WeakNumber + 1, TaskNumber + 1)] = np.random.randint(
                        variants_numbers[number_of_distribution], size=students_number)
                    number_of_distribution += 1

            writer = pd.ExcelWriter(self.students_with_variants_path)
            Students.to_excel(writer)
            writer.save()
        except:
            print('File with students doesnot exist')

    def Check_New_Students(self):
        try:
            Students = pd.read_excel(self.student_path)
        except:
            print('File with students doesnot exist')
            return None
        try:
            Students_with_variants = pd.read_excel(self.students_with_variants_path)
        except:
            print('No Students_with_variants file')
            return True
        if len(Students) != len(Students_with_variants):
            return True
        else:
            return False

    def SortByName(self):
        try:
            Students_with_variants = pd.read_excel(self.students_with_variants_path)
            Students_with_variants = Students_with_variants.sort_values(by='Student')
            writer = pd.ExcelWriter(self.students_with_variants_path)
            Students_with_variants.to_excel(writer, index=False)
            writer.save()
        except:
            print('No Students_with_variants file')
            return None

    def GenerateVariantsDistribution(self):
        """
        generate variant distrbution, and sorted it
        :param random_seed_parametr: parametr to np.random.seed
        :param student_path: path to students list
        :param students_with_variants_path: path to students list with variants
        """
        if self.Check_New_Students():
            self.__GenerateVariantsDistribution()
            self.SortByName()
if __name__ == '__main__':
    variantgenerator().GenerateVariantsDistribution()

