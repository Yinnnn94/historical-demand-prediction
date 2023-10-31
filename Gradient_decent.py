import sympy as sp
import random as r
import numpy as np
import matplotlib.pyplot as plt
def f(w, x, b):
    return w * x + b

def mse(y_pred_list, y_label_list):
    e = (y_label_list - y_pred_list) ** 2
    return sum(e)/len(e) 

def gradient_decent(x, iteration, lr):
    # random initial the paratmeter
    current_w = 0.5
    current_b = 0.2
    param = []
    cost = []
    n = len(x)
    
    for i in range(iteration): # number of iteration 
        y_pred = f(current_w, x,current_b)
        if i > 0 and abs(mse(x, y_pred) - cost[-1]) < 1e-5:
            break
        else:
            cost.append(mse(x, y_pred))
            dw = -(1/2*n) * sum(x * (x - y_pred))
            db = -(1/2*n) * sum(x - y_pred)
            current_w = current_w - (lr * dw)
            current_b = current_b - (lr * db)
            param.append([current_w, current_b])
    plt.plot(cost)
    plt.show()
    print(f'smallest cost:{min(cost)},parameter:{cost.index((min(cost)))}')
    return cost, param
    