"""
The purpose of this py file is to facilitate prototyping and optimizing, and make portable (between notebooks) 
the preprocessing workflow, that I will be developing throughout this project. 

The code in this script is custom to the tabular data available in the directory "data/" in this repository
"""

from matplotlib.pyplot import axis, table
import pandas as pd
import numpy as np

from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import EditedNearestNeighbours
from imblearn.combine import SMOTEENN


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

# data preprocessing
def data_cleaner(file_path: str):
    # load raw data, ignore index and id collumns 
    df = pd.read_csv(file_path,compression='zip',index_col=0)
    df.drop('id',axis=1,inplace=True)

    # handle NaNs in arrival delay, replace numpy NaNs with numerical zeros
    df['Arrival Delay in Minutes'].replace({np.NaN:0},inplace=True)
    
    # define X below
    X = df.drop('Customer Type',axis=1)

    # one-hot-encode categoricals within X
    X = pd.get_dummies(X,drop_first=True)

    # imputes any zeros in the survey as the mode of the surveyee's other answers.
    survey = X[survey_labels] #slice only the survey feature
    for row in survey.iterrows(): 
        zero_bool = (row[1]==0).sum()
        row_mode = row[1].aggregate(func='mode')
        if zero_bool > 0:
            survey.iloc[row[0]].replace(0,row_mode[0],inplace=True) # if there is at least one zero, replace it with the mode of the row
    
    for col in survey_labels:
        X[col]=survey[col] # replace columns in X with respective columns in survey


    # define y below
    y = df['Customer Type']
    # one-hot-encode target
    y = pd.get_dummies(y,drop_first=True)['disloyal Customer'] # 1 = disloyal
    
    return X,y

# data resampling (SMOTEENN)
def data_sampler(X,y):
    smote = SMOTE()
    enn = EditedNearestNeighbours(sampling_strategy='majority')
    SMN = SMOTEENN(sampling_strategy='all',smote=smote,enn=enn,n_jobs=3)

    X_smn, y_smn = SMN.fit_resample(X,y)

    return X_smn,y_smn
