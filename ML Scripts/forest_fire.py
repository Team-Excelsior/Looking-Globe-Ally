import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from keras.models import Sequential
import keras.optimizers as opti
from keras.layers import Dense, Activation,Dropout

df = pd.read_csv('forestfires.csv')
df['Log-area']=np.log10(df['area']+1)
for i in df.describe().columns[:-2]:
    print(df.plot.scatter(i,'Log-area',grid=True))
df.boxplot(column='Log-area',by='day')
df.boxplot(column='Log-area',by='month')

enc = LabelEncoder()
enc.fit(df['month'])
print(enc.classes_)


df['month_encoded']=enc.transform(df['month'])
print(df.head())
enc.fit(df['day'])
print(enc.classes_)
df['day_encoded']=enc.transform(df['day'])
print(df.head(15))

test_size=0.4
X_data=df.drop(['area','Log-area','month','day'],axis=1)
y_data=df['Log-area']

X_train, X_test, y_train, y_test = train_test_split(X_data, y_data, test_size=test_size)
y_train=y_train.reshape(y_train.size,1)

model = Sequential()
model.add(Dense(100, input_dim=12))
model.add(Activation('selu'))
model.add(Dropout(0.3))
model.add(Dense(100))
model.add(Dropout(0.3))
model.add(Activation('selu'))
model.add(Dense(50))
model.add(Activation('elu'))
model.add(Dense(1))
print(model.summary())


learning_rate=0.001
optimizer = opti.RMSprop(lr=learning_rate)
model.compile(optimizer=optimizer,loss='mse')

data=X_train
target = y_train
model.fit(data, target, epochs=100, batch_size=10,verbose=0)

a=model.predict(X_test)
print("RMSE for Deep Network:",np.sqrt(np.mean((y_test-a.reshape(a.size,))**2)))