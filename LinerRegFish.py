Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> '''
ISA taskphase: linear Regression
dataset:https://www.kaggle.com/aungpyaeap/fish-market/
'''
import pandas as pd                 # Importing linear algebra
import numpy as np                  # Imported for processing data

fr= open("FishList.csv","r")            #opens file
data_df = pd.read_csv(fr)               #reads the data from datasheet

#print(data_df.head())              # this line prints the first 5 rows

# dependent variable is Species
# indpendent variables are Weight Length1, Length2, Length3, Height, Width

fish_map = {'Bream':1 , 'Roach':2, 'Whitefish':3, 'Parkki':4, 'Perch':5, 'Pike':6, 'Smelt':7}
        #giving an int value to the type of fish

data_df = data_df.replace(to_replace=fish_map)

col_name = data_df.columns[0]
data_df.rename(columns={col_name:'Species'},inplace=True)


x= np.array(data_df.drop(['Species'],1))
y= np.array(data_df['Species'])

#spliting the data into training and test set
from sklearn.model_selection import train_test_split
x_train, x_test,y_train, y_test= train_test_split(x,y,test_size=0.3,random_state=0)


#training the model on the training set
from sklearn.linear_model import LinearRegression
ml=LinearRegression()
ml.fit(x_train, y_train)

#predicting the test set results
y_pred= ml.predict(x_test)


#plot the results
import matplotlib.pyplot as plt

plt.scatter(y_test,y_pred)
plt.xlabel("actual")
plt.ylabel("predicted")
plt.title("actual vs predicted")
plt.show()







