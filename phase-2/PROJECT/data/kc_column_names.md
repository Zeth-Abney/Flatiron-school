# Column Names and Descriptions for King County Data Set
* `id` - Unique identifier for a house
* `date` - Date house was sold
* `price` - Sale price (prediction target)
* `bedrooms` - Number of bedrooms
* `bathrooms` - Number of bathrooms
* `sqft_living` - Square footage of living space in the home
* `sqft_lot` - Square footage of the lot
* `floors` - Number of floors (levels) in house

* `waterfront` - Whether the house is on a waterfront
{'Duwamish':[98168],
'Elliott Bay':[98119,98104,98129,98132,98127,98125,98195,98101,98134,98170,98139,98131,98181], 
'Puget Sound':[98071,98083,98013,98070,98031,98131,98063,98195,98207,98190] 
'Lake Union':[98109], 
'Ship Canal':[00000], 
'Lake Washington':[98072,98077], 
'Lake Sammamish':[98074,98075,98029], 
'other lake':[00000], 
'river/slough waterfronts':[00000]}

* `view` - Quality of view from house
  * Includes views of 
  {'Mt. Rainier': 46.852886, -121.760374
  'Olympics': 47.96935, -123.49856
  'Cascades': 47.425938, -121.700106
  'Territorial': 0,0
  'Seattle Skyline': 47.6204, -122.3491 
  'Puget Sound': 47.694239, -122.462782
  'Lake Washington': 47.621187, -122.256172
  'Lake Sammamish': 47.608341, -122.087502
  'small lake/river/creek/other': 0,0} 
  
* `condition` - {'Poor':1,'Fair':2,'Average':3,'Good':4,'Very Good':5}
1 = Poor- Worn out. Repair and overhaul needed on painted surfaces, roofing, plumbing, heating and numerous functional inadequacies. Excessive deferred maintenance and abuse, limited value-in-use, approaching abandonment or major reconstruction; reuse or change in occupancy is imminent. Effective age is near the end of the scale regardless of the actual chronological age.
2 = Fair- Badly worn. Much repair needed. Many items need refinishing or overhauling, deferred maintenance obvious, inadequate building utility and systems all shortening the life expectancy and increasing the effective age.
3 = Average- Some evidence of deferred maintenance and normal obsolescence with age in that a few minor repairs are needed, along with some refinishing. All major components still functional and contributing toward an extended life expectancy. Effective age and utility is standard for like properties of its class and usage.
4 = Good- No obvious maintenance required but neither is everything new. Appearance and utility are above the standard and the overall effective age will be lower than the typical property.
5= Very Good- All items well maintained, many having been overhauled and repaired as they have shown signs of wear, increasing the life expectancy and lowering the effective age with little deterioration or obsolescence evident with a high degree of utility. 

* `grade` - 
1-3 Falls short of minimum building standards. Normally cabin or inferior structure.
4 Generally older, low quality construction. Does not meet code.
5 Low construction costs and workmanship. Small, simple design.
6 Lowest grade currently meeting building code. Low quality materials and simple designs.
7 Average grade of construction and design. Commonly seen in plats and older sub-divisions.
8 Just above average in construction and design. Usually better materials in both the exterior and interior finish work.
9 Better architectural design with extra interior and exterior design and quality.
10 Homes of this quality generally have high quality features. Finish work is better and more design quality is seen in the floor plans. Generally have a larger square footage.
11 Custom design and higher quality finish work with added amenities of solid woods, bathroom fixtures and more luxurious options.
12 Custom design and excellent builders. All materials are of the highest quality and all conveniences are present.
13 Generally custom designed and built. Mansion level. Large amount of highest quality cabinet work, wood trim, marble, entry ways etc.
  * See the [King County Assessor Website](https://info.kingcounty.gov/assessor/esales/Glossary.aspx?type=r#w) 

* `sqft_above` - Square footage of house apart from basement
* `sqft_basement` - Square footage of the basement
* `yr_built` - Year when house was built
* `yr_renovated` - Year when house was renovated
* `zipcode` - ZIP Code used by the United States Postal Service
* `lat` - Latitude coordinate
* `long` - Longitude coordinate
* `sqft_living15` - The square footage of interior housing living space for the nearest 15 neighbors
* `sqft_lot15` - The square footage of the land lots of the nearest 15 neighbors
