# -*- coding: utf-8 -*-
from sympy import *
from sympy.parsing.sympy_parser import parse_expr
from sympy.plotting import plot
from math import exp

x = symbols('x')

y1 = parse_expr('(x ** 2 + cos(x)) / 4')

y2 = parse_expr('cos(x)/(4-x)')

y3 = parse_expr('x ** 3 - x ** 2 *5 + 7 * x - 3')

y4 = parse_expr('x ** 3 - x ** 2 * 0.25 + 0.75 * x - 2')

y5 = parse_expr('sin(x) - exp(1) ** x')

y6 = parse_expr('exp(1) ** x - x ** 2 * 4')

p1 = plot (y1, show=False)
p1.show()

p2 = plot (y2, show=False)
p2.show()

p3 = plot (y3, show=False)
p3.show()

p4 = plot (y4, show=False)
p4.show()

p5 = plot (y5, show=False)
p5.show()

p6 = plot (y6, show=False)
p6.show()