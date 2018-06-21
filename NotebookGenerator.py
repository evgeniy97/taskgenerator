
import json

from copy import copy

# __kernelspec__ = {"display_name": "Python 3", "language": "python", "name": "python3"},

_language_info = { "codemirror_mode": { "name": "ipython", "version": 3 }, "file_extension": ".py", "mimetype": "text/x-python", "name": "python", "nbconvert_exporter": "python", "pygments_lexer": "ipython3", "version": "3.6.4" }

_metadata = {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"} ,"language_info":  _language_info }

jupyter_notebook = {"cells": [], "metadata": _metadata, "nbformat": 4, "nbformat_minor": 2 }

null = None

cell_code = { "cell_type": "code", "execution_count": null, "metadata": {}, "outputs": [], "source": [] }
cell_markdown = { "cell_type": "markdown",  "metadata": {}, "source": [] }

def generate_uniq_cell_id(nbtype='None'):

    def generator_id():
        id_number = 0
        while True:
            yield id_number
            id_number += 1

    gen

def create_notebook(notebook_name="test.ipynb", cell_list=[copy(cell_code)], path="", use_nbdrader_mode = True):
    """
    create notebook with cell_list content in path directory
    :param notebook_name: notebook name with .ipynb
           cell_list: ordered list of cells
           path: path
    :return:
    """
    if use_nbdrader_mode:
        jupyter_notebook["metadata"]["celltoolbar"] = "Create Assignment"

    jupyter_notebook['cells'] = cell_list
    with open(notebook_name, 'w', encoding="utf8") as file:
        s = json.dumps(jupyter_notebook, indent=2, ensure_ascii=False)
        file.write(s)



def give_nbtype(path_to_MetaDictionary = 'MetaDictionary.json',nbtype = 'None'):
    """

    :param path_to_MetaDictionary: return metadata for nbgrader
    :param nbtype: type of cell of nbdrader
    :return: dictionary describe metada
    """
    with open(path_to_MetaDictionary, 'r', encoding="utf8") as json_file:
        MetaDictionary = json.load(json_file)
    return MetaDictionary[nbtype]

def create_cell(content, type='c', nbtype='None'):
    """
    create cell according type and nbgrader type with content
    :param content:
    :param type: c - code; m - markdown;
           nbtype: тип ячейки в метаданных nbgrader
    :return: cell
    """
    if type == 'c':
        cell = copy(cell_code)
    elif type == 'm':
        cell = copy(cell_markdown)

    cell['source'] = content
    cell['metadata'] = give_nbtype(nbtype=nbtype)
    return cell

def cells_query(source_list):
    cell_list = []
    for s in source_list:
        if len(s) < 3:
            s.append('None')
        cell_list.append(create_cell(s[0], s[1],s[2]))

    def generator_id():
        id_number = 0
        while True:
            yield id_number
            id_number += 1

    generator_id_ReadOnly = generator_id()
    generator_id_AutograderAnswer = generator_id()
    generator_id_ManuallyGradedAnswer = generator_id()
    generator_id_AutoGraderTests = generator_id()


    for cell in cell_list:
        if cell['metadata'] != {} :
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
    cells = cells_query([['print("Hi")\n'
    'print("Hi klgj kjhhjb")\n'
    'print("Hi")\n'
    'print("Hi klgj kjhhjb")', 'c'],['Hi','m']])
    create_notebook(cell_list=cells)

