# -*- coding: utf-8 -*-
"""rock vs mine prediciton.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vfgDNzZtwIVQMURrdgP0ewFXKxh_eXAT

Importing dependencies
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

"""Data collection and pre-processing"""

#collection of data
sonar_data=pd.read_csv('/Copy of sonar data.csv',header=None)

#to print the starting 5 rows of the dataframe/dataset
sonar_data.head()

#print the number rows and column
sonar_data.shape

#to get the statistical measures about the data
sonar_data.describe()

#gives the number of instances in 'mine' and 'rock' in 60th column
sonar_data[60].value_counts()

"""M --> Mine
R --> Rock
"""

sonar_data.groupby(60).mean()

#split the data and lables
x=sonar_data.drop(columns=60, axis =1)
y=sonar_data[60]

print(x)
print(y)

"""train_test_split --> function to split the data set

x,y indicates they are getting splitted

test_size --> attribute to split the percentage of dataset into test

stratify --> attribute to specify, based on 'y' the dataset is splitted -- testa and train includes equal number of M and R.

random state --> data is splitted in specific order.
"""

x_train,x_test, y_train, y_test=train_test_split(x,y,test_size=0.1,stratify=y,random_state=1)

print(x.shape, x_train.shape, x_test.shape)

"""Model training --> Logistic Regression"""

model=LogisticRegression()

#training logistic regression model with training data
model.fit(x_train, y_train)

"""Model Evaluation"""

x_train_prediction=model.predict(x_train)
x_train_accuracy=accuracy_score(x_train_prediction,y_train)

print("Accuracy on training dataset : ",x_train_accuracy)

x_test_prediction=model.predict(x_test)
x_test_accuracy=accuracy_score(x_test_prediction,y_test)

print('Accuracy on test dataset : ',x_test_accuracy)

"""MAKING A PREDICTIVE SYSTEM"""

input_data=(0.0286,0.0453,0.0277,0.0174,0.0384,0.0990,0.1201,0.1833,0.2105,0.3039,0.2988,0.4250,0.6343,0.8198,1.0000,0.9988,0.9508,0.9025,0.7234,0.5122,0.2074,0.3985,0.5890,0.2872,0.2043,0.5782,0.5389,0.3750,0.3411,0.5067,0.5580,0.4778,0.3299,0.2198,0.1407,0.2856,0.3807,0.4158,0.4054,0.3296,0.2707,0.2650,0.0723,0.1238,0.1192,0.1089,0.0623,0.0494,0.0264,0.0081,0.0104,0.0045,0.0014,0.0038,0.0013,0.0089,0.0057,0.0027,0.0051,0.0062)

#changing the input data into numpy array
input_data_to_numpy_array=np.asarray(input_data)

#reshape the np array as we are predicting for one instance
input_data_reshaped=input_data_to_numpy_array.reshape(1,-1)

prediction=model.predict(input_data_reshaped)

print(prediction)

if(prediction[0]=='R'):
  print("The object is Rock")
else:
  print("The object is Mine")

