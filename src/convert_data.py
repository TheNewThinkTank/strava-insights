"""Take manually downloaded Strava activities data,
from the file: data/manual_entries.txt,
parse and then transform them to fit with the data schema:
"Activity Date","Activity Type","Elapsed Time","Distance"
and finally write them to file: data/manual_activities.csv

Note: only the date is parsed,
and the activity time is given the default value of "00:00:00 PM"
"""

import csv
from datetime import datetime
import os
# from pprint import pprint as pp
import re
# from icecream import ic  # type: ignore


def transform_data(example):
    activity_pattern = re.compile(r"\b(\w+)\b")
    date_pattern = re.compile(r"\b(\w{3}, \d{1,2}/\d{1,2}/\d{4})\b")
    time_pattern = re.compile(r"\b(\d{1,2}:\d{2})\b")
    distance_pattern = re.compile(r"\b(\d+(\.\d+)?) km\b")

    activity_match = activity_pattern.search(example)
    date_match = date_pattern.search(example)
    time_match = time_pattern.search(example)
    distance_match = distance_pattern.search(example)
    activity_type = activity_match.group(1) if activity_match else ""
    # ic(activity_type)
    original_date = date_match.group(1) if date_match else ""
    # ic(original_date)
    activity_date = datetime.strptime(original_date, "%a, %m/%d/%Y").strftime(
        "%b %d, %Y"
    ) + ", 00:00:00 PM"
    # ic(activity_date)
    elapsed_time = time_match.group(1) if time_match else ""
    # ic(elapsed_time)
    distance = distance_match.group(1) if distance_match else ""
    return activity_date, activity_type, elapsed_time, distance


def get_data(data_file):
    data_list = []
    with open(data_file, "r") as rf:
        data = rf.readlines()
    for line in data:
        data_list.append(transform_data(line))
    # pp(data_list)
    return data_list


def write_data(data_list, out_file) -> None:
    file_exists = os.path.exists(out_file)
    with open(out_file, "a", newline="") as wf:
        csv_writer = csv.writer(wf)
        if not file_exists:
            csv_writer.writerow(
                ["Activity Date", "Activity Type", "Elapsed Time", "Distance"]
            )
        for line in data_list:
            csv_writer.writerow(line)


def main():
    data_list = get_data("data/manual_entries.txt")
    write_data(data_list, "data/manual_activities.csv")


if __name__ == "__main__":
    main()
