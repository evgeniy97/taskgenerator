
import json

from copy import copy

# __kernelspec__ = {"display_name": "Python 3", "language": "python", "name": "python3"},

_language_info = { "codemirror_mode": { "name": "ipython", "version": 3 }, "file_extension": ".py", "mimetype": "text/x-python", "name": "python", "nbconvert_exporter": "python", "pygments_lexer": "ipython3", "version": "3.6.4" }

_metadata = {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"} ,"language_info":  _language_info }

jupyter_notebook = {"cells": [], "metadata": _metadata, "nbformat": 4, "nbformat_minor": 2 }

null = None

cell_code = { "cell_type": "code", "execution_count": null, "metadata": {}, "outputs": [], "source": [] }
cell_markdown = { "cell_type": "markdown",  "metadata": {}, "source": [] }


if __name__ == '__main__':
     jupyter_notebook['cells'].append(copy(cell_code))
     jupyter_notebook['cells'].append(copy(cell_markdown))
     jupyter_notebook['cells'].append(copy(cell_markdown))

     # Тут лежит код из ячейки
     jupyter_notebook['cells'][0]['source'] = ['print("Hello word!")']
     jupyter_notebook['cells'][1]['source'] = [r'$\frac{1}{2}$']
     jupyter_notebook['cells'][2]['source'] = ["# Not russian"]

     with open('test.ipynb','w') as file:
        s = json.dumps(jupyter_notebook, indent=2, ensure_ascii=False)
        file.write(s)