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

from settings import weekPath, baseFile, variantsFile, tasksFile, TASKS_DB, outputFile

class VariantGenerator:
    def __init__(self, week_number=1):
        self.week_number = week_number
        self.week_path = weekPath.format(self.week_number)
        self.base_path = os.path.join(self.week_path, baseFile)
        self.variants_path = variantsFile
        self.tasks_path = tasksFile
        self.task_variants = TASKS_DB
        self.output_path = outputFile.format(self.week_number)

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



    def insert_tasks(self):
        students = pd.read_excel(self.variants_path)
        new_notebook = []
        for student in students.iterrows():
            print("Студент", student[1]['Student'])
            #new_notebook = copy(base_notebook)
            new_notebook = self.read_base_notebook()
            for i, cell in enumerate(new_notebook['cells']):
                new_cell = []
                for line in cell['source']:
                    position_variant = line.find("TASK_VARIANT")
                    if position_variant != -1:
                        current_task = line[position_variant - 2]
                        #print("Внутри", student[1]['Student'])
                        current_variant = str(student[1]['Week {0} Task {1}'.format(self.week_number, current_task)])
                        #print(line.replace("TASK_VARIANT", "Variant1").format(**self.task_variants))
                        new_cell.append(line.replace("TASK_VARIANT", current_variant).format(**self.task_variants))
                    else:
                        new_cell.append(line)
                new_notebook['cells'][i]['source'] = new_cell # можно делать это только для тех ячеек где происходят изменения
            student_path = self.output_path + '/{0}_week{1}.ipynb'.format(student[1]['Student'], self.week_number)
            self.create_notebook(new_notebook, student_path)
            print(new_notebook)
        return new_notebook

    def create_notebook(self, new_notebook, notebook_name="test.ipynb"):
        if not os.path.isfile(notebook_name):
            print("%s is empty or wrong\n" % notebook_name)
            exit(1)
        with open(notebook_name, 'w', encoding="utf8") as file:
            s = json.dumps(new_notebook, indent=2, ensure_ascii=False)
            file.write(s)
        return new_notebook


if __name__ == '__main__':
    first_task = VariantGenerator()
    #first_task.create_notebook()
    first_task.insert_tasks()



