# Data Dictionary 
## Feature label: feature description
### notes on preprocessing and encoding 

Gender: Gender of the passengers (Female, Male)
    - categorical (binary)
    - encoding ------- Male: 1,    Female: 0 
    - og weights ----- Male: 0.49, Female: 0.51

Customer Type: The customer type (Loyal customer, disloyal customer)
    - categorical (binary)
    - target feature... target class: **disloyal**
    - encoding ----- Loyal: 1,    Disloyal: 0 
    - og weights --- Loyal: 0.82, Disloyal: 0.18

Age: The actual age of the passengers
    - continuous (years)
    - range:  7 - 85  
    - mean:   39.4
    - median: 40.0 
    - mode:   39.0 (2969 instances)

Type of Travel: Purpose of the flight of the passengers (Personal Travel, Business Travel)
    - categorical (binary) 
    - encoding ----- business: 1,    personal: 0
    - og weights --- business: 0.69, personal 0.31

Class: Travel class in the plane of the passengers (Business, Eco, Eco Plus)
    - categorical (ternary)
    - encoding ----- one-hot (OHE)
    - og weights --- business: 0.478, eco: 0.449, eco plus: 0.072

Flight distance: The flight distance of this journey
    - continuous (miles)
    - range: 31 - 4983
    - mean:   1189.5
    - median: 843.0
    - mode:   337 (660 instances)

Inflight wifi service: Satisfaction level of the inflight wifi service (0:Not Applicable;1-5)
    - categorical (ordinal)
    - mean: 2.73
    - median: 3.0
    - mode: 3 (25868 instances)

Departure/Arrival time convenient: Satisfaction level of Departure/Arrival time
    - categorical (ordinal)
    - mean: 3.06
    - median: 3.0
    - mode: 4 (25546 instances)

Ease of Online booking: Satisfaction level of online booking
    - categorical (ordinal)
    - mean: 2.76
    - median: 3.0
    - mode:  3 (24449 instances)

Gate location: Satisfaction level of Gate location
    - categorical (ordinal)
    - mean: 2.98
    - median: 3.0
    - mode: 3 (28577 instances)

Food and drink: Satisfaction level of Food and drink
    - categorical (ordinal)
    - mean: 3.20
    - median: 3.0
    - mode: 4 (24359 instances)

Online boarding: Satisfaction level of online boarding
    - categorical (ordinal)
    - mean: 3.25
    - median: 3.0
    - mode: 4 (30762 instances)
    
Seat comfort: Satisfaction level of Seat comfort
    - categorical (ordinal)
    - mean: 3.44
    - median: 4.0 
    - mode: 4 (31765 instances)

Inflight entertainment: Satisfaction level of inflight entertainment
    - categorical (ordinal)
    - mean: 3.36
    - median: 4.0
    - mode: 4 (29493 instances)

On-board service: Satisfaction level of On-board service
    - categorical (ordinal)
    - mean: 3.38
    - median: 4.0
    - mode: 4 (30867 instances)

Leg room service: Satisfaction level of Leg room service
    - categorical (ordinal)
    - mean: 3.35
    - median: 4.0
    - mode: 4 (28789 instances)

Baggage handling: Satisfaction level of baggage handling
    - categorical (ordinal)
    - mean: 3.63
    - median: 4.0
    - mode: 4 (378383 instances)

Check-in service: Satisfaction level of Check-in service
    - categorical (ordinal)
    - mean: 3.30
    - median: 3.0
    - mode: 4 (29055 instances)

Inflight service: Satisfaction level of inflight service
    - categorical (ordinal)
    - mean: 3.64
    - median: 4.0
    - mode: 4 (37945 instances)

Cleanliness: Satisfaction level of Cleanliness
    - categorical (ordinal)
    - mean: 3.29
    - median: 3.0 
    - mode: 4 (27179)

Departure Delay in Minutes: Minutes delayed when departure
    - continuous (minutes)
    - range: 0.0 - 26.5 hours
    - mean: ~15 minutes
    - median: 0.0 
    - mode: 0 (58668 instances)

Arrival Delay in Minutes: Minutes delayed when Arrival
    - continuous (minutes)
    - range: 0.0 - 26.4 hours
    - mean: ~15 minutes
    - median: 0.0
    - mode: 0.0 (58469 instances)

Satisfaction: Airline satisfaction level(Satisfaction, neutral or dissatisfaction)
    - categorical (binary)
    - encoding ----- satistfied: 1,   neutral/dissatisfied: 0
    - og weights --- satisfied: 0.56, neutral/dissatisfied: 0.43