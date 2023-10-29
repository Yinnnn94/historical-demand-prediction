import pandas as pd
import numpy as np
from datetime import datetime as dt_dt
import datetime as dt

data = pd.read_csv(r"Historical Product Demand.csv")
data = data.dropna()
path_of_combination = r"Historical Product Demand_combine_with_date.csv"
# Combine same date data 
def combine_data_by_date(data, path_of_combination):
    date_object = [dt_dt.strptime(i,'%Y/%m/%d').date() for i in data['Date']]
    data['Date'] = date_object
    pp = data['Product_Code'].value_counts().index
    new_data_list = []

    for p in pp[:5]:
        new_data = pd.pivot_table(data[data['Product_Code'] == p], values='Order_Demand', index='Date',
                                  aggfunc={'Order_Demand': ['sum', 'mean', 'count']})
        
        if not new_data.empty:
            for d, c, m, s in zip(new_data.index, new_data['count'].values, new_data['mean'].values, new_data['sum'].values):
                new_data_list.append([d, p, c, m, s])

    new_data_arr = np.array(new_data_list)
    new_data_column = ['Date', 'Product', 'Demand_count', 'Demand_mean', 'Demand_sum']
    new_data = pd.DataFrame(new_data_arr, columns=new_data_column)
    new_data['Year'] = [i.year for i in new_data['Date']]
    new_data['Month'] = [i.month for i in new_data['Date']]
    new_data['Week'] = [i.weekday() + 1 for i in new_data['Date']]
    new_data.to_csv(path_of_combination)
    return new_data

combined_data = combine_data_by_date(data, path_of_combination)

def generate_pred_data():
    pp = data['Product_Code'].value_counts().index
    data_2012_1359 = combined_data[(combined_data['Product'] == pp[0]) & (combined_data['Year'] == 2012)]
    half_6_month = data_2012_1359.loc[(data_2012_1359['Date'] >= dt.date(2012, 1,1)) & (data_2012_1359['Date'] < dt.date(2012, 6,30))][['Date', 'Demand_sum']]
    target = data_2012_1359[data_2012_1359['Month'] == 7][['Date', 'Demand_sum']]
    return half_6_month, target