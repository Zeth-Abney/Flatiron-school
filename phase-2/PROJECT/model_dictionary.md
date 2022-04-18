# Feature Names and Details for King County Realestate Regression Model. 


* `bathrooms` - Number of bathrooms in the house. 
    (minimum 0.5, maximum 7.5, mean 2.0)


* `lat` - Latitudinal degree that the propertry lies on (decimal format). 
        This model covers about a 43 mile range. 
        (minimum 47.155900, maximum 47.777600)


* `grade` 
    - 1-3 (1 data point) Falls short of minimum building standards. Normally cabin or inferior structure. 

    - 4 (27 data points) Generally older, low quality construction. Does not meet code.

    - 5 (235 data points) Low construction costs and workmanship. Small, simple design.

    - 6 (1,996 data points) Lowest grade currently meeting building code. Low quality materials and simple designs.

    - 7 (8,775 data points) Average grade of construction and design. Commonly seen in plats and older sub-divisions.

    - 8 (5,808 data points) Just above average in construction and design. Usually better materials in both the exterior and interior finish work.

    - 9 (2,258 data points) Better architectural design with extra interior and exterior design and quality.

    - 10 (747 data points) Homes of this quality generally have high quality features. Finish work is better and more design quality is seen in the floor plans. Generally have a larger square footage.

    - 11 (130 data points) Custom design and higher quality finish work with added amenities of solid woods, bathroom fixtures and more luxurious options.

    - 12 (5 data points) Custom design and excellent builders. All materials are of the highest quality and all conveniences are present.

    - 13 (0 data points) Generally custom designed and built. Mansion level. Large amount of highest quality cabinet work, wood trim, marble, entry ways etc.


* `sqft_living15` - The average sqaure footage of living space for the nearst 15 other homes. (Minimum 399, maximum 4950, mean 1921)


* `view` - Quality of view from house on a 5 point scale starting at 0.
    - 0: poor or no view (18459 data points)
    - 1: fair view (270 data points)
    - 2: Average (777 data points)
    - 3: Good (334 data points)
    - 4: Excellent (142 data points)

    * Includes views of 
    {'Mt. Rainier': (46.852886, -121.760374),
    'Olympics': (47.96935, -123.49856),
    'Cascades': (47.425938, -121.700106),
    'Territorial': (0,0),
    'Seattle Skyline': (47.6204, -122.3491), 
    'Puget Sound': (47.694239, -122.462782),
    'Lake Washington': (47.621187, -122.256172),
    'Lake Sammamish': (47.608341, -122.087502),
    'small lake/river/creek/other': (0,0)}


* `condition` - Qualitative assessment of the livability and quality of the home.

    1: Poor (27 data points)- Worn out. Repair and overhaul needed on painted surfaces, roofing, plumbing, heating and numerous functional inadequacies. Excessive deferred maintenance and abuse, limited value-in-use, approaching abandonment or major reconstruction; reuse or change in occupancy is imminent. Effective age is near the end of the scale regardless of the actual chronological age.

    2: Fair (164 data points)- Badly worn. Much repair needed. Many items need refinishing or overhauling, deferred maintenance obvious, inadequate building utility and systems all shortening the life expectancy and increasing the effective age.

    3: Average (12,971 data points)- Some evidence of deferred maintenance and normal obsolescence with age in that a few minor repairs are needed, along with some refinishing. All major components still functional and contributing toward an extended life expectancy. Effective age and utility is standard for like properties of its class and usage.

    4: Good (5,296 data points)- No obvious maintenance required but neither is everything new. Appearance and utility are above the standard and the overall effective age will be lower than the typical property.

    5: Very Good (1524 data points)- All items well maintained, many having been overhauled and repaired as they have shown signs of wear, increasing the life expectancy and lowering the effective age with little deterioration or obsolescence evident with a high degree of utility. 


* `sale_date` - Date the house was sold (pandas ordinal, see ".toordinal")
    This data set only covers about a year; from May 02,2014 to May 24, 2015


* `sale_month` - integer between 1-12 representing the month of the year in which the property was sold. 


* `waterfront` - A boolean (1/0) indicating wether or not a property is on a waterfront (1) or not (0). There are 50 non-zero data points.  


* `waterfront locations` - Whether the house is in the same zipcode as a particular waterfront. (2023 total data points)

    Lake Union (82 data points): 98109

    Lake Sammamish (1036 data points)): 98074,98075,98029

    Puget Sound (379 data points): 98071,98083,98013,98070,98031,98131,98063,98195,98207,98190

    Duwamish (262 data points): 98168

    Lake Washington (444 data points): 98072,98077


* `Piechart / treemap reference` - a guide to which features are grouped together for the purposes of the treemap and piechart visualizations at the end of student.ipynb

    - How far north? lat,
    - On a waterfront? waterfront,
    - Which waterfront? (sum of absolute values) waterfront_Lake Union,waterfront_Lake Sammamish,waterfront_Puget Sound,waterfront_Duwamish,'waterfront_Lake Washington,
    - How much repair needed? (sum of absolute values) condition, grade,
    - How many bathrooms? bathrooms,
    - Good view? view,
    - When? (sum of absolute values) sale_date,sale_month



  * For more details see the [King County Assessor Website](https:May//info.kingcounty.gov/assessor/esales/Glossary.aspx?type=r#w)
  * For more info on the analysis please email [Zeth Abney](zethusabney@gmail.com)


