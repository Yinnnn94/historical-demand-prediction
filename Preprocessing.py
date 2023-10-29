import pandas as pd
import numpy as np
from datetime import datetime as dt


# Combine same date data 
def combine_data_by_date(data):
    date_object = [dt.strptime(i,'%Y/%m/%d').date() for i in data['Date']]
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
    return new_data