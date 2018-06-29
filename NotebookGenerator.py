import json
import os
from copy import copy


class NotebookGenerator:
    def __init__(self):
        # __kernelspec__ = {"display_name": "Python 3", "language": "python", "name": "python3"},
        self._language_info = {"codemirror_mode": { "name": "ipython", "version": 3},
                               "file_extension": ".py",
                               "mimetype": "text/x-python",
                               "name": "python",
                               "nbconvert_exporter": "python",
                               "pygments_lexer": "ipython3",
                               "version": "3.6.4" }
        self._metadata = {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
                          "language_info":  self._language_info}

        self.jupyter_notebook = {"cells": [],
                                 "metadata": self._metadata,
                                 "nbformat": 4,
                                 "nbformat_minor": 2}
        self.cell_code = {"cell_type": "code",
                          "execution_count": None,
                          "metadata": {},
                          "outputs": [],
                          "source": []}
        self.cell_markdown = {"cell_type": "markdown",
                              "metadata": {},
                              "source": []}
        self.null = None

    def create_notebook(self, notebook_name="test.ipynb", cell_list=None, path="", use_nbdrader_mode=True):
        """
        create notebook with cell_list content in path directory
        :param notebook_name: notebook name with .ipynb
               cell_list: ordered list of cells
               path: path
        :return:
        """
        if not cell_list:
            cell_list = [copy(self.cell_code)]
        if use_nbdrader_mode:
            self.jupyter_notebook["metadata"]["celltoolbar"] = "Create Assignment"

        self.jupyter_notebook['cells'] = cell_list
        if not os.path.isfile(notebook_name):
            print("%s is empty or wrong\n" % notebook_name)
            exit(1)
        with open(notebook_name, 'w', encoding="utf8") as file:
            s = json.dumps(self.jupyter_notebook, indent=2, ensure_ascii=False)
            file.write(s)

    def give_nbtype(self, path_to_MetaDictionary='MetaDictionary.json', nbtype='None'):
        """

        :param path_to_MetaDictionary: return metadata for nbgrader
        :param nbtype: type of cell of nbdrader
        :return: dictionary describe metada
        """
        with open(path_to_MetaDictionary, 'r', encoding="utf8") as json_file:
            MetaDictionary = json.load(json_file)
        return MetaDictionary[nbtype]

    def create_cell(self, content, cell_type='c', nbtype='None'):
        """
        create cell according type and nbgrader type with content
        :param content:
        :param type: c - code; m - markdown;
               nbtype: тип ячейки в метаданных nbgrader
        :return: cell
        """
        if cell_type == 'c':
            cell = copy(self.cell_code)
        elif cell_type == 'm':
            cell = copy(self.cell_markdown)
        else:
            print("\nCell type error\n")
            cell = None
            exit(3)
        cell['source'] = content
        cell['metadata'] = self.give_nbtype(nbtype=nbtype)
        return cell

    def generator_id(self):
        id_number = 0
        while True:
            yield id_number
            id_number += 1

    def cells_query(self, source_list):
        cell_list = []
        for s in source_list:
            if len(s) < 3:
                s.append('None')
            cell_list.append(self.create_cell(s[0], s[1], s[2]))
        generator_id_ReadOnly = self.generator_id()
        generator_id_AutograderAnswer = self.generator_id()
        generator_id_ManuallyGradedAnswer = self.generator_id()
        generator_id_AutoGraderTests = self.generator_id()
        for cell in cell_list:
            if cell['metadata'] != {}:
                if cell['metadata']["nbgrader"]['grade_id'] == 'ReadOnly':
                    cell['metadata']["nbgrader"]['grade_id'] = 'ReadOnly{}'.format(next(generator_id_ReadOnly))
                elif cell['metadata']["nbgrader"]['grade_id'] == 'AutograderAnswer':
                    cell['metadata']["nbgrader"]['grade_id'] = 'AutograderAnswer{}'.format(next(generator_id_AutograderAnswer))
                elif cell['metadata']["nbgrader"]['grade_id'] == 'ManuallyGradedAnswer':
                    cell['metadata']["nbgrader"]['grade_id'] = 'ManuallyGradedAnswer{}'.format(next(generator_id_ManuallyGradedAnswer))
                elif cell['metadata']["nbgrader"]['grade_id'] == 'AutoGraderTests':
                    cell['metadata']["nbgrader"]['grade_id'] = 'AutoGraderTests{}'.format(next(generator_id_AutoGraderTests))
        return cell_list

if __name__ == '__main__':
    #jupyter_notebook['cells'].append(copy(cell_code))
    #jupyter_notebook['cells'].append(copy(cell_markdown))
    #jupyter_notebook['cells'].append(copy(cell_markdown))
     # Тут лежит код из ячейки
    #jupyter_notebook['cells'][0]['source'] = ['print("Hello word!")']
    #jupyter_notebook['cells'][1]['source'] = [r'$\frac{1}{2}$']
    #jupyter_notebook['cells'][2]['source'] = ["# Not russian"]
    #cells = []
    #cells.append(create_cell('print("HELP ME")'))
    #cells.append(create_cell('Hi', type='m'))
    nb_generator = NotebookGenerator()
    cells = nb_generator.cells_query([['print("Hi")\n'
    'print("Hi klgj kjhhjb")\n'
    'print("Hi")\n'
    'print("Hi klgj kjhhjb")', 'c'],['Hi','m']])
    nb_generator.create_notebook(cell_list=cells)

