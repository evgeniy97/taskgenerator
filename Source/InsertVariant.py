from settings{2} import weekPath, baseFile, variantsFile, tasksFile, outputFile
from BaseNotebooks.{2}DB import Tasks_db

import json
import os
from copy import copy
import pandas as pd
from sympy import latex
from sympy.abc import x


class VariantGenerator:
    def __init__(self, week_number=1):
        self.week_number = week_number
        self.week_path = weekPath.format(self.week_number)
        self.base_path = os.path.join(self.week_path, baseFile)
        self.variants_path = variantsFile
        self.tasks_path = os.path.join(self.week_path, tasksFile)
        self.task_variants = Tasks_db
        self.output_path = outputFile.format(self.week_number)

        if not os.path.exists(self.output_path):
            os.mkdir(self.output_path)


    def read_base_notebook(self):
        if not os.path.isfile(self.base_path):
            print("%s is empty or wrong\n" % self.base_path)
            exit(1)
        with open(self.base_path, 'r', encoding='utf-8') as json_file:
            base_data = json.load(json_file)
            new_data = copy(base_data)
        return new_data

    def change_cell(self, cell, student):
        new_cell = []
        for line in cell['source']:
            position_variant = line.find("TASK_VARIANT")
            if position_variant != -1:
                current_task = line[position_variant - 2]
                current_variant = str(student[1]['Week {0} Task {1}'.format(self.week_number, current_task)])
                # если нет такого ключа
                self.task_variants["Task" + str(current_task)][int(current_variant)]['f_latex'] = latex(
                    self.task_variants["Task" + str(current_task)][int(current_variant)]['f'](x))
                new_cell.append(line.replace("TASK_VARIANT", current_variant).format(**self.task_variants))
            else:
                new_cell.append(line)
        return new_cell

    def add_latex(self, current_task, current_variant):
        self.task_variants["Task" + str(current_task)][int(current_variant)]['f_latex'] = latex(
            self.task_variants["Task" + str(current_task)][int(current_variant)]['f'](x))

    def insert_tasks(self):
        students = pd.read_excel(self.variants_path)
        for student in students.iterrows():
            #new_notebook = copy(base_notebook)
            new_notebook = self.read_base_notebook()
            for i, cell in enumerate(new_notebook['cells']):
                new_notebook['cells'][i]['source'] = self.change_cell(cell, student) # можно делать это только для тех ячеек где происходят изменения
            student_path = self.output_path + '/{0}_week{1}.ipynb'.format(student[1]['Student'], self.week_number)
            self.create_notebook(new_notebook, student_path)

    def create_notebook(self, new_notebook, notebook_path="test.ipynb"):
        # Что за проверка? Может наоборот надо
        #if not os.path.isfile(notebook_path):
        #    print("%s is empty or wrong\n" % notebook_path)
        #    exit(1)
        with open(notebook_path, 'w', encoding="utf8") as file:
            s = json.dumps(new_notebook, indent=2, ensure_ascii=False)
            file.write(s)
        return new_notebook


if __name__ == '__main__':
    first_task = VariantGenerator()
    first_task.insert_tasks()



