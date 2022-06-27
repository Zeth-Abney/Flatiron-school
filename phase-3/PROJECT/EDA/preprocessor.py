"""
The purpose of this py file is to facilitate prototyping and optimizing, and make portable (between notebooks) 
the preprocessing workflow, that I will be developing throughout this project. 

The code in this script is custom to the tabular data available in the directory "data/" in this repository
"""

from ast import Pass
from matplotlib.pyplot import axis, table
import pandas as pd
import numpy as np

# column names of all features with data from the customer survey
survey_labels = [
    'Inflight wifi service', 
    'Departure/Arrival time convenient',
    'Ease of Online booking', 
    'Gate location', 
    'Food and drink',
    'Online boarding', 
    'Seat comfort', 
    'Inflight entertainment', 
    'On-board service', 
    'Leg room service', 
    'Baggage handling', 
    'Checkin service', 
    'Inflight service', 
    'Cleanliness']

def data_cleaner(file_path: str):
    df = pd.read_csv(file_path,compression='zip',index_col=0)
    df.drop('id',axis=1,inplace=True)

    # handle NaNs in arrival delay
    df['Arrival Delay in Minutes'].replace({np.NaN:0},inplace=True)
    
    # define X below
    X = df.drop('Customer Type',axis=1)
    X = pd.get_dummies(X,drop_first=True)

    

    # imputes any zeros in the survey as the mode of the surveyee's other answers.
    survey_test = X[survey_labels]
    for row in survey_test.iterrows():
        zero_bool = (row[1]==0).sum()
        row_mode = row[1].aggregate(func='mode')
        if zero_bool > 0:
            survey_test.iloc[row[0]].replace(0,row_mode[0],inplace=True)
    for col in survey_labels:
        X[col]=survey_test[col]

    # define y below
    y = df['Customer Type']
    y = pd.get_dummies(y,drop_first=True)['disloyal Customer'] # 1 = disloyal
    
    return X,y