# Column Names and Descriptions for Cleaned data set

* `price` - Sale price of the property (prediction target)

* `zip_tax_revenue` - The total amount of revenue from income tax for a given zipcode.
* `bathrooms` - The number of bathrooms in a given house.
* `lat` - The latitudinal degree a given property lies on.
* `view` - quality of view on 5 point scale (0-4)
* `sqft_living15` - The average square footage of living space for the 15 nearest other houses.
* `floors` - Number of floors (levels) in house
* `condition` - General condition of the property {'Poor':1,'Fair':2,'Average':3,'Good':4,'Very Good':5}
* `sqft_lot` - Total square footage of the lot
* `long` - Longitudinal degree that the property lies on
* `date` - Date house was sold, in days since year 0 day 1 (see pandas toordinal method)
* `bedrooms` - The number of bedrooms in the house.
* `yr_renovated` - The year that the house was renovated (if at all)
* `waterfront` - boolean indicating proximity to a waterfront
* `grade` - Condition of the property as well as level of luxury.
    {1, 3, 4, 5, 6, 7, 8, 9}
    - <= 5 does not meet code
    - 6-8 barely meets code to just about average
    - 9-10 high quality homes
    - 11 -> custom, luxury homes. 
* `waterfront_Duwamish, waterfront_Elliott Bay. waterfront_Lake Sammamish, waterfront_Lake Union, waterfront_Lake Washington, waterfront_Puget Sound` - one-hot encoded booleans (0/1) indicating if property is located at that specific waterfront. (some waterfront properties are not at any of these waterfronts in which case waterfront will be 1 but all of these columns will be 0's) 
