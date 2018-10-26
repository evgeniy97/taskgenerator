
# coding: utf-8

# In[ ]:


"""
Numerical Methods, lab 3
"""

import sympy as sy
from sympy import Rational as syR
from sympy import exp, sin, cos, sqrt, log, ln
from sympy import pi, cot, sinh, cosh, atan, tan

# Это был Task_db
Tasks_db = {
	'Task1':
	[
        # 3.1.1
        {'a': lambda c: 15/(4*c**5 +6*c+1),
         'N': 6, 
        },
		# 3.1.2
        {'a': lambda c: 125/(4+0.25*c)**6,
         'N': 6,
        },
		# 3.1.3
        {'a': lambda c: 12/(4*c+4),
         'N': 6,
        },
		# 3.1.4
        {'a': lambda c: 55/(c**2+3*c+100),
         'N': 7,
        },
		# 3.1.5
        {'a': lambda c: 135/(2+0.3*c)**5,
         'N': 7,
        },
		# 3.1.6
        {'a': lambda c: 3/(c**4-4*c**3),
         'N': 7,
        },
		# 3.1.7
        {'a': lambda c: 256/(5+c*0.256)**5,
         'N': 6,
        },
		# 3.1.8
        {'a': lambda c: 1/sqrt(c**2+0.58*c),
         'N': 6,
        },
		# 3.1.9
        {'a': lambda c: 3/(c+1)**2,
         'N': 5,
        },
		# 3.1.10
        {'a': lambda c: sin(c/8),
         'N': 5,
        },
		# 3.1.11
        {'a': lambda c: 1/(67+c**4),
         'N': 4,
        },
		# 3.1.12
        {'a': lambda c: 111/(c**4+13+3*c),
         'N': 4,
        },
		# 3.1.13
        {'a': lambda c: 1/(c+1)**3,
         'N': 5,
        },
		# 3.1.14
        {'a': lambda c: 1.5/(0.001*c**3-2.5*c),
         'N': 7,
        },
		# 3.1.15
        {'a': lambda c: 88.5/(c+0.03*c**2),
         'N': 6,
        },
		# 3.1.16
        {'a': lambda c: 100/(0.3*c+3)**5,
         'N': 5,
        },
		# 3.1.17
        {'a': lambda c: 115/(3*c+4*c**3),
         'N': 4,
        },
		# 3.1.18
        {'a': lambda c: 123/(2*c**3+5*c**2),
         'N': 5,
        },
		# 3.1.19
        {'a': lambda c: 100/(c+11)**5,
         'N': 5,
        },
		# 3.1.20
        {'a': lambda c: cos(c/25),
         'N': 6,
        },
		# 3.1.21
        {'a': lambda c: 1000/(3*c**2+c**3),
         'N': 6,
        },
		# 3.1.22
        {'a': lambda c: 150/(13*c**3+777*c),
         'N': 5,
        },
		# 3.1.23
        {'a': lambda c: 11.7/(c+1)**7,
         'N': 5,
        },
		# 3.1.24
        {'a': lambda c: 159/(10*c**3+c**2+25),
         'N': 4,
        },
		# 3.1.25
        {'a': lambda c: 321/(c+1)**6,
         'N': 5,
        },
		# 3.1.26
        {'a': lambda c: 31/sqrt(c**2+6*c),
         'N': 5,
        },
		# 3.1.27
        {'a': lambda c: 350/(5+0.35*c)**3,
         'N': 6,
        },
		# 3.1.28
        {'a': lambda c: 500/(8*c-5)**2,
         'N': 5,
        },
		# 3.1.29
        {'a': lambda c: 10/(0.3*c**3+10*c),
         'N': 6,
        },
		# 3.1.30
        {'a': lambda c: 1/(0.4*c**3+20*c),
         'N': 5,
        }
    ]
}

