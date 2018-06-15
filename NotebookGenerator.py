
import json

from copy import copy

# __kernelspec__ = {"display_name": "Python 3", "language": "python", "name": "python3"},

_language_info = { "codemirror_mode": { "name": "ipython", "version": 3 }, "file_extension": ".py", "mimetype": "text/x-python", "name": "python", "nbconvert_exporter": "python", "pygments_lexer": "ipython3", "version": "3.6.4" }

_metadata = {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"} ,"language_info":  _language_info }

jupyter_notebook = {"cells": [], "metadata": _metadata, "nbformat": 4, "nbformat_minor": 2 }

null = None

cell_code = { "cell_type": "code", "execution_count": null, "metadata": {}, "outputs": [], "source": [] }
cell_markdown = { "cell_type": "markdown",  "metadata": {}, "source": [] }


def create_notebook(notebook_name="test.ipynb", cell_list=[copy(cell_code)], path=""):
    """
    create notebook with cell_list content in path directory
    :param notebook_name: notebook name with .ipynb
           cell_list: ordered list of cells
           path: path
    :return:
    """
    jupyter_notebook['cells'] = cell_list
    with open(notebook_name, 'w') as file:
        s = json.dumps(jupyter_notebook, indent=2, ensure_ascii=False)
        file.write(s)

def create_cell(content, type='c', nbtype=''):
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
    return cell

if __name__ == '__main__':
    #jupyter_notebook['cells'].append(copy(cell_code))
    #jupyter_notebook['cells'].append(copy(cell_markdown))
    #jupyter_notebook['cells'].append(copy(cell_markdown))

     # Тут лежит код из ячейки
    #jupyter_notebook['cells'][0]['source'] = ['print("Hello word!")']
    #jupyter_notebook['cells'][1]['source'] = [r'$\frac{1}{2}$']
    #jupyter_notebook['cells'][2]['source'] = ["# Not russian"]
    cells = []
    cells.append(create_cell('print("HELP ME")'))
    cells.append(create_cell('Hi',type='m'))
    create_notebook(cell_list=cells)

