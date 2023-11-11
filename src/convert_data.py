"""Take manually downloaded Strava activities data,
parse them transform them to fit with the data schema
"""

from datetime import datetime
import re

from icecream import ic

activity_pattern = re.compile(r'\b(\w+)\b')
date_pattern = re.compile(r'\b(\w{3}, \d{1,2}/\d{1,2}/\d{4})\b')
time_pattern = re.compile(r'\b(\d{1,2}:\d{2})\b')
distance_pattern = re.compile(r'\b(\d+(\.\d+)?) km\b')

# example = "Run Mon, 10/30/2023 Afternoon Run 18:57 4.01 km"
example = "Ride	Wed, 9/27/2023	Afternoon Ride	23:00	6.85 km"

activity_match = activity_pattern.search(example)
date_match = date_pattern.search(example)
time_match = time_pattern.search(example)
distance_match = distance_pattern.search(example)

if activity_match:
    activity_type = activity_match.group(1)
    ic(activity_type)
else:
    print("Activity Type not found")
if date_match:
    original_date = date_match.group(1)
    ic(original_date)
    activity_date = datetime.strptime(original_date, '%a, %m/%d/%Y').strftime('%b %d, %Y')
    ic(activity_date)
else:
    print("Date not found")
if time_match:
    ic(time_match.group(1))
else:
    print("Time not found")
if distance_match:
    print("Distance:", distance_match.group(1), "km")
else:
    print("Distance not found")

# activity_date
# activity_name
activity_type
elapsed_time
distance

header = "Activity Date,Activity Type,Elapsed Time,Distance"
