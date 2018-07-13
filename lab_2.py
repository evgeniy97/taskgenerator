# -*- coding: utf-8 -*-
"""
Numerical Methods, year 3, lab 2
"""
from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import sympy as sy
from sympy import Rational as syR
from sympy import exp, sin, cos, sqrt, log, ln
from sympy import pi, cot, sinh, cosh, atan, tan

from abstract_problem import AbstractProblem


# Define several named constants, to lighten formulas; XXX: are these useful?
sq2, sq3 = sy.sqrt(2), sy.sqrt(3)
half, quarter = sy.Rational(1, 2), sy.Rational(1, 4)


class Problem1(AbstractProblem):
    tag = "nm_yr3lab2q2.1"

    text = r"""Даны два уравнения  $f(x)=0$ и $g(x)=0$. Найти с точностью $\epsilon = 10e(-10)$ все корни уравнений,
	содержащиеся на отрезке $[a, b]$. Для решения  задачи использовать  метод бисекции.  Найти корни с помощью встроенной функции root пакета  MATHCAD. 
    ПОРЯДОК  РЕШЕНИЯ  ЗАДАЧИ:
	1. Найти аналитическое решение уравнения  $f(x)=0$.
	2. Используя пакет  MATHCAD, локализовать корни  $f(x)=0$  графически.
	3. Используя программу  bisec (см. ПРИЛОЖЕНИЕ 2.B),  найти корни уравнения $f(x)=0$  с точностью $\epsilon$ с помощью метода бисекции.
	4. Используя  встроенную функции root пакета   MATHCAD, найти корни уравнения $f(x)=0$ с точностью $\epsilon$.
	5. Аналогично п. 1-4 попытаться найти корни уравнения  $g(x)=0$. Объяснить полученные результаты.
	"""

    variants = [
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
    ]
    

class Problem2(AbstractProblem):
    tag = "nm_yr3lab2q2.2"

    text = r"""Найти указанный в варианте корень уравнения $f(x)=0$
	с точностью $\epsilon = 10^{-6}$, двумя способами.
	а) Использовать метод бисекции. Предварительно определить отрезок локализации $[a, b]$.
	б) Используя метод Ньютона. В качестве начального приближения взять середину
	отрезка локализации $[a, b]$.
	"""

    variants = [
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
    ]
	
