
# coding: utf-8

# In[ ]:



"""
Numerical Methods, lab 5
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
        # 5.1.1
        {
            A = np.array([[79.2, 0.0,35.0,19.8, 24.0],
     [39.6, 85.0, 0.0, 19.8, 25.0],
     [19.8, -15.0, 45.0, 0.0, 10.0],
     [49.5, 18.0, 20.0, 89.1, 0.0],
     [9.9, 15.0, 20.0, -49.5, 95.0]])

            b = np.array([[86.0],[55.0],[77.0],[5.0], [-64.0]])
        },
        # 5.1.2
        {
            A = np.array([[29.7, 2.0, 0.0, 19.8, 2.0],
     [9.9, -21.0, 0.0, -9.9, 1.0],
     [-9.9, 11.0, 29.0, 6.6, 1.0],
     [9.9, 7.5, 2.0, -19.8, 0.0],
     [-49.5, -1.0, 23.0, 9.9, 84.0]])

            b = np.array([[26.2],[-41.1],[97.4],[99.8], [27.1]])
        },

        # 5.1.3
        {
            A = np.array([[89.1, 29.0, 0.0,59.4, 0.0],
     [39.6, -84.0, 0.0, -39.6, 4.0],
     [-29.7, 31.0, 86.0, 19.8, 3.0],
     [49.5, 39.0, 8.0, -99.0, 0.0],
     [-59.4, 0.0, 24.0, 13.2, 98.0]])

            b = np.array([[260.2],[-313.2],[293.3],[-212.4], [230.8]])
        },
        
        # 5.1.4
        {
            A = np.array([[39.6, 0.0,17.5,9.9, 12.0],
     [79.2, 120.0, 0.0, 39.6, 0.0],
     [19.8, -21.0, 46.0, 0.0, 5.0],
     [49.5, 19.0, 19.0, 89.1, 0.0],
     [9.9, 25.0, 10.0, -39.6, 85.0]])

            b = np.array([[38.5],[38.8],[93.7],[43.0], [-49.7]])
        },
        # 5.1.5
        {
            A = np.array([[99.0, 28.0,0.0,69.3, 0.0],
     [49.5, -94.0, 3.0, -29.7, 10.0],
     [39.6, 24.0, -96.0, -29.7, 0.0],
     [29.7, 24.0, 23.0, 79.2, 0.0],
     [69.3, 0.0, 21.0, -3.3, -98.0]])

            b = np.array([[40.2],[91.5],[93.4],[84.7], [-1.5]])
        },
        
        # 5.1.6
        {
            A = np.array([[7.92, 3.36, -2.24, 1.98],
     [-13.86 , 18.20, 0.0, 3.96],
     [-2.97, 0.20, 4.80, 0.0],
     [5.94, 0.0, -10.60, 16.83]])

            b = np.array([[-1.956],[62.8],[-4.16],[48.31]])
        },
        
        # 5.1.7
        {
            A = np.array([[4.95, 1.12, 2.9, 0.66],
     [8.91, 19.9, -4.0, 6.93],
     [-2.97, 2.2, -5.8, 0.0],
     [5.94, 1.3, 10.5, 17.82]])

            b = np.array([[-3.41],[50.33],[19.49],[-45.88]])
        },

        # 5.1.8
        {
            A = np.array([[118.8, -14.0, -5.0, -89.1],
     [-59.4, 194.0, 5.0, 128.7],
     [148.5, 12.0, -310.0, 148.5],
     [0.0, 18.5, 90.0,-108.9]])

            b = np.array([[-92.5],[-340.1],[-898.0],[184.1]])
        },        
        
        # 5.1.9
        {
            A = np.array([[118.8, -14.0, -5.0, -89.1],
     [-14.85, -20.0, -5.0, 0.0],
     [297.0, 16.0, 320.0, 0.0],
     [0.0, 6.0, -30.0, -36.3]])

            b = np.array([[444.5],[-41.05],[-635.0],[209.3]])
        },
                
        # 5.1.10
        {
            A = np.array([[49.5,12.52,16.12,19.80],
     [0.0, 27.1,1.64,23.76],
     [12.87,11.52, 40.0,-14.85],
     [0,4.32, 0.12, 6.27]])

            b = np.array([[-92.98],[25.46],[-26.76],[-1.15]])
        },   
        
        # 5.1.11
        {
            A = np.array([[3.96, -1.5, 0.0,-0.99,-1.4,0.0],
     [3.96,18.3,1.6,6.93, 4.3,1.5],,
     [0.0, 4.6,-13.0,4.29,-1.4 ,2.3],
     [3.96,0.4,0.0,5.94,1.5,0.0],
     [ 5.94,3.1,3.4,0.99,14.4,0.9],
     [-2.97,-1.2 ,0.8,4.95,-2.7,12.7]])

            b = np.array([[32.83],[91.31],[29.91],[98.8], [56.97],[37.92]])
        },
                
        # 5.1.12
        {
            A = np.array([[9.9,3.0 , 4.0,0.0,1.3, 1.5],
     [1.98,9.8,0.8,5.94,0.42,-0.6],
     [3.96,-4.8,19.7,9.9,0.72 ,0.3],
     [1.98,1.2,1.1,6.93, 0.81,-1.2],
     [9.9,-7.5,2.1,-9.9,29.5,0.0],
     [-2.97,-1.2,0.8, 4.95, 2.7,12.7]])

            b = np.array([[-73.34],[-37.456],[-126.316],[-82.528], [96.66],[7.41]])
        },
        
                        
        # 5.1.13
        {
            A = np.array([[2.97,0.4,0.3,1.98,0.0,0.1],
     [0.99,4.9,0.4,2.97,0.2,-0.3],
     [0.0,-1.8,6.6,3.3,0.6,0.8 ],
     [4.95,1.6,1.2,8.91,0.8,0.3],
     [1.98,-1.5,0.4,-1.98,6.1,0.0],
     [9.9,1.4,2.4,5.94,3.2,23.3]])

            b = np.array([[4.69],[12.18],[-3.64],[21.05], [0.42],[-13.91]])
        },
        
        # 5.1.14
        {
            A = np.array([[5.94,0.8,0.6,-3.96,0.2,0.3],
     [2.97,6.4,0.0,-2.97,0.2,0.2],
     [2.97,3.5,8.7,1.98,0.2,0.0],
     [4.95,1.6,1.2,-8.91,0.8,0.3],
     [-0.99,2.5,1.1,-3.96,9.0,0.4],
     [5.94,1.4,2.4,0.0,3.2,13]])

            b = np.array([[11.44],[-54.75],[-4.64],[20.47], [-95.86],[26.92]])
        },
        
        # 5.1.15
        {
            A = np.array([[0.33,0.1,0.1,0.0,0.02,0.1],
     [0.99,4.9,0.4,2.97,0.21,-0.3],
     [1.32,-1.6,6.6,3.3,0.24,0.1],
     [1.98,1.2,1.1,6.93,0.81,-1.2],
     [1.98,-1.5,0.4,-1.98,6.1,0.0],
     [0.99,0.4,0.3,1.65,0.9,4.3]])

            b = np.array([[1.620],[23.365],[-14.010],[18.955], [24.880],[-1.500]])
        },
        
        # 5.1.16
        {
            A = np.array([[79.2, 0.0,35.0,19.8, 24.0],
     [39.6, 85.0, 0.0, 19.8, 25.0],
     [19.8, -15.0, 45.0, 0.0, 10.0],
     [49.5, 18.0, 20.0, 89.1, 0.0],
     [9.9, 15.0, 20.0, -49.5, 95.0]])

            b = np.array([[-468.1],[122.3],[-257.2],[-223.6], [35.9]])
        },
        # 5.1.17
        {
            A = np.array([[29.7, 2.0, 0.0, 19.8, 2.0],
     [9.9, -21.0, 0.0, -9.9, 1.0],
     [-9.9, 11.0, 29.0, 6.6, 1.0],
     [9.9, 7.5, 2.0, -19.8, 0.0],
     [-49.5, -1.0, 23.0, 9.9, 84.0]])

            b = np.array([[29.2],[99.9],[-174.7],[75.05], [-185.9]])
        },

        # 5.1.18
        {
            A = np.array([[89.1, 29.0, 0.0,59.4, 0.0],
     [39.6, -84.0, 0.0, -39.6, 4.0],
     [-29.7, 31.0, 86.0, 19.8, 3.0],
     [49.5, 39.0, 8.0, -99.0, 0.0],
     [-59.4, 0.0, 24.0, 13.2, 98.0]])

            b = np.array([[200.5],[-64.4],[-95.1],[-40.7], [12.6]])
        },
        
        # 5.1.19
        {
            A = np.array([[39.6, 0.0,17.5,9.9, 12.0],
     [79.2, 120.0, 0.0, 39.6, 0.0],
     [19.8, -21.0, 46.0, 0.0, 5.0],
     [49.5, 19.0, 19.0, 89.1, 0.0],
     [9.9, 25.0, 10.0, -39.6, 85.0]])

            b = np.array([[-34.35],[-530],[102.1],[-286.5], [101.3]])
        },
        # 5.1.20
        {
            A = np.array([[99.0, 28.0,0.0,69.3, 0.0],
     [49.5, -94.0, 3.0, -29.7, 10.0],
     [39.6, 24.0, -96.0, -29.7, 0.0],
     [29.7, 24.0, 23.0, 79.2, 0.0],
     [69.3, 0.0, 21.0, -3.3, -98.0]])

     b = np.array([[-58.7],[-156.9],[-405.5],[239.6],[-306.5]])
        },
        
        # 5.1.21
        {
            A = np.array([[7.92, 3.36, -2.24, 1.98],
     [-13.86 , 18.20, 0.0, 3.96],
     [-2.97, 0.20, 4.80, 0.0],
     [5.94, 0.0, -10.60, 16.83]])

            b = np.array([[14.556],[-100.54],[-1.27],[-71.31]])
        },
        
        # 5.1.22
        {
            A = np.array([[4.95, 1.12, 2.9, 0.66],
     [8.91, 19.9, -4.0, 6.93],
     [-2.97, 2.2, -5.8, 0.0],
     [5.94, 1.3, 10.5, 17.82]])

            b = np.array([[-31.024],[-37.81],[28.58],[9.32]])
        },

        # 5.1.23
        {
            A = np.array([[118.8, -14.0, -5.0, -89.1],
     [-59.4, 194.0, 5.0, 128.7],
     [148.5, 12.0, -310.0, 148.5],
     [0.0, 18.5, 90.0,-108.9]])

            b = np.array([[451.5],[-1158.3],[5700],[-2060.7]])
        },        
        
        # 5.1.24
        {
            A = np.array([[118.8, -14.0, -5.0, -89.1],
     [-14.85, -20.0, -5.0, 0.0],
     [297.0, 16.0, 320.0, 0.0],
     [0.0, 6.0, -30.0, -36.3]])

            b = np.array([[943],[-80.7],[2602.8],[1.1]])
        },
                
        # 5.1.25
        {
            A = np.array([[49.5,12.52,16.12,19.80],
     [0.0, 27.1,1.64,23.76],
     [12.87,11.52, 40.0,-14.85],
     [0,4.32, 0.12, 6.27]])

            b = np.array([[-51.176],[101.46],[-178.846],[14.084]])
        },   
        
        # 5.1.26
        {
            A = np.array([[3.96, -1.5, 0.0,-0.99,-1.4,0.0],
     [3.96,18.3,1.6,6.93, 4.3,1.5],,
     [0.0, 4.6,-13.0,4.29,-1.4 ,2.3],
     [3.96,0.4,0.0,5.94,1.5,0.0],
     [ 5.94,3.1,3.4,0.99,14.4,0.9],
     [-2.97,-1.2 ,0.8,4.95,-2.7,12.7]])

            b = np.array([[11.95],[-64.89],[-38.57],[-23.82],[-84.83],[30.35]])
        },
                
        # 5.1.27
        {
            A = np.array([[9.9,3.0 , 4.0,0.0,1.3, 1.5],
     [1.98,9.8,0.8,5.94,0.42,-0.6],
     [3.96,-4.8,19.7,9.9,0.72 ,0.3],
     [1.98,1.2,1.1,6.93, 0.81,-1.2],
     [9.9,-7.5,2.1,-9.9,29.5,0.0],
     [-2.97,-1.2,0.8, 4.95, 2.7,12.7]])

            b = np.array([[72.45],[77.48],[31.33],[10.03],[-78.74],[64.22]])
        },
        
                        
        # 5.1.28
        {
            A = np.array([[2.97,0.4,0.3,1.98,0.0,0.1],
     [0.99,4.9,0.4,2.97,0.2,-0.3],
     [0.0,-1.8,6.6,3.3,0.6,0.8 ],
     [4.95,1.6,1.2,8.91,0.8,0.3],
     [1.98,-1.5,0.4,-1.98,6.1,0.0],
     [9.9,1.4,2.4,5.94,3.2,23.3]])

            b = np.array([[-10.45],[-8.28],[4.48],[-26.93],[11.82],[38.84]])
        },
        
        # 5.1.29
        {
            A = np.array([[5.94,0.8,0.6,-3.96,0.2,0.3],
     [2.97,6.4,0.0,-2.97,0.2,0.2],
     [2.97,3.5,8.7,1.98,0.2,0.0],
     [4.95,1.6,1.2,-8.91,0.8,0.3],
     [-0.99,2.5,1.1,-3.96,9.0,0.4],
     [5.94,1.4,2.4,0.0,3.2,13]])

            b = np.array([[22.08],[29.99],[38.7],[37.19], [36.74],[67.34]])
        },
        
        # 5.1.30
        {
            A = np.array([[0.33,0.1,0.1,0.0,0.02,0.1],
     [0.99,4.9,0.4,2.97,0.21,-0.3],
     [1.32,-1.6,6.6,3.3,0.24,0.1],
     [1.98,1.2,1.1,6.93,0.81,-1.2],
     [1.98,-1.5,0.4,-1.98,6.1,0.0],
     [0.99,0.4,0.3,1.65,0.9,4.3]])

            b = np.array([[0.94],[18.68],[12.50],[5.56],[-10.28],[12.29]])
        }
    ]
}

