
# coding: utf-8

# In[ ]:


"""
Numerical Methods, lab 4
"""

import sympy as sy
from sympy import Rational as syR
from sympy import exp, sin, cos, sqrt, log, ln
from sympy import pi, cot, sinh, cosh, atan, tan

# Это был Task_db
Tasks_db = {
	'Task1':
	[
        # 4.1.1
        {'f1': lambda x1,x2: sin(x1+x2)-x2-1.2,
         'f2': lambda x1,x2: 2*x1+cos(x2)-2, 
        },
		# 4.1.2
        {'f1': lambda x1,x2: cos(x1-1)+x2-0.5,
         'f2': lambda x1,x2: sin(x1)+2*x2-2, 
        },
		# 4.1.3
        {'f1': lambda x1,x2: sin(x1)+x2-2,
         'f2': lambda x1,x2: cos(x1)+x2-1.5, 
        },
		# 4.1.4
        {'f1': lambda x1,x2: cos(x1)+x2-1.5,
         'f2': lambda x1,x2: 2*x1-sin(x2-0.5)-1, 
        },
		# 4.1.5
        {'f1': lambda x1,x2: sin(x1+1.5)-x2+2.9,
         'f2': lambda x1,x2: cos(x2-2)+x1, 
        },
		# 4.1.6
        {'f1': lambda x1,x2: cos(x1+0.5)+x2-0.8,
         'f2': lambda x1,x2: sin(x2)-2*x1-1.6, 
        },
		# 4.1.7
        {'f1': lambda x1,x2: sin(x1-1)+x2-0.1,
         'f2': lambda x1,x2: x1-sin(x2+1)-0.8, 
        },
		# 4.1.8
        {'f1': lambda x1,x2: cos(x1+x2)+2*x2,
         'f2': lambda x1,x2: x1+sin(x2)-0.6, 
        },
		# 4.1.9
        {'f1': lambda x1,x2: cos(x1+0.5)-x2-2,
         'f2': lambda x1,x2: sin(x2)-2*x1-1, 
        },
		# 4.1.10
        {'f1': lambda x1,x2: sin(x1+x2)-x2-1.5,
         'f2': lambda x1,x2: x1+cos(x2-0.5)-0.5, 
        },
		# 4.1.11
        {'f1': lambda x1,x2: sin(x2+1)-x1-1.2,
         'f2': lambda x1,x2: 2*x1**2+x2-2, 
        },
		# 4.1.12
        {'f1': lambda x1,x2: cos(x2-1)+x1-0.5,
         'f2': lambda x1,x2: x2-cos(x1)-3, 
        },
		# 4.1.13
        {'f1': lambda x1,x2: tan(x1*x2+0.4)-x1**2,
         'f2': lambda x1,x2: 0.6*x1**2+2*x2**2-1, 
        },
		# 4.1.14
        {'f1': lambda x1,x2: sin(x1+x2)-1.6*x1-1,
         'f2': lambda x1,x2: x1**2+x2**2-1, 
        },
		# 4.1.15
        {'f1': lambda x1,x2: tan(x1*x2+0.1)-x1**2,
         'f2': lambda x1,x2: x1**2+2*x2**2-1, 
        },
		# 4.1.16
        {'f1': lambda x1,x2: sin(0.5*x1+x2)-1.2*x1-1,
         'f2': lambda x1,x2: x1**2+x2**2-1, 
        },
		# 4.1.17
        {'f1': lambda x1,x2: tan(x1*x2+0.3)-x1**2,
         'f2': lambda x1,x2: 0.9*x1**2+2*x2**2-1, 
        },
		# 4.1.18
        {'f1': lambda x1,x2: sin(x1+x2)-1.3*x1-1,
         'f2': lambda x1,x2: x1**2+0.2*x2**2-1, 
        },
		# 4.1.19
        {'f1': lambda x1,x2: tan(x1*x2)-x1**2,
         'f2': lambda x1,x2: 0.8*x1**2+2*x2**2-1, 
        },
		# 4.1.20
        {'f1': lambda x1,x2: sin(x1+x2)-1.5*x1-0.1,
         'f2': lambda x1,x2: 3*x1**2+x2**2-1, 
        },
		# 4.1.21
        {'f1': lambda x1,x2: tan(x1*x2)-x1**2,
         'f2': lambda x1,x2: 0.7*x1**2+2*x2**2-1, 
        },
		# 4.1.22
        {'f1': lambda x1,x2: sin(x1+x2)-1.2*x1-0.1,
         'f2': lambda x1,x2: x1**2+x2**2-1, 
        },
		# 4.1.23
        {'f1': lambda x1,x2: tan(x1*x2+0.2)-x1**2,
         'f2': lambda x1,x2: 0.6*x1**2+2*x2**2-1, 
        },
		# 4.1.24
        {'f1': lambda x1,x2: sin(x1+x2)-x1+0.1,
         'f2': lambda x1,x2: 2x2-cos(3*x1)+0.1, 
        },
		# 4.1.25
        {'f1': lambda x1,x2: cos(x1+0.5)+x2-1,
         'f2': lambda x1,x2: sin(x2)-2*x1-2, 
        },
		# 4.1.26
        {'f1': lambda x1,x2: cos(x2-2)+x1,
         'f2': lambda x1,x2: sin(x1+0.5)-x2+2.9, 
        },
		# 4.1.27
        {'f1': lambda x1,x2: sin(x1-1)+x2-1.5,
         'f2': lambda x1,x2: x1-sin(x2-1)-1, 
        },
		# 4.1.28
        {'f1': lambda x1,x2: sin(x2+1)-x1-1,
         'f2': lambda x1,x2: 2*x2+cos(x1)-0.5, 
        },
		# 4.1.29
        {'f1': lambda x1,x2: cos(x2-1)+x1-0.8,
         'f2': lambda x1,x2: x2-cos(x1)-2, 
        },
		# 4.1.30
        {'f1': lambda x1,x2: cos(x1-1)+x2-1,
         'f2': lambda x1,x2: sin(x2)+2*x1-1.6, 
        },
    ]
}