class Problem3(AbstractProblem):
	
	text = r"""Локализовать корни уравнения $f(x)=0$ 
	и найти их с точностью $\epsilon = 10^{-5}$, используя метод простой итерации... """
	
	variants = [
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
class Problem4(AbstractProblem):

	text = r"""Локализовать корни уравнения $f(x)=x^5 + a_4x^4 + a_3x^3 + a_2x^2 + a_1x + a_0 $. 
			Найти их с точностью $\epsilon = 10^{-8}$,
			используя методы простой итерации и Ньютона.  
			Сравнить скорость сходимости  методов (по числу итераций). """
			
	variants = [
		# 2.4.1
		{'a4': 4.545004,
		 'a3': -3.055105,
		 'a2': -18.06895,
		 'a1': 4.002429,
		 'a0': 4.722482},
		# 2.4.2
		{'a4': -2.656764,
		 'a3': -3.406111,
		 'a2': 10.89372,
		 'a1': -1.752935,
		 'a0': -3.423612},
		# 2.4.3
		{'a4': -4.556062,
		 'a3': 2.93309,
		 'a2': 9.274868,
		 'a1': -10.32081,
		 'a0': 0.422098},
		# 2.4.4
		{'a4': 7.809249,
		 'a3': 16.28542,
		 'a2': -2.771356,
		 'a1': -27.95304,
		 'a0': -11.33921},
		# 2.4.5
		{'a4': -13.0072,
		 'a3': 60.24546,
		 'a2': -122.0716,
		 'a1': 105.6798,
		 'a0': -30.19201}, 
	
	]
	
class Problem5(AbstractProblem):
	
	text = r""" . Найти  приближенно корень уравнения $f(x)=0$, принадлежащий отрезку $[a,b]$, 
	с точностью $\epsilon = 10^{-5}$ , используя модификацию* метода Ньютона для случая кратного корня 
	при значениях $m=1,2,3,4,5$. По числу итераций определить кратность корня."""
	
	variants = [
		# 2.5.1
		{'f': lambda x: 36*cos(x) + 18*sqrt(3)*x + 9*x**2 + pi**2 - 18 - 6*sqrt(3)*pi - 6*pi*x,
		 'a': 0.8, 'b': 1.2,
             'd_f': lambda x: -36*sin(x)+ 18*sqrt(3) + 18*x - 6*pi},
		# 2.5.2
		{'f': lambda x: 144*sin(x) + 12*sqrt(3)*pi + 36*x**2 + pi**2 - 72 -12*pi*x - 72*sqrt(3)*x,
		 'a': 0.3, 'b': 0.7,
             'd_f': lambda x: 144*cos(x) +72*x - 12*pi - 72*sqrt(3) },
		# 2.5.3
		{'f': lambda x: 32*sqrt(2)*sin(x) + 8*pi + 16*x**2 + pi**2 - 32 - 8*pi*x - 32*x,
		 'a': 0.5, 'b': 1,
              'd_f': lambda x: -36*sqrt(2)*cos(x) + 32*x - 8*pi - 32},
		# 2.5.4
		{'f': lambda x: cot(x) + 2*x + pi*x - 1 - (pi/ 2) - 2*x**2 - (pi**2/ 8),
		 'a': 0, 'b': 1,
              'd_f': lambda x: -1/sin(x)**2 + 2 +pi - 4*x },
		# 2.5.5 
		{'f': lambda x: sqrt(3)*cot(x) + 4*sqrt(3)*x + 4*pi*x - 3 - (2*pi/ sqrt(3)) - 12*x**2 - (pi**2/ 3),
		 'a': 0, 'b': 0.7,
              'd_f': lambda x: -sqrt(3)/sin(x)**2 + 4*sqrt(3) + 4*pi - 24*x}
	]

class Problem6(AbstractProblem):
	
	text = r""" Локализовать корни уравнения $f(x)=0$.  Найти их с точностью $\epsilon = 10^{-5}$ и $\epsilon = 10^{-12}$  ,
			используя метод  Ньютона и метод, указанный в индивидуальном варианте.  
			Сравнить скорость сходимости  методов (по числу итераций) для каждого значения  ."""
	
	variants = [
		# 2.6.1
		{'f': lambda x: exp(x) - 3*sqrt(x),
		 'method': 'упрощенный метод Ньютона'
		},
		# 2.6.2
		{'f': lambda x: sqrt(2 - x**2) - exp(x),
		 'method': 'метод ложного положения'
		},
		# 2.6.3
		{'f': lambda x: ln(x) - 2*cos(x),
		 'method': 'метод простой итерации'
		},
		# 2.6.4
		{'f': lambda x: sqrt(x)*exp(cos(x)) - 1,
		 'method': 'метод секущих'
		},
		# 2.6.5
		{'f': lambda x: exp(-(x+1)) + x**2 +2*x - 1,
		 'method': 'метод Стеффенсена'
		}
	]

class Problem7(AbstractProblem):

	text = r"""Локализовать корни уравнения $f(x)=0$. Найти их с точностью $eps = 10^{-5}$ и $eps = 10^{-12}$,
	используя метод  Ньютона, упрощенный метод Ньютона и метод секущих**. 
	Сравнить скорость сходимости  методов (по числу итераций) для каждого значения $\epsilon$ . """
	
	variants = [
		# 2.7.1
		{'f': lambda x: x*ln(x) - x**2 + 3*x - 1},
		# 2.7.2
		{'f': lambda x: x**3 - 0.9*x**2 - x - 0.1},
		# 2.7.3
		{'f': lambda x: exp(-x) - 5*x + 10*x},
		# 2.7.4
		{'f': lambda x: ln(2*x - x**2) + 2 - sqrt(x)},
		# 2.7.5
		{'f': lambda x: sqrt(x) - x**2 - 10}
	]
	
class Problem8(AbstractProblem):

	text = r"""Найти приближенно все (в том числе комплексные) корни уравнения $f(x)=0$ с точностью $\epsilon = 10^{-5}$,
	используя метод  Ньютона. 
	УКАЗАНИЕ. Для поиска комплексных корней следует использовать комплексные начальные приближения. """
	
	variants = [
		#2.8.1
		{'f': lambda x: x**3 - 2*x - 5},
		#2.8.2
		{'f': lambda x: x**4 - 2.7*x**3 + 3},
		#2.8.3
		{'f': lambda x: x**4 - 2.7*x**3 + x - 1},
		#2.8.4
		{'f': lambda x: x**5 + 3*x**4 + 2*x**3 - 1},
		#2.8.5
		{'f': lambda x: x**5 + 2*x**4 + 4*x**3 - 5*x + 2.7}		
	]
	
class Problem9(AbstractProblem):

	text = r""". a) Локализовать корни уравнения $f(x)=0$. Уточнить их с точностью $\epsilon = 10^{-7}$,
	используя метод Ньютона. Для поиска кратного корня и определения его кратности следует использовать 
	модификацию метода Ньютона для случая кратного корня с $m=1,2,3$. 
	При любых ли начальных приближениях такой метод сходится?  """
	
	variants = [
		# 2.9.1
		{'f': lambda x: 3*x**3 - 77*x**2 + 605*x - 1331},
		# 2.9.2
		{'f': lambda x: 3*x**3 - 35*x**2 + 125*x - 125},
		# 2.9.3
		{'f': lambda x: x**3 - 7*x**2 + 15*x - 9},
		# 2.9.4
		{'f': lambda x: x**3 - 5.5*x**2 + 9.5625*x - 5.0625},
		# 2.9.5
		{'f': lambda x: 3*x**3 - 28*x**2 + 80*x - 64},
	]
	
class Problem10(AbstractProblem):
	text = r"""Функция $y=f(x)$ задана неявно уравнением $F(x,y)=0$. 
	На отрезке $[1, 5]$ построить таблицу значений функции $y=f(x)$ с шагом $h=0.5$, 
	применяя один из методов численного решения нелинейного уравнения (с точностью  ). 
	Построить график функции $y=f(x)$ на заданном отрезке """
	
	variants = [
		#2.10.1
		{'f': lambda x: sinh(y*exp(y)+x/20) + atan(20*y*exp(y) - x) - 0.5,
		 'x_lower': 1, 'x_upper': 5,
		 'y_lower': 0.1, 'y_upper': 1.2
		 },
		#2.10.2
		{'f': lambda x: cosh(y*exp(y) + x/20) + 1/atan(20*y*exp(y) + x) - 13,
		 'x_lower': 1, 'x_upper': 5,
		 'y_lower': 1, 'y_upper': 1.5
		 },
		#2.10.3
		{'f': lambda x: exp(x*y) - cos(x*y**3),
		 'x_lower': 0.5, 'x_upper': 1.5,
		 'y_lower': -1.3, 'y_upper': -0.3
		 },
		#2.10.4
		{'f': lambda x: exp(x*y) - cos(x*y**(syR(1,3))),
		 'x_lower': 4.5, 'x_upper': 7.2,
		 'y_lower': -1.2, 'y_upper': -0.2
		 },
		#2.10.5
		{'f': lambda x: ln(x*y) - sin(y*x**2), 
		 'x_lower': 1, 'x_upper': 2.5,
		 'y_lower': 0.5, 'y_upper': 2.5
		 },
	]

