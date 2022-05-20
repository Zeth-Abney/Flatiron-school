
# Logistic Regression in scikit-learn - Lab

## Introduction 

In this lab, you are going to fit a logistic regression model to a dataset concerning heart disease. Whether or not a patient has heart disease is indicated in the column labeled `'target'`. 1 is for positive for heart disease while 0 indicates no heart disease.

## Objectives

In this lab you will: 

- Fit a logistic regression model using scikit-learn 


## Let's get started!

Run the following cells that import the necessary functions and import the dataset: 


```python
# Import necessary functions
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
```


```python
# Import data
df = pd.read_csv('heart.csv')
df.head()
```

## Define appropriate `X` and `y` 

Recall the dataset contains information about whether or not a patient has heart disease and is indicated in the column labeled `'target'`. With that, define appropriate `X` (predictors) and `y` (target) in order to model whether or not a patient has heart disease.


```python
# Split the data into target and predictors
y = None
X = None
```

## Normalize the data 

Normalize the data (`X`) prior to fitting the model. 


```python
# Your code here
X = None
X.head()
```

## Train- test split 

- Split the data into training and test sets 
- Assign 25% to the test set 
- Set the `random_state` to 0 


```python
# Split the data into training and test sets
X_train, X_test, y_train, y_test = None
```

## Fit a model

- Instantiate `LogisticRegression`
  - Make sure you don't include the intercept  
  - set `C` to a very large number such as `1e12` 
  - Use the `'liblinear'` solver 
- Fit the model to the training data 


```python
# Instantiate the model
logreg = None

# Fit the model

```

## Predict
Generate predictions for the training and test sets. 


```python
# Generate predictions
y_hat_train = None
y_hat_test = None
```

## How many times was the classifier correct on the training set?


```python
# Your code here

```

## How many times was the classifier correct on the test set?


```python
# Your code here

```

## Analysis
Describe how well you think this initial model is performing based on the training and test performance. Within your description, make note of how you evaluated performance as compared to your previous work with regression.


```python
# Your analysis here
```

## Summary

In this lab, you practiced a standard data science pipeline: importing data, split it into training and test sets, and fit a logistic regression model. In the upcoming labs and lessons, you'll continue to investigate how to analyze and tune these models for various scenarios.
