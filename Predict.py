from Preprocessing import generate_pred_data
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from sklearn.preprocessing import StandardScaler
from keras.layers import LSTM, Dense, Activation
from sklearn.model_selection import train_test_split
import numpy as np


ss = StandardScaler()
preprpro_data = generate_pred_data() #x ,y
x = np.array(preprpro_data[['Demand_count', 'Demand_mean','Year', 'Month','Week']])
x_scaled = ss.fit_transform(x)
target_scaled = ss.fit_transform(preprpro_data['Demand_sum'].values.reshape(-1,1))
x_train, x_test, y_train, y_test = train_test_split(x_scaled, target_scaled, test_size = 0.2)
model = Sequential()
model.add(Dense(units = 10, input_dim = 5))
model.add(Activation('relu'))
model.add(Dense(units = 60))
model.add(Activation('sigmoid'))
model.compile(loss = 'mse', optimizer = 'adam')
model.summary()
history = model.fit(x_train, y_train, epochs = 100)
plt.plot(history.history['loss'])
plt.show()
