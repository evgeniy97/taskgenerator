# -*- coding: utf-8 -*-
"""
Numerical Methods, lab 2
"""

import sympy as sy
from sympy import Rational as syR
from sympy import exp, sin, cos, sqrt, log, ln
from sympy import pi, cot, sinh, cosh, atan, tan

# Это был Task_db
Tasks_db = {
	'Task1':
	[
        # 2.1.1
        {'f': lambda x: sin(x)**2 - syR(5, 6)*sin(x) + syR(1, 6),
         'g': lambda x: sin(x)**2 - sin(x) + syR(1, 4),
         'a': 0, 'b': 1
        },
		# 2.1.2
        {'f': lambda x: sin(x)**2 + syR(7, 12)*sin(x) + syR(1, 12),
         'g': lambda x: sin(x)**2 + syR(2, 3)*sin(x) + syR(1, 9),
         'a': -1, 'b': 0
        },
		# 2.1.3
        {'f': lambda x: sin(x)**2 - syR(1, 30)*sin(x) - syR(1, 30),
         'g': lambda x: sin(x)**2 - syR(2, 5)*sin(x) + syR(1, 25),
         'a': -0.5, 'b': 0.5
        },
		# 2.1.4
        {'f': lambda x: cos(x)**2 + syR(2, 35)*cos(x) - syR(1, 35),
         'g': lambda x: cos(x)**2 - syR(2, 7)*cos(x) + syR(1, 49),
         'a': 0, 'b': 2
        },
		# 2.1.5
        {'f': lambda x: cos(x)**2 - (1/sqrt(2)+syR(1, 4))*cos(x) + (1/4*sqrt(2)),
         'g': lambda x: cos(x)**2 - (2/sqrt(2))*cos(x) + syR(1, 2),
         'a': 0, 'b': 1.5
        },
		# 2.1.6
        {'f': lambda x: cos(x)**2 + syR(1, 2)*cos(x) + syR(1, 18),
         'g': lambda x: cos(x)**2 + syR(1, 3)*cos(x) + syR(1, 36),
         'a': 0, 'b': 2
        },
		# 2.1.7
        {'f': lambda x: ln(x)**2 - 5*ln(x) + 6,
         'g': lambda x: ln(x)**2 - 4*ln(x) + 4,
         'a': 5, 'b': 25
        },
		# 2.1.8
        {'f': lambda x: ln(x)**2 - ln(x) - 2,
         'g': lambda x: ln(x)**2 + 2*ln(x) + 1,
         'a': 0.1, 'b': 10
        },
		# 2.1.9
        {'f': lambda x: ln(x)**2 - syR(3, 4)*ln(x) + syR(1, 8),
         'g': lambda x: ln(x)**2 - ln(x) + syR(1, 4),
         'a': 0.1, 'b': 2
        },
		# 2.1.10
        {'f': lambda x: tan(x)**2 + (sqrt(3) - 1)*tan(x) - sqrt(3),
         'g': lambda x: tan(x)**2 - 2*tan(x) + 1,
         'a': -1.2, 'b': 1
        },
		# 2.1.11
        {'f': lambda x: tan(x)**2 - (syR(28, 9)*tan(x) + syR(1, 3)),
         'g': lambda x: tan(x)**2 - 6*tan(x) + 9,
         'a': 0, 'b': 1.5
        },
		# 2.1.12
        {'f': lambda x: tan(x)**2 - syR(53, 6)*tan(x) - syR(3, 2),
         'g': lambda x: tan(x)**2 - syR(1, 3)*tan(x) + syR(1, 36),
         'a': -0.5, 'b': 1.5
        },
		# 2.1.13
        {'f': lambda x: x**4 - 7*x**2 +10,
         'g': lambda x: x**4 - 4*x**2 + 4,
         'a': 0, 'b': 3
        },
		# 2.1.14
        {'f': lambda x: x**4 - syR(10, 3)*x**2 + 1,
         'g': lambda x: x**4 - 6*x**2 + 9,
         'a': 0, 'b': 2
        },
		# 2.1.15
        {'f': lambda x: x**4 - syR(13, 2)*x**2 + 3,
         'g': lambda x: x**4 - x**2 + syR(1, 4),
         'a': 0, 'b': 3
        },
		# 2.1.16
        {'f': lambda x: sin(x)**2 + syR(5, 6)*sin(x) + syR(1, 6),
         'g': lambda x: sin(x)**2 + syR(2, 3)*sin(x) + syR(1, 9),
         'a': -1, 'b': 0
        },
		# 2.1.17
        {'f': lambda x: sin(x)**2 - syR(7, 12)*sin(x) + syR(1, 12),
         'g': lambda x: sin(x)**2 - syR(1, 2)*sin(x) + syR(1, 16),
         'a': 0, 'b': 1
        },
		# 2.1.18
        {'f': lambda x: sin(x)**2 + syR(1, 30)*sin(x) - syR(1, 30),
         'g': lambda x: x**4 + syR(1, 3)*x**2 + syR(1, 36),
         'a': -0.5, 'b': 0.5
        },
		# 2.1.19
        {'f': lambda x: cos(x)**2 - syR(2, 35)*cos(x) - syR(1, 35),
         'g': lambda x: cos(x)**2 - syR(2, 5)*cos(x) + syR(1, 25),
         'a': 0, 'b': 3
        },
		# 2.1.20
        {'f': lambda x: cos(x)**2 + ((1/sqrt(2)) - syR(1, 4))*cos(x) - (1/4*sqrt(2)),
         'g': lambda x: cos(x)**2 - syR(1, 2)*cos(x) + syR(1, 16),
         'a': 0, 'b': 2
        },
		# 2.1.21
        {'f': lambda x: cos(x)**2 - syR(1, 2)*cos(x) + syR(1, 18),
         'g': lambda x: cos(x)**2 - syR(2, 3)*cos(x) + syR(1, 9),
         'a': 0, 'b': 2
        },
		# 2.1.22
        {'f': lambda x: log(x, 10)**2 + syR(5, 3)*log(x, 10) - syR(2, 3),
         'g': lambda x: log(x, 10)**2 - syR(2, 3)*log(x, 10) + syR(1, 9),
         'a': 0.001, 'b': 3
        },
		# 2.1.23
        {'f': lambda x: log(x, 10)**2 - log(x, 10) - syR(3, 4),
         'g': lambda x: log(x, 10)**2 - 3*log(x, 10) + syR(9, 4),
         'a': 0.1, 'b': 35
        },
		# 2.1.24
        {'f': lambda x: log(x, 10)**2 + syR(3, 4)*log(x, 10) - syR(1, 4),
         'g': lambda x: log(x, 10)**2 + 2*log(x, 10) + 1,
         'a': 0.01, 'b': 3
        },
		# 2.1.25
        {'f': lambda x: tan(x)**2 - (1 + (1/sqrt(3)))*tan(x) + (1/sqrt(3)),
         'g': lambda x: tan(x)**2 - 2*tan(x) + 1,
         'a': 0, 'b': 1
        },
		# 2.1.26
        {'f': lambda x: tan(x)**2 - syR(7, 4)*tan(x) - syR(1, 2),
         'g': lambda x: tan(x)**2 + syR(1, 2)*tan(x) + syR(1, 16),
         'a': -0.5, 'b': 1.5
        },
		# 2.1.27
        {'f': lambda x: tan(x)**2 + syR(37, 6)*tan(x) + 1,
         'g': lambda x: tan(x)**2 + 12*tan(x) + 36,
         'a': -1.5, 'b': 0
        },
		# 2.1.28
        {'f': lambda x: x**4 - 11*x**2 + 24,
         'g': lambda x: x**4 - 6*x**2 + 9,
         'a': 1, 'b': 3
        },
		# 2.1.29
        {'f': lambda x: x**4 - syR(26, 5)*x**2 + 1,
         'g': lambda x: x**4 - 10*x**2 + 25,
         'a': 0, 'b': 3
        },
		# 2.1.30
        {'f': lambda x: x**4 - syR(21, 2)*x**2 + 5,
         'g': lambda x: x**4 - x**2 + syR(1, 4),
         'a': 0, 'b': 5
        }
    ],
	'Task2':
	[
        # 2.2.1
        {'f': lambda x: exp(-x) - 2 + x**2,
         'which': 'отрицательный'},
        # 2.2.2
        {'f': lambda x: x*exp(-x) - x - 1,
         'which': 'положительный'},
		 # 2.2.3
		{'f': lambda x: exp(x) + 1 - sqrt(9 - x**2),
         'which': 'положительный'},
		# 2.2.4
		{'f': lambda x: (x+1)*exp(x+1) - x - 2,
         'which': 'наибольший по модулю'},
		# 2.2.5
		{'f': lambda x: sqrt(x) - cos(x),
         'which': 'все корни'}
    ],
	'Task3':
	[
		# 2.3.1
		{'f': lambda x: sin(x) + 2*x**2 + 4*x},
		# 2.3.2
		{'f': lambda x: exp(-x) - lg(1-x**2) -2},
		# 2.3.3
		{'f': lambda x: sin(x+2) - x**2 + 2*x - 1},
		# 2.3.4
		{'f': lambda x: (x-1)*sinh(x+1) - x},
		# 2.3.5
		{'f': lambda x: x - exp(-x**2)}
	]
}
