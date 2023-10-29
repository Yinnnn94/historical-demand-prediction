import pandas as pd
from Preprocessing import combine_data_by_date, generate_pred_data
import matplotlib.pyplot as plt

from Gradient_decent import f, mse, gradient_decent
# Using top1 data(2012.01 ~ 2012.06 to predict 2012.07)

half_6_month, target = generate_pred_data()

gradient_decent(half_6_month['Demand_sum'], 10, 0.01)
