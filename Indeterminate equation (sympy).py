import sympy
from sympy.solvers.diophantine import diophantine
from sympy import symbols

# 記号x,y,tを定義
x, y, z = symbols('x、y、z', integer = True)

# 3x+2y=5の解
diophantine(2*x + 3*y - 5)
