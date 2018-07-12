import os
import sympy as sy
from sympy import Rational as syR
from sympy import exp, sin, cos, sqrt, log, ln
from sympy import pi, cot, sinh, cosh, atan, tan
# Define several named constants, to lighten formulas; XXX: are these useful?
sq2, sq3 = sy.sqrt(2), sy.sqrt(3)
half, quarter = sy.Rational(1, 2), sy.Rational(1, 4)

variantsFile = 'StudentsWithVariants.xlsx'
notebookStructureDir = 'notebookstructure'
weekPath = 'Course/week{}'
nbgraderState = True

headFile = 'head.json'
theoryFile = 'theory.json'
taskFile = 'task{}.json'
outputFile = 'NoteBooks/week{}'
baseFile = 'BaseNotebook.ipynb'
tasksFile = 'TASK_VARIANTS.ipynb'

TASK_VARIANTS = {"Task1":
 {"Variant1": {'f': lambda x: sin(x)**2 - syR(5, 6)*sin(x) + syR(1, 6),
 'g': lambda x: sin(x)**2 - sin(x) + syR(1, 4),
 'a': 0, 'b': 1},
"Variant2": {'f': lambda x: sin(x)**2 + syR(7, 12)*sin(x) + syR(1, 12),
 'g': lambda x: sin(x)**2 + syR(2, 3)*sin(x) + syR(1, 9),
 'a': -1, 'b': 0},
"Variant3": {'f': lambda x: sin(x)**2 - syR(1, 30)*sin(x) - syR(1, 30),
 'g': lambda x: sin(x)**2 - syR(2, 5)*sin(x) + syR(1, 25),
 'a': -0.5, 'b': 0.5},
"Variant4": {'f': lambda x: cos(x)**2 + syR(2, 35)*cos(x) - syR(1, 35),
 'g': lambda x: cos(x)**2 - syR(2, 7)*cos(x) + syR(1, 49),
 'a': 0, 'b': 2},
"Variant5": {'f': lambda x: cos(x)**2 - (1/sqrt(2)+syR(1, 4))*cos(x) + (1/4*sqrt(2)),
 'g': lambda x: cos(x)**2 - (2/sqrt(2))*cos(x) + syR(1, 2),
 'a': 0, 'b': 1.5}
 },
 "Task2":
 {"Variant1": {'f': lambda x: exp(-x) - 2 + x**2,
 'which': 'отрицательный'},
"Variant2": {'f': lambda x: x*exp(-x) - x - 1,
 'which': 'положительный'},
"Variant3": {'f': lambda x: exp(x) + 1 - sqrt(9 - x**2),
 'which': 'положительный'},
"Variant4": {'f': lambda x: (x+1)*exp(x+1) - x - 2,
 'which': 'наибольший по модулю'},
"Variant5": {'f': lambda x: sqrt(x) - cos(x),
 'which': 'все корни'}
 }
}