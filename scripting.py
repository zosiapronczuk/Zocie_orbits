#hello
import numpy as np 
import matplotlib.pyplot as plt
from scipy import integrate


# The four first oder ODES
M_i = 3
def n(t):
    """returns the right hand side of the ODE"""
    return t/M_i

print(n(1))
