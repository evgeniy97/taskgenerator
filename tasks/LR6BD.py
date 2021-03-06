
# coding: utf-8

# In[ ]:


"""
Numerical Methods, lab 6
"""

import numpy as np
import sympy as sy
from sympy import Rational as syR
from sympy import exp, sin, cos, sqrt, log, ln
from sympy import pi, cot, sinh, cosh, atan, tan

# Это был Task_db
Tasks_db = {
	'Task1':
	[
        # 6.1.1
        {
          x = np.array([-1,-0.7,-0.43,-0.14,-0.14,0.43,0.71,1,1.29,1.57,1.86,2.14,2.43,2.71,3])
          y = np.array([-2.25,-0.77,0.21,0.44,0.64,0.03,-0.22,-0.84,-1.2,-1.03,-0.37,0.61,2.67,5.04,8.90])
        },
        # 6.1.2
        {
          x = np.array([0.0,0.375,0.563,0.75,1.125,1.313,1.5,1.690,1.875,2.063,2.25,2.438,2.625,2.813,3])
          y = np.array([4.568,3.365,2.810,2.624,0.674,0.557,0.384,-0.566,-1.44,-1.696,-1.91,-2.819,-3.625,-3.941,-4.367])
        },
         # 6.1.3
        {
          x = np.array([-1,-0.74,-0.48,-0.21,0.05,0.31,0.58,0.84,1.1,1.36,1.63,1.89,2.15,2.41,2.95])
          y = np.array([3.614,1.199,-0.125,-0.5838,-0.538, -0.2855,0.1111,0.4529,0.6711,0.6625,0.4501,0.157,-0.1876,-0.542,-0.1983])
        },
         # 6.1.4
        {
          x = np.array([-0.5,-0.25,0.0,0.25,0.5,0.75,1.0,1.25,1.5,1.75,2.0,2.25,2.5,2.75,3])
          y = np.array([0.72,1.271,1.2,0.7363,0.24,-0.175,-0.36,-0.328,0.0,0.3538,0.72,0.6969,0.0,-1.792,-5.16])
        },
         # 6.1.5
        {
          x = np.array([-2.1+0.3*i for i in range(15)])
          y = np.array([14.1982,11.4452,9.1586,7.2426,6.3640,4.8182,6.1088,3.9536,4.6872,4.7601,5.8511,7.1010,9.1792,11.421,14.097])
        },
         # 6.1.6
        {
          x = np.array([.2*i for i in range(11)])
          y = np.array([-.9,-.6482,-.2436,-.1,.0231,.026,.0967,-.2203,-.3230,-.6472,-.763])
        },
                 # 6.1.7
        {
          x = np.array([-0.7,-0.41,-0.12,0.17,0.46,0.75,1.04,1.33,1.62,1.91,2.2])
          y = np.array([-4.152,1.244,3.182,2.689,0.95,-2.743,-5.839,-7.253,-6.1,-2.144,6.103])
        },
                 # 6.1.8
        {
          x = np.array([0.3*i for i in range(11)])
          y = np.array([1.019,1.4889,2.2079,3.0548,3.8648,4.2161,5.118,5.7661,6.672,7.196,7.8551])
        },
                         # 6.1.9
        {
          x = np.array([2.5+0.25*i for i in range(11)])
          y = np.array([6.109,2.615,-0.157, -2.010, -2.697,-3.615,-3.478,-2.25,0.193,2.086,5.882])
        },
                                 # 6.1.10
        {
          x = np.array([-3.6,-308,-2.56,-2.04,-1.52,-1.0,-0.48,0.04,0.56,1.08,1.6])
          y = np.array([-2.397,-0.401,-0.577,-1.268,-0.933,-0.359,1.107,1.3,1.703,-0.299,-1.417])
        },
                                 # 6.1.11
        {
          x = np.array([0.0,0.17,0.33,0.5,0.67,0.83,1.0,1.17,1.33,1.5,1.67,1.83,2.0])
          y = np.array([2.25,1.206,0.3951,-0.0334,-0.2,-0.1137,0.0294,0.1008,0.3,-0.0021,-0.3682,-1.119,-2.226])
        },
                                 # 6.1.12
        {
          x = np.array([-1+0.25*i for i in range(13)])
          y = np.array([0.192,-0.054,-0.209,-0.429,-0.413,-0.491,-0.357,-0.434,-0.14,-0.13,0.142,0.288,0.876])
        },
                                 # 6.1.13
        {
          x = np.array([-0.7+0.2*i for i in range(13)])
          y = np.array([1.04,1.08,0.68,0.38,0.07,-0.03,-0.38,-0.22,-0.36,-0.33,-0.28,-0.17,0.27])
        },
                                 # 6.1.14
        {
          x = np.array([-3.0,-2.55,-2.1,-1.65,-1.2,-0.75,-0.3,0.15,0.6,1.05,1.5,1.95,2.4])
          y = np.array([0.262,-1.032,-1.747,-1.981,-0.564,0.774,2.4,2.131,2.2,-0.393,-1.815,-0.788,8.03])
        },
                                 # 6.1.15
        {
          x = np.array([-0.7,-0.375,-0.05, 0.275,0.6,0.925,1.25,1.575,1.9,2.25,2.55,2.875,3.2])
          y = np.array([3.822,-1.498,-2.419,-1.292,0.828,1.963,2.401,1.877,2.2,-1.395,-1.46,3.604])
        },
                            # 6.1.16
        {
          x = np.array([-3.2,-2.66,-2.12,-1.58,-1.04,-0.5,0.04,0.58,1.12,1.66,2.2])
          y = np.array([-0.173,-0.574,-1.811,-1.849,0.123,1.462,2.399,1.3,1.703,-2.045,2.817])
        },
                                 # 6.1.17
        {
          x = np.array([-0.7,-0.31,0.08,0.47,0.86,1.25,1.64,2.03,2,42,2.81,3.2])
          y = np.array([4.166,-2.278,-3.172,-0.506,2.748,2.665,1.353,-0.294,-1.613,-2.223,4.04])
        },
                                    # 6.1.18
        {
          x = np.array([2+0.4*i for i in range(11)])
          y = np.array([1.108,1.832,2.413,3.656,5.126,5.552,6.024,7.202,8.59,8.953,10.046])
        },     
                                 # 6.1.19
        {
          x = np.array([6+0.4*i i in range(11)])
          y = np.array([7.079,-1.509,-7.654,-12.211,-13.941,-15.117,-13.72,-10.702,-4.696,3.501,10.572])
        },
                          # 6.1.20
        {
          x = np.array([-0.7,-0.41,-0.2,0.17,0.46,0.75,1.04,1.33,1.62,1.91,2.2])
          y = np.array([-12.917,3.619,9.586,7.949,1.543,-8.057,-16.15,-20.561,-17.72,-6.2,18.115])
        },
                          # 6.1.21
        {
          x = np.array([0.25*i for i in range(13)])
          y = np.array([-2.815,-2.18,-0.225,1.722,3.492,3.31,2.945,1.449,0.334,-1.906,-3.43,-2.983,0.087])
        },
                          # 6.1.22
        {
          x = np.array([-2.0,-1.67,-1.33,-1.0,-0.67,-0.33,0.0,0.33,0.67,1.0,1.67,2])
          y = np.array([-4.596,-4.216,-3.216,-2.459,-1.558,-0.876,-0.168,0.44,1.715,2.106,2.845,3.83,4.634])
        },
                          # 6.1.23
        {
          x = np.array([-0.5,-0.42,-0.33,-0.25,-0.17,-0.08,0.0,0.08,0.17,0.25,0.33,0.42,0.5])
          y = np.array([0.061,4.185,7.271,9.683,11.319,11.469,11.324,10.495,9.659,7.345,5.132,2.619,0.069])
        },
                          # 6.1.24
        {
          x = np.array([5.5+0.25*i for i in range(13)])
          y = np.array([1.542,0.652,-0.008,-0.62,-0.751,-1.183,-1.229,-1.139,-0.77,-0.586,-0.066,0.633,1.542])
        },
                          # 6.1.25
        {
          x = np.array([-1.0,-0.708,-0.417,-0.125,0.167,0.458,0.75,1.042,1.333,1.625,2.917,2.208,2.5])
          y = np.array([-5.265,-1.994,0.224,1.146,1.552,-0.148,-1.233,-2.297,-2.4,-2.317,2.257,7.806])
        },
                          # 6.1.26
        {
          x = np.array([-1,-0.56,-0.13,0.313,0.75,1.188,1.625,2.063,2.5])
          y = np.array([-5.317,-0.581,1.137,0.478,-0.79,-2.502,-2.482,0.554,7.904])
        },
                          # 6.1.27
        {
          x = np.array([-0.4,-0.05,0.3,0.65,1.0,1.35,1.7,2.05,2.4])
          y = np.array([0.918,1.258,0.685,-1.314,-1.709,-3.446,-2.473,0.084,6.031])
        },
                          # 6.1.28
        {
          x = np.array([-1.3,-0.85,-0.4,0.05,0.5,0.95,1.4,1.85,2.3])
          y = np.array([-1.762,0.955,3.614,4.707,3.721, 0.402,-3.101,-2.489,9.868])
        },
                          # 6.1.29
        {
          x = np.array([0.0,0.288,0.575,0.863,1.15,1.438,1.725,2.013,2.3])
          y = np.array([5.241,4.892,3.521,1.121,-1.357,-3.5,-3.528,0.257,10.515])
        },
                          # 6.1.30
        {
          x = np.array([-0.8, -0.475,-0.15,0.175,0.5,0.825,1.15,1.475,1.8])
          y = np.array([3.503,-0.55,-1.681,-1.263,0.421,1.301,2.551,2.937,2.097])
        },
            ],
	'Task2':
	[ 
        # 6.2.1
        {
          t = np.array([1. ,  1.4,  1.8,  2.6,  3. ,  3.4,  3.8,  4.2,  4.6,  5.])
          x2 = np.array([10.6,18.01,25.85,44.0,50.64,60.2,68.27,77.77,84.5,93.4])
        },
     # 6.2.2
        {
          t = np.array([1.0,1.625,2.25,2.88,3.5,4.13,4.75,5.375,6])
          x2 = np.array(14.86,27.15,41.19,54.0,69.03,81.6,96.11,109.4,124.03[])
        },
     # 6.2.3
        {
          t = np.array([0.5*i for i in range(9)])
          x2 = np.array([3.732,9.378,15.53,22.0,29,52,35.2,42.35,48.61,55.51])
        },
     # 6.2.4
        {
          t = np.array([0. ,  0.6,  1.2,  1.8,  2.4,  3. ,  4.2,  4.8,  5.4,  6.])
          x2 = np.array([6.449,19.97,33.91,48.2,64.15,76.9,106.2,122.2,135.6,149.0])
        },
     # 6.2.5
        {
          t = np.array([2.0,3.2,4.4,5.0,5.6,6.8,7.4,8.0])
          x2 = np.array([18.5,35.73,54.65,62.4,71.74,90.5,98.1,107.6])
        },
     # 6.2.6
        {
          t = np.array([5.0,5.5,6.0,6.5,7.0,7.5,8.0,8.5,9.0])
          x2 = np.array([13.85,14.3,15.84,16.9,18.89,19.7,21.03,22.08,23.95])
        },
    ],
    	'Task3':
	[ 
        # 6.3.1
        {
          x3 = np.array([-2.5+0.5*i for i in range(11)])
          y3 = np.array([0.876,0.29523,0.725958,1.49184,2.23671,2.56,2.23671,1.49184,0.75958,0.29523,0.0876])
          'f3': lambda x,a,b: a*exp(b*x**2)
        },
    # 6.3.2
        {
          x3 = np.array([0.1+0.2*i for i in range(11)])
          y3 = np.array([5.53,2.7967,2.25,2.0157,1.8856,1.8027,1.7454,1.7033,1.6712,1.6458,1.6252])
          'f3': lambda x,a,b: a+b/x
        },
        # 6.3.3
        {
          x3 = np.array([0.1*0.1*i for i in range(11)])
          y3 = np.array([0.479,0.7562,0.9184,1.0335,1.1957,1.2573,1.3107,1.3579,1.4,1.4381])
          'f3': lambda x,a,b: a+b*ln(x) 
        },
        # 6.3.4
        {
          x3 = np.array([-2.0+0.4*i for i in range(11)])
          y3 = np.array([1.649,1.942,2.142,2.274,2.35,2.274,2.142,1.942,1.649])
          'f3': lambda x,a,b: sqrt(a+b*x**2)
        },
        # 6.3.5
        {
          x3 = np.array([-1.5+0.3*i for i in range(11)])
          y3 = np.array([0.0829,0.2192,0.5794,1.5315,4.0481,10.7,4.0481,0.5794,0.2192,0.0829])
          'f3': lambda x,a,b: a*exp(b*abs(x)) 
        },
        # 6.3.6
        {
          x3 = np.array([-2.0+0.4*i for i in range(11)])
          y3 = np.array([8.16617,5.92986,4.30596,3.12677,2.27050,1.64872,2.27050,3.12677,4.30596,5.92986,8.16617])
          'f3': lambda x,a,b: exp(a+b*abs(x)) 
        },
        # 6.3.7
        {
          x3 = np.array([-4+0.8*i for i in range(11)])
          y3 = np.array([-6.47,-3.2086,-2.3433,-2.2767,-1.4114,1.85,9.105,21.951,21.951,41.986,70.806,110.01])
          'f3': lambda x,a,b: a+b*(x+2)**3 
        },
        # 6.3.8
        {
          x3 = np.array([1+0.7*i for i in range(11)])
          y3 = np.array([4.0199,3.9404,3.8574,3.7706,3.6793,3.5827,3.4799,3.3693,3.249,3.1158,2.9644])
          'f3': lambda x,a,b: sqrt(a+b*x)+2 
        },
        # 6.3.9
        {
          x3 = np.array([0.5+0.25*i for i in range(11)])
          y3 = np.array([1.7499,2.5732,3.2817,3.8197,4.1396,4.2065,3.5208,2.7829,1.8224,0.6915,0.6915])
          'f3': lambda x,a,b: (a*x+b)*sin(x) 
        },
        # 6.3.10
        {
          x3 = np.array([-1*0.2*i for i in range(11)])
          y3 = np.array([0.756,1.0033,1.2215,1.4,1.5289,1.6,1.6073,1.5474,1.4196,1.2262,0.9725])
          'f3': lambda x,a,b: (a*x+b)*cos(x) 
        },
    ]
}

