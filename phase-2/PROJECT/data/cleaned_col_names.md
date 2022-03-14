# Column Names and Descriptions for Cleaned data set

* `id` - Unique identifier for a house
* `date` - Date house was sold
* `price` - Sale price (prediction target)
* `bedrooms` - Number of bedrooms
* `bathrooms` - Number of bathrooms
* `sqft_living` - Square footage of living space in the home
* `sqft_lot` - Square footage of the lot
* `floors` - Number of floors (levels) in house
* `condition` - {'Poor':1,'Fair':2,'Average':3,'Good':4,'Very Good':5}
* `grade` - {1, 3, 4, 5, 6, 7, 8, 9}
    - <= 5 does not meet code
    - 6-8 barely meets code to just about average
    - 9-10 high quality homes
    - 11 -> custom, luxury homes. 
* `sqft_above` - Square footage of house apart from basement
* `sqft_basement` - Square footage of the basement
* `yr_built` - Year when house was built
* `zipcode` - ZIP Code used by the United States Postal Service
* `sqft_living15` - The square footage of interior housing living space for the nearest 15 neighbors
* `sqft_lot15` - The square footage of the land lots of the nearest 15 neighbors
* `age` - days since it was built
* `day_of_year` - date on a scale of 365
* `bed_bath_ratio` - ratio of bedrooms to bathrooms
* `level_ratio` - ratio of sqft above grade to below grade
* `relative_living_space` - sqft relative to nearest 15 houses
* `relative_lot_size` - sqft relative to nearest 15 houses
* `level_difference` - difference between sqft_above and sqft basement.


First linreg model:
 p_value > .05 
 ()
- sqft_lot
- sqft_above *
- sqft_basement *
- yr_built 
- sqft_lot15
- age
- relative_living_space *
- relative_lot_size 

* adjust for outliers???

Variance inflation factors:
(age,day_of_year,level_ratio)
{'bedrooms': 58.32118384194414, 
 'bathrooms': 57.84054290751994,
 'sqft_living': inf,
 'sqft_lot': inf,
 'floors': 15.926052423084142,
 'condition': 27.9388737465139,
 'grade': 13.70204366610633,
 'sqft_above': inf,
 'sqft_basement': inf,
 'sqft_living15': inf,
 'sqft_lot15': inf,
 'age': 6.881296527889314, *******************
 'day_of_year': 4.6860289878245736, ***************
 'bed_bath_ratio': 30.0137067238,
 'level_ratio': 1.3218881314724718, ****************
 'relative_living_space': inf,
 'relative_lot_size': inf,
 'level_difference': inf}
 
 * good ( x <= 5)
 ~ maybe ( 6 <= X <= 9)
 ! no good (X => 10)
