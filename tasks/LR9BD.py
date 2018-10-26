
# coding: utf-8

# In[ ]:


"""
Numerical Methods, lab 9
"""

import sympy as sy
from sympy import Rational as syR
from sympy import exp, sin, cos, sqrt, log, ln
from sympy import pi, cot, sinh, cosh, atan, tan


Tasks_db = {
	'Task1':
	[
        # 9.1.1
        {'f1': lambda x:x**2+2*exp(x),
         'a': -2., 'b': 2.
        },
     # 9.1.2
        {'f1': lambda x:exp(x)*sin(x),
         'a': 0., 'b': 4.
        },
     # 9.1.3
        {'f1': lambda x:2*x+exp(4-x),
         'a': 1., 'b': 7.
        },
     # 9.1.4
        {'f1': lambda x:exp(x)-2*sin(x),
         'a': 0., 'b': 2.
        },
     # 9.1.5
        {'f1': lambda x:x**2-2**x,
         'a': 0, 'b': 2
        },
         # 9.1.6
        {'f1': lambda x:2**x-ln(x),
         'a': 0.1, 'b': 3
        },
     # 9.1.7
        {'f1': lambda x:x**3-exp(x),
         'a': 0, 'b': 3
        },
     # 9.1.8
        {'f1': lambda x:sin(x)-2*cos(x),
         'a': 1, 'b': 4
        },
     # 9.1.9
        {'f1': lambda x:x**2-2*sin(x),
         'a': 0, 'b': 3
        },
     # 9.1.10
        {'f1': lambda x:exp(x)*cos(x),
         'a': 0, 'b': 1.5
        },
     # 9.1.11
        {'f1': lambda x:-3*x+exp(x-1),
         'a': 0, 'b': 4
        },
     # 9.1.12
        {'f1': lambda x:x**3-3**x,
         'a': 2, 'b': 3.5
        },
     # 9.1.13
        {'f1': lambda x:exp(x)-ln(x),
         'a': 0.1, 'b': 2
        },
     # 9.1.14
        {'f1': lambda x:3*cos(x)-sin(x),
         'a': 0, 'b': 5
        },
     # 9.1.15
        {'f1': lambda x:x**4-exp(x),
         'a': 0, 'b': 2
        },
     # 9.1.16
        {'f1': lambda x: 3*(cos(x))**2-sqrt(x),
         'a': 0, 'b': 3
        },
     # 9.1.17
        {'f1': lambda x:4*sqrt(x)-tan(x),
         'a': 0, 'b': 1.5
        },
     # 9.1.18
        {'f1': lambda x:(sin(x))**3+(cos(x))**2,
         'a': 0, 'b': 1.5
        },
     # 9.1.19
        {'f1': lambda x:cos(x)*x**2,
         'a': 0, 'b': 2
        },
     # 9.1.20
        {'f1': lambda x: 4**x-8*x,
         'a': 0, 'b': 2
        },
     # 9.1.21
        {'f1': lambda x: x**5-5**x,
         'a': 0.5, 'b': 1.5
        },
     # 9.1.22
        {'f1': lambda x: ln(x)-5*sin(x),
         'a': 1, 'b': 2
        },
     # 9.1.23
        {'f1': lambda x: x**3-exp(x),
         'a': -1, 'b': 0
        },
     # 9.1.24
        {'f1': lambda x: sin(x)+exp(-x**2),
         'a': -1, 'b': 2
        },
     # 9.1.25
        {'f1': lambda x: (sin(x))**2-sqrt(x),
         'a': 0, 'b': 1
        },
     # 9.1.26
        {'f1': lambda x: cos(x)*2**x,
         'a': -2, 'b': 2
        },
     # 9.1.27
        {'f1': lambda x: exp(x-4)-4*x,
         'a': 3, 'b': 8
        },
     # 9.1.28
        {'f1': lambda x: ln(x)-4**x,
         'a': 0.1, 'b': 1
        },
     # 9.1.29
        {'f1': lambda x: 2*sin(x)-3*cos(x),
         'a': -1, 'b': 1
        },
     # 9.1.30
        {'f1': lambda x:x**6-exp(x),
         'a': 0, 'b': 1
        },
    ],
	'Task2':
	[
        # 9.2.1
        {'f2': lambda t: sin(t**2),
         'x1': 0, 'x2': 2
         'which': 'Золотого сечения'},
    # 9.2.2
        {'f2': lambda t: (t+1)*cos(t),
         'x1': 0, 'x2': 4
         'which': 'Деления отрезка пополам'},
    # 9.2.3
        {'f2': lambda t: cos(exp(t)),
         'x1': 1, 'x2': 2
         'which': 'Фибоначчи'},
    # 9.2.4
        {'f2': lambda t: (t**2-t-1)/(t**2+t+5),
         'x1': -1, 'x2': 2
         'which': 'Золотого сечения'},
    # 9.2.5
        {'f2': lambda x: sin(t)/(t**2+1),
         'x1': 1, 'x2': 4
         'which': 'Деления отрезка пополам'},
    # 9.2.6
        {'f2': lambda t: (t**2-3)/(t**2+2),
         'x1': -1, 'x2': 4
         'which': 'Фибоначчи'},
        # 9.2.7
        {'f2': lambda t: (t**2-2)/exp(t),
         'x1': 0, 'x2': 4
         'which': 'Золотого сечения'},
    # 9.2.8
        {'f2': lambda t: sin(exp(t)),
         'x1': 0, 'x2': 1.5
         'which': 'Деления отрезка пополам'},
    # 9.2.9
        {'f2': lambda t:t*sin(t) ,
         'x1': 0, 'x2': 5
         'which': 'Фибоначчи'},
    # 9.2.10
        {'f2': lambda t: cos(t**2),
         'x1': 0, 'x2': 2
         'which': 'Золотого сечения'},
    ]
}

