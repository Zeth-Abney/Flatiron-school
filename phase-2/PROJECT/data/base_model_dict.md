# Column Names and Descriptions for Cleaned data set

* `price` - Sale price (prediction target)

* `date` - Date house was sold, in days since year 0 day 1 (see pandas toordinal method)
* `floors` - Number of floors (levels) in house
* `waterfront` - boolean indicating proximity to a waterfront
* `view` - quality of view on 5 point scale (0-4)
* `condition` - {'Poor':1,'Fair':2,'Average':3,'Good':4,'Very Good':5}
* `sqft_basement` - Square footage of the basement
* `yr_built` - Year when house was built
* `yr_renovated` - 4-digit year of renovation. 0.0 if no data or hasn't been renovated
* `bed_bath_ratio` - ratio of bedrooms to bathrooms
* `level_ratio` - ratio of sqft above grade to below grade
* `live_lot_ratio` - ratio of square footage of living space to square footage of the lot
* `relative_living_space` - sqft relative to nearest 15 houses
* `relative_lot_size` - sqft relative to nearest 15 houses
* `level_difference` - difference between sqft_above and sqft basement.
* `waterfront_Duwamish, waterfront_Elliott Bay. waterfront_Lake Sammamish, waterfront_Lake Union, waterfront_Lake Washington, waterfront_Puget Sound` - one-hot encoded booleans indicating if property is located at that specific waterfront. (some waterfront properties are not at any of these waterfronts in which case waterfront will be 1 but all of these columns will be 0's) 
