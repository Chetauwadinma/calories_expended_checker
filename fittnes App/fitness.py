#fitness prediction model

# import the libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import warnings
warnings.filterwarnings('ignore')
import pickle
#import dataset
df1 = pd.read_csv(r"C:\Users\HomePC\Desktop\calories pred app\calories.csv")
df2 = pd.read_csv(r"C:\Users\HomePC\Desktop\calories pred app\exercise.csv")

#merge both dataset
df = pd.merge(df1,df2, on = "User_ID")

# choose target and dependent variable
y = df["Calories"].values # target var
x = df[["Duration","Heart_Rate","Body_Temp"]] # dependent var

#  split the data into training and testing set
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=22)

lr = LinearRegression()
# fit the model into the dataset
model = lr.fit(x_train, y_train)
# check fittedness
model
# save the model with pickle
import pickle # import lib
# open pickle an d save the shit
with open('fitness.pkl', 'wb') as file:
    pickle.dump(model, file)