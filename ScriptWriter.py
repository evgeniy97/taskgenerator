# Rewrite as class

import os

source_path = 'Source'
settings_path = os.path.join(source_path, 'settings.py')
InsertVariant_path =  os.path.join(source_path, 'InsertVariant.py')

def __get_py_list(COURSE_PATH = 'BaseNotebooks'):
    """

    :param COURSE_PATH:
    :return: list of notebooks in COURSE_PATH dir
    """
    path = os.path.join(os.getcwd(), COURSE_PATH)
    tree = os.walk(path) # tree is a generator, so us next
    files = next(tree)
    return [j[:-6] for j in files[2] if j[-6:] == '.ipynb']


def scriptwriter():
    for py_file in __get_py_list():
        # Create settings file
        settings_source = ''
        with open(settings_path, 'r', encoding="utf8") as in_file:
            settings_source = in_file.read()
        settings_source = settings_source.format(py_file)
        with open('settings{}.py'.format(py_file), 'w', encoding="utf8") as output_file:
            output_file.write(settings_source)

        # Create InsertVariant file
        InsertVariant_source = ''
        with open(InsertVariant_path, 'r', encoding="utf8") as in_file:
            InsertVariant_source = in_file.read()
        InsertVariant_source = InsertVariant_source.format({0},{1},py_file)
        with open('InsertVariant{}.py'.format(py_file), 'w', encoding="utf8") as output_file:
            output_file.write(InsertVariant_source)

        # Run InsertVariant for this py_file
        os.system('python InsertVariant{}.py'.format(py_file))
        # Delete it
        os.remove('settings{}.py'.format(py_file))
        os.remove('InsertVariant{}.py'.format(py_file))

if __name__ == '__main__':
    scriptwriter()