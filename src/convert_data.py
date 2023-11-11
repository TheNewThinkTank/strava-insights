"""Take manually downloaded Strava activities data,
parse them transform them to fit with the data schema
"""

import csv
from datetime import datetime
# from pprint import pprint as pp
import re

# from icecream import ic  # type: ignore

activity_pattern = re.compile(r'\b(\w+)\b')
date_pattern = re.compile(r'\b(\w{3}, \d{1,2}/\d{1,2}/\d{4})\b')
time_pattern = re.compile(r'\b(\d{1,2}:\d{2})\b')
distance_pattern = re.compile(r'\b(\d+(\.\d+)?) km\b')


def get_data(example):
    activity_match = activity_pattern.search(example)
    date_match = date_pattern.search(example)
    time_match = time_pattern.search(example)
    distance_match = distance_pattern.search(example)
    activity_type = activity_match.group(1) if activity_match else ""
    # ic(activity_type)
    original_date = date_match.group(1) if date_match else ""
    # ic(original_date)
    activity_date = datetime.strptime(original_date, '%a, %m/%d/%Y').strftime('%b %d, %Y')
    # ic(activity_date)
    elapsed_time = time_match.group(1) if time_match else ""
    # ic(elapsed_time)
    distance = distance_match.group(1) if distance_match else ""
    return activity_date, activity_type, elapsed_time, distance


def main():
    data_list = []

    with open("data/manual_entries.txt", "r") as rf:
        data = rf.readlines()
    
    for line in data:
        data_list.append(get_data(line))
    
    # pp(data_list)
    csv_file_path = 'data/activity_data.csv'

    with open(csv_file_path, 'w', newline='') as wf:
        csv_writer = csv.writer(wf)

        csv_writer.writerow(["Activity Date", "Activity Type", "Elapsed Time", "Distance"])

        for line in data_list:
            csv_writer.writerow(line)


if __name__ == "__main__":
    main()
