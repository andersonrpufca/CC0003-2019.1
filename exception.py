#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 10:40:48 2019

@author: ufca
"""

try:
    valor = int(input()) / int(input())
except ZeroDivisionError:
    print('ai dento')
except Exception as e:
    print('outra coisa: ', e)
else:
    print(valor)
finally:
    print("morreu maria preá")