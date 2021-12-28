
# Understanding Pandas Series and DataFrames - Lab

## Introduction

In this lab, let's get some hands-on practice working with data cleanup using Pandas.

## Objectives
You will be able to:

- Use the `.map()` and `.apply()` methods to apply a function to a pandas Series or DataFrame 
- Perform operations to change the structure of pandas DataFrames 
- Change the index of a pandas DataFrame 
- Change data types of columns in pandas DataFrames 

## Let's get started! 

Import the file `'turnstile_180901.txt'`. 


```python
# Import the required libraries
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
```


```python
# Import the file 'turnstile_180901.txt'
df = pd.read_csv('turnstile_180901.txt')

# Print the number of rows ans columns in df
print(df.shape)

# Print the first five rows of df
df.head()
```

Rename all the columns to lower case: 


```python
# Rename all the columns to lower case

```

Change the index to `'linename'`: 


```python
# Change the index to 'linename'

```

Reset the index: 


```python
# Reset the index

```

Create another column `'Num_Lines'` that is a count of how many lines pass through a station. Then sort your DataFrame by this column in descending order. 

*Hint: According to the [data dictionary](http://web.mta.info/developers/resources/nyct/turnstile/ts_Field_Description.txt), LINENAME represents all train lines that can be boarded at a given station. Normally lines are represented by one character. For example, LINENAME 456NQR represents trains 4, 5, 6, N, Q, and R.*


```python
# Add a new 'num_lines' column

```

Write a function to clean column names: 


```python
def clean(col_name):
    # Clean the column name in any way you want to. Hint: think back to str methods 
    cleaned = None
    return cleaned
```


```python
# Use the above function to clean the column names

```


```python
# Check to ensure the column names were cleaned
df.columns
```

- Change the data type of the `'date'` column to a date 
- Add a new column `'day_of_week'` that represents the day of the week


```python
# Convert the data type of the 'date' column to a date


# Add a new column 'day_of_week' that represents the day of the week 

```


```python
# Group the data by day of week and plot the sum of the numeric columns
grouped = df.groupby('day_of_week').sum()
grouped.plot(kind='barh')
plt.show()
```

- Remove the index of `grouped` 
- Print the first five rows of `grouped` 


```python
# Reset the index of grouped
grouped = None

# Print the first five rows of grouped

```

Add a new column `'is_weekend'` that maps the `'day_of_week'` column using the dictionary `weekend_map` 


```python
# Use this dictionary to create a new column 
weekend_map = {0:False, 1:False, 2:False, 3:False, 4:False, 5:True, 6:True}

# Add a new column 'is_weekend' that maps the 'day_of_week' column using weekend_map
grouped['is_weekend'] = grouped['day_of_week'].map(weekend_map)
```


```python
# Group the data by weekend/weekday and plot the sum of the numeric columns
wkend = grouped.groupby('is_weekend').sum()
wkend[['entries', 'exits']].plot(kind='barh')
plt.show()
```

Remove the `'c/a'` and `'scp'` columns. 


```python
# Remove the 'c/a' and 'scp' columns
df = None
df.head(2)
```

## Analysis Question 

What is misleading about the day of week and weekend/weekday charts you just plotted?


```python
# Your answer here 
```

## Summary

Great! You practiced your data cleanup skills using Pandas.
