import sympy as sp
import random as r
import numpy as np

def f(w,b,x):
    return w * x + b

def mse(y_pred_list, y_label_list):
    e = (y_label_list - y_pred_list) ** 2
    return sum(e)/len(e)

def gradient_decent(x, iteration, lr):
    current_w = r.randint(1,15)
    current_b = r.randint(1,15)
    costs = []
    weights = []
    for i in range(iteration):
        y_pred_list = [f(current_w, current_w, y_label) for y_label in x]

        # db=(np.sum(y_pred_list - x)*2)/len(y)
        # dw=(np.dot((y_pred_list- x),x)*2)/len(y)
        # current_cost = loss(x, y_pred_list)
#     return y_pred_list