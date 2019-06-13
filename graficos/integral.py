#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 10:21:13 2019

@author: ufca
"""

from sympy import init_printing
from sympy import *
from sympy.parsing.sympy_parser import parse_expr

init_printing()
x = symbols('x')
y = parse_expr('(x**4)/2 - 5*x**3 + 20*x**2 - 1 + cos(x) / sin(x)')
pprint(y)

inty = Integral(y,x)
intey = integrate(y,x)
pprint(inty)

ponto = float(input('Digite o ponto: '))

valor = y.evalf(subs={x:ponto})
print(valor)
