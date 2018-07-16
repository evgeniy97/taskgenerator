import pandas as pd
import json
import os

from NotebookGenerator import NotebookGenerator
from settings import variantsFile, notebookStructureDir, weekPath, nbgraderState
from settings import headFile, theoryFile, taskFile, outputFile


class TaskGenerator:
    def __init__(self, week_number=1, use_nbgrader_mode=nbgraderState):
        self.week_number = week_number
        self.variants_path = variantsFile
        self.use_nbgrader_mode = use_nbgrader_mode
        # Define all paths
        self.week_path = weekPath.format(self.week_number)
        self.head_path = os.path.join(self.week_path, headFile)
        self.theory_path = os.path.join(self.week_path, theoryFile)
        self.task_path = os.path.join(self.week_path, taskFile)
        self.output_path = outputFile.format(self.week_number)
        self.week_structure_path = os.path.join(notebookStructureDir, 'week{}.txt'.format(self.week_number))

        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)

    def read_cells(self):
        if not os.path.isfile(self.week_structure_path):
            print("\nWeek structure is not exists or wrong\n")
            exit(2)
            #return list()
        with open(self.week_structure_path, encoding="utf8") as file:
            cells = [line.replace('\n', '').split() for line in file.readlines()]
            return cells

    def read_data(self, path):
        if not os.path.isfile(path):
            print("%s is empty or wrong\n" % path)
            exit(2)
            #return list()
        with open(path, 'r', encoding="utf8") as json_file:
            data_task = json.load(json_file)
            return data_task

    def parse_theory_cell(self, cell):
        theory_source = []
        data_task = self.read_data(self.theory_path)
        data = data_task[cell[1]]  # Получили номер необходимой нам теории
        # print(data)
        for data_cell in data:
            theory_source.append([data_cell[0], data_cell[1], data_cell[2]])
        return theory_source

    # cells_source.append([data, 'm'])

    def parse_task_cell(self, cell, student):
        task_source = []
        data_task = self.read_data(self.task_path.format(cell[1]))
        data = data_task[str(student[1]['Week {0} Task {1}'.format(self.week_number, cell[1])])]
        for data_cell in data:
            task_source.append([data_cell[0], data_cell[1], data_cell[2]])
        return task_source

    def parse_head_cell(self, student):
        head_source = []
        data_task = self.read_data(self.head_path)
            # data = data_task['text']
            # cells_source.append([data, 'm'])
        for data_cell in data_task:
            # Первое текст, второе тип - мы идем по ключам словаря. format - чтобы добавить имя
            head_source.append(
                [data_task[data_cell][0].format(student[1]['Student']),
                 data_task[data_cell][1],
                 data_task[data_cell][2]])
        return head_source

    def create_task(self):
        # Load all stuff
        students = pd.read_excel(self.variants_path)
        cells = self.read_cells()
        for student in students.iterrows():
            cells_source = []
            for cell in cells:
                if cell[0] == 'Task':
                    source = self.parse_task_cell(cell, student)
                elif cell[0] == 'Head':
                    source = self.parse_head_cell(student)
                elif cell[0] == 'Th':
                    source = self.parse_theory_cell(cell)
                else:
                    print("\nstructure type error\n")
                    source = list()
                cells_source += source

            nb_generator = NotebookGenerator()
            cells_to_write = nb_generator.cells_query(cells_source)
            student_path = self.output_path + '/{0}_week{1}.ipynb'.format(student[1]['Student'], self.week_number)
            nb_generator.create_notebook(notebook_name=student_path, cell_list=cells_to_write)
        print('Done!')


if __name__ == '__main__':
    first_task = TaskGenerator()
    first_task.create_task()

