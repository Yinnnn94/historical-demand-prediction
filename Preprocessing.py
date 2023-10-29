import pandas as pd
import numpy as np
from datetime import datetime as dt
data = pd.read_csv(r"Historical Product Demand.csv")
data = data.dropna()
date_object = [dt.strptime(i,'%Y/%m/%d').date() for i in data['Date']]
data['Date'] = date_object
# Combine same date data 
def combine_data_by_date(data): #Same product at same date will combine together
    pp = data['Product_Code'].value_counts().index
    new_data_arr = np.array([])
    new_data = pd.DataFrame()
    for p in pp[:5]:
        print(p)
        new_data = pd.pivot_table(data[data['Product_Code'] == p], values = 'Order_Demand', index = 'Date', 
                                  aggfunc = {'Order_Demand': ['sum', 'mean', 'count']})
        for d,c,m,s in zip(new_data.index, new_data['count'].values, new_data['mean'].values, new_data['sum'].values):
            new_data_arr = np.append(new_data_arr, [d,p,c,m,s])
    new_data_arr = new_data_arr.reshape(int(len(new_data_arr)/5), 5)
    return new_data_arr
# new_data['Date'] = list(new_data_arr[:,0])
# new_data['Product'] = list(new_data_arr[:,1])
# new_data['Demand_count'] = list(new_data_arr[:,2])
# new_data['Demand_mean'] = list(new_data_arr[:,3])
# new_data['Demand_sum'] = list(new_data_arr[:,4])
# new_data['Year'] = [i.year for i in new_data['Date']]
# new_data['Month'] = [i.month for i in new_data['Date']]
# new_data['Week'] = [i.weekday() +1 for i in new_data['Date']]
# new_data
combine_data_by_date(data)