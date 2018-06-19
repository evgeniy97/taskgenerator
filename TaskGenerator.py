import pandas as pd
import json
import NotebookGenerator
import os

def CreateTask(week_number=1, student_with_variants_path='StudentsWithVariants.xlsx',
                notebook_structure_path='Course/notebookstructure/',
                week_path='Course/week{}'):
    # Define all paths
    week_path = week_path.format(week_number)
    head_path = week_path + '/head.json'
    theory_path = week_path + '/theory.json'
    task_path = week_path + '/task{}.json'
    output_path = 'NoteBooks/week{}'.format(week_number)

    if not os.path.exists(output_path):
        os.makedirs(output_path)
    # Load all stuff

    Students = pd.read_excel(student_with_variants_path)
    with open(notebook_structure_path + 'week{}.txt'.format(week_number), encoding="utf8") as file:
        cells = [line.replace('\n', '').split() for line in file.readlines()]

    for student in Students.iterrows():
        cells_source = []
        for cell in cells:
            if cell[0] == 'Task':
                with open(task_path.format(cell[2]), 'r', encoding="utf8") as json_file:
                    data_task = json.load(json_file)
                data = data_task[str(student[1]['Weak 1 Task 1 '])]

                for data_cell in data:
                    cells_source.append([data_cell[0], data_cell[1]])

            elif cell[0] == 'Head':
                with open(head_path, 'r', encoding="utf8") as json_file:
                    data_task = json.load(json_file)
                #data = data_task['text']
                #cells_source.append([data, 'm'])

                for data_cell in data_task:
                    # Первое текст, второе тип - мы идем по ключам словаря. format - чтобы добавить имя
                    cells_source.append([data_task[data_cell][0].format(student[1]['Student']), data_task[data_cell][1]])


            elif cell[0] == 'Th':
                with open(theory_path, 'r', encoding="utf8") as json_file:
                    data_task = json.load(json_file)
                data = data_task[cell[2]] # Получили номер необходимой нам теории
                #print(data)
                for data_cell in data:
                    cells_source.append([data_cell[0], data_cell[1]])
                #cells_source.append([data, 'm'])

        cells_to_write = NotebookGenerator.cells_query(cells_source)
        student_path = output_path + '/{0}_week{1}.ipynb'.format(student[1]['Student'], week_number)
        NotebookGenerator.create_notebook(notebook_name=student_path, cell_list=cells_to_write)
    print('Done!')


if __name__ == '__main__':
    CreateTask()

