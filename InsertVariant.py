import json
import os
from copy import copy
import pandas as pd

import sympy as sy
from sympy import Rational as syR
from sympy import exp, sin, cos, sqrt, log, ln
from sympy import pi, cot, sinh, cosh, atan, tan
# Define several named constants, to lighten formulas; XXX: are these useful?
sq2, sq3 = sy.sqrt(2), sy.sqrt(3)
half, quarter = sy.Rational(1, 2), sy.Rational(1, 4)

from settings import weekPath, baseFile, variantsFile, tasksFile, TASK_VARIANTS

class VariantGenerator:
    def __init__(self, week_number=1):
        self.week_number = week_number
        self.week_path = weekPath.format(self.week_number)
        self.base_path = os.path.join(self.week_path, baseFile)
        self.variants_path = variantsFile
        self.tasks_path = tasksFile
        self.task_variants = TASK_VARIANTS

    #student_path = self.output_path + '/{0}_week{1}.ipynb'.format(student[1]['Student'], self.week_number)
    #nb_generator.create_notebook(notebook_name=student_path, cell_list=cells_to_write)

    def read_base_notebook(self):

        if not os.path.isfile(self.base_path):
            print("%s is empty or wrong\n" % self.base_path)
            exit(1)
        with open(self.base_path, 'r', encoding='utf-8') as json_file:
            base_data = json.load(json_file)
            new_data = copy(base_data)
        return new_data

    #def read_tasks(self):
    #    if not os.path.isfile(self.tasks_path):
    #        print("%s is empty or wrong\n" % self.tasks_path)
    #        exit(1)
    #    with open(self.tasks_path, 'r', encoding='utf-8') as json_file:
    #        data = json.load(json_file)
    #        tasks_data = copy(data)
    #    return tasks_data['cells'][0]['source']

    def read_variants(self):
        student_variants = []
        students = pd.read_excel(self.variants_path)
        for student in students.iterrows():
            curr_student_var = []
            #print(student[1]['Student'])
            for variant in student[1][1:]:
                curr_student_var.append(variant)
            student_variants.append(curr_student_var)
        #print(student_variants)
        return student_variants

    def insert_tasks(self):
        base_notebook = self.read_base_notebook()
        new_notebook = copy(base_notebook)
        student_variants = self.read_variants() # все задания пока что от 0 до 9
        for i, cell in enumerate(base_notebook['cells']):
            new_cell = []
            for line in cell['source']:
                position_variant = line.find("TASK_VARIANT")
                if position_variant != -1:
                    #print("Позиция варианта", position_variant)
                    current_variant = line[position_variant - 2]
                    print("Текущее задание", current_variant)

                    #print(line.replace("TASK_VARIANT", "Variant1").format(**self.task_variants))

                    new_cell.append(line.replace("TASK_VARIANT", "Variant1").format(**self.task_variants))
                else:
                    new_cell.append(line)
            new_notebook['cells'][i]['source'] = new_cell # можно делать это только для тех ячеек где происходят изменения
        print(new_notebook)
        return new_notebook

    def create_notebook(self, notebook_name="test.ipynb"):
        if not os.path.isfile(notebook_name):
            print("%s is empty or wrong\n" % notebook_name)
            exit(1)
        with open(notebook_name, 'w', encoding="utf8") as file:
            new_notebook = self.insert_variant()
            s = json.dumps(new_notebook, indent=2, ensure_ascii=False)
            file.write(s)
        return new_notebook


if __name__ == '__main__':
    first_task = VariantGenerator()
    #first_task.create_notebook()
    first_task.insert_tasks()


