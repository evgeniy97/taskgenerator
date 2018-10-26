
# coding: utf-8

# In[ ]:


"""
Numerical Methods, lab 8
"""

import sympy as sy
from sympy import Rational as syR
from sympy import exp, sin, cos, sqrt, log, ln
from sympy import pi, cot, sinh, cosh, atan, tan

# Это был Task_db
Tasks_db = {
	'Task1':
	[
        # 8.1.1
        {c0 = 0.6,
         c1 = 1.3, 
         c2=0.0,
         c3=1.2,
         c4=1.9
        },
        # 8.1.2
        {c0 =1.0 ,
         c1 =0.9 , 
         c2= 0.8,
         c3=0.7 ,
         c4= 0.5
        },
                # 8.1.3
        {c0 = 0.4,
         c1 = 0.3, 
         c2= 0.2,
         c3= 0.1,
         c4= 2.0
        },
        # 8.1.4
        {c0 = 0.1,
         c1 = -0.1, 
         c2= 1.0,
         c3= 1.0,
         c4= 1.0
        },
        # 8.1.5
        {c0 = 1.5,
         c1 = 0.0, 
         c2= -2.1,
         c3= -1.1,
         c4=3.1 
        },
            # 8.1.6
        {c0 = 2.5,
         c1 =  -2.1,
         c2= 0.0,
         c3= 0.4,
         c4= 0.5
        },
            # 8.1.7
        {c0 = 6.8,
         c1 =  1.7,
         c2= -4.1,
         c3= 0.1,
         c4= -6.1
        },
            # 8.1.8
        {c0 = 0.0,
         c1 =  1.4,
         c2= 3.2,
         c3= 1.6,
         c4= -9.4
        },
            # 8.1.9
        {c0 = 1.3,
         c1 =  0.0,
         c2= -0.1,
         c3= 0.7,
         c4= 8.1
        },
            # 8.1.10
        {c0 = 4.2,
         c1 =  -1.2,
         c2= 1.5,
         c3= 0.0,
         c4= 7.1
        },
            # 8.1.11
        {c0 = 2.2,
         c1 =  0.7,
         c2= 4.5,
         c3= 0.8,
         c4= 0.6
        },
            # 8.1.12
        {c0 = 5.3,
         c1 =  -1.2,
         c2= -1.5,
         c3= 1.3,
         c4= -7.1
        },
            # 8.1.13
        {c0 = 4.9,
         c1 =  5.3,
         c2= 3.3,
         c3= 0.8,
         c4= 5.1
        },
            # 8.1.14
        {c0 = 0.4,
         c1 =  2.7,
         c2= 1.5,
         c3= 1.4,
         c4= 1.1
        },
            # 8.1.15
        {c0 = 2.8,
         c1 =  -1.2,
         c2= -1.5,
         c3= 0.0,
         c4= 6.4
        },
            # 8.1.16
        {c0 = 5.4,
         c1 =  2.1,
         c2= 0.3,
         c3= 2.1,
         c4= 1.6,
         c5=1.6
        },
            # 8.1.17
        {c0 = 0.0,
         c1 =  -2.9,
         c2= -0.9,
         c3= 0.4,
         c4= 1.9,
         c5=2.3
        },
            # 8.1.18
        {c0 = 5.2,
         c1 =  5.3,
         c2= 2.5,
         c3= 0.1,
         c4= 0.0,
         c5=2.3
        },
            # 8.1.19
        {c0 = 4.6,
         c1 =  -0.4,
         c2= 1.6,
         c3= 0.0,
         c4= 2.4,
         c5=-4.1
        },
            # 8.1.20
        {c0 = 3.5,
         c1 =  -0.2,
         c2= -2.3,
         c3= -3.1,
         c4= 3.1,
         c5=5.2
        },
            # 8.1.21
        {c0 = 2.2,
         c1 =  -4.1,
         c2= 0.3,
         c3= -3.4,
         c4= 3.5,
         c5=6.5
        },
            # 8.1.22
        {c0 = 0.8,
         c1 =  6.5,
         c2= -4.4,
         c3= 6.1,
         c4= -3.6,
         c5=2.4
        },
            # 8.1.23
        {c0 = 7.9,
         c1 =  -0.4,
         c2= 2.7,
         c3= 0.7,
         c4= -2.4,
         c5=-2.7
        },
            # 8.1.24
        {c0 = 1.3,
         c1 =  0.5,
         c2= 2.1,
         c3= 5.7,
         c4= 8.3,
         c5=-3.7
        },
            # 8.1.25
        {c0 = 2.7,
         c1 =  2.4,
         c2= 4.5,
         c3= -3.2,
         c4= 6.6,
         c5=2.4
        },
            # 8.1.26
        {c0 = 2.8,
         c1 =  -1.5,
         c2= -0.9,
         c3= 1.8,
         c4= 2.4,
         c5=5.6
        },
            # 8.1.27
        {c0 = 3.3,
         c1 =  -2.3,
         c2= 0.5,
         c3= 0.3,
         c4= 4.3,
         c5=-4.3
        },
            # 8.1.28
        {c0 = 6.1,
         c1 =  0.0,
         c2= 7.5,
         c3= 7.4,
         c4= 0.6,
         c5=-0.6
        },
            # 8.1.29
        {c0 = 2.5,
         c1 =  -3.3,
         c2= 0.0,
         c3= 8.4,
         c4= -5.2,
         c5=0.9
        },
            # 8.1.30
        {c0 = 5.6,
         c1 =  -7.2,
         c2= 1.5,
         c3= 4.6,
         c4= -5.1,
         c5=7.1
        },
],
	'Task3':
	[
          # 8.3.1
        {'f3': lambda x: cos(x)*(2*x)**3,
         'a': 0., 'b': 1.5
        },
    # 8.3.2
        {'f3': lambda x: exp(-2*sin(x)),
         'a': -1.5, 'b': 0.
        },
    # 8.3.3
        {'f3': lambda x:(x+2*x**4)*sin(x**2),
         'a': 0., 'b': 1.7
        },
# 8.3.4
        {'f3': lambda x: (x**2-2*x**3)*cos(x**2),
         'a': -3., 'b': 0
        },
# 8.3.5
        {'f3': lambda x: sin(x)*exp(x**2),
         'a': 0.7, 'b': 1.7
        },
# 8.3.6
        {'f3': lambda x: (cos(x)-x)*exp(x**2),
         'a': -1.7, 'b': 0.
        },
# 8.3.7
        {'f3': lambda x: (cos(x**2)-2)*(2*x)**(1/3),
         'a': -2., 'b': 0.
        },
# 8.3.8
        {'f3': lambda x: (sin(x**(1/3))-3)*x**2,
         'a': 0.5, 'b': 1.5
        },
# 8.3.9
        {'f3': lambda x: ln(2*x+sin(x**2)),
         'a': 1., 'b': 4.
        },
# 8.3.10
        {'f3': lambda x: 4*ln(cos(x**3)+x**2),
         'a': 0., 'b': 2.
        },
    ]
}
