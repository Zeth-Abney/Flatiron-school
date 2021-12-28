# Accessing Data within Pandas - Lab

## Introduction

In this lab, we'll look at a dataset which contains information on World Cup matches. Let's use the pandas commands learned in the previous lesson to learn more about our data!

## Objectives
You will be able to: 
- Use pandas methods and attributes to access information about a dataset 
- Index pandas dataframes with .loc, .iloc, and column names 
- Use a boolean mask to index pandas series and dataframes

## Load the Data

Load the file `'WorldCupMatches.csv'` as a DataFrame in pandas.


```python
# Replace None with appropriate code

# Import pandas using the standard alias
None

# Load 'WorldCupMatches.csv' as a DataFrame
df = None
```

## Common Methods and Attributes

Use the correct method to display the **first 7 rows** of the dataset.


```python
# Your code here
```

Display the **last 3 rows** of the dataset.


```python
# Your code here
```

Get a concise summary of the data using `.info()`. 


```python
# Your code here
```

Obtain a tuple representing the **number of rows and number of columns**.


```python
# Your code here
```

Use the appropriate attribute to get the **column names**.


```python
# Your code here
```

## Selecting DataFrame Information

When looking at the DataFrame's `.head()` and `.tail()`, you might have noticed that the games are structured chronologically in the DataFrame.

Use the right selection method to display all the information from the 3rd to the 5th game (i.e. **select rows 3 through 5 inclusive**).


```python
# Your code here
```

Now, display the info from **game 5-9** (inclusive), but **only the `"Home Team Name"` and the `"Away Team Name"` columns**.


```python
# Your code here
```

Next, we'd like the information on all the games played in **Group 3** for the **1950** World Cup.

Hint: You can combine conditions like this:

`df[(condition1) | (condition2)]`  -> Returns rows where either condition is true

`df[(condition1) & (condition2)]`  -> Returns rows where both conditions are true


```python
# Your code here
```

Let's repeat the command above, but this time display **only the attendance column** for the Group 3 games. 


```python
# Your code here
```

Throughout the entire history of the World Cup as recorded in this dataset, **how many home games were played by the Netherlands**?

(Remember that you can use the `len()` built-in function to find the number of rows in a DataFrame.)


```python
# Your code here
```

**How many games were played by the Netherlands in total**?


```python
# Your code here
```

Next, let's try and figure out **how many games the USA played in the 2014 World Cup**.


```python
# Your code here
```

Now, let's try to find out **how many countries participated in the 1986 World Cup**.

Hint 1: As a first step, create a new dataset that only contains games in that year.

Hint 2: Make sure you don't end up with duplicate country names. Consider using `set()` or `.unique()`.


```python
# Your code here
```

## Changing Values and Creating New Columns

In World Cup history, **how many matches had 5 goals or more in total**? Create a column `"Total Goals"` to answer this question.


```python
# Your code here
```

Now **create a new column `"Half-time Goals"`** in `df` that includes both home and away values.


```python
# Your code here
```


```python
# Run this cell without changes to see your new column
df.columns
```

Run the code below. You'll notice that for Korea, there are records for both North-Korea (Korea DPR) and South-Korea (Korea Republic). 


```python
# Run this cell without changes

# Diaplay all records containing the string 'Korea'
df.loc[df['Home Team Name'].str.contains('Korea'), 'Home Team Name']
```

Imagine that, for some reason, we simply want Korea listed as one entry, so we want to replace every "Home Team Name" and "Away Team Name" entry that contains "Korea" to simply "Korea". In the same way, we want to change the columns "Home Team Initials" and "Away Team Initials" to NSK (North & South Korea) instead of "KOR" and "PRK". 


```python
# Update the 'Home Team Name' and 'Home Team Initials' columns 

```

Make sure to verify your answer!


```python
# Check the updated columns

```

## Summary

In this lab, you practiced accessing data within Pandas!
