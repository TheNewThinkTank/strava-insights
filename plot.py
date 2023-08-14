"""
Analyze and plot strava activities
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("activities.csv")

# print(df.head())
# print(df.columns)

df = df[df["Activity Type"] == "Run"]

df = df[[
    "Activity Date",
    "Elapsed Time",
    "Distance",
    "Moving Time",
    "Average Speed"
]]

df = df.set_index(df["Activity Date"])
df = df.drop(columns=["Activity Date"])
print(df.head())
# df = df.sort_values(ascending=False)

plt.figure(figsize=(12, 6))
plt.subplots_adjust(bottom=0.4)

ax = sns.barplot(
    x=df.index,
    y=df["Distance"],
    # hue=df["Elapsed Time"]  # df["Moving Time"]
    )

ax.set(xlabel="Date & time", ylabel="Distance (km)")
plt.title("Runs")
plt.xticks(rotation=90)
# plt.ylabel("", rotation=0)
# ax.yaxis.set_label_coords(-0.1, 0.5)
# plt.show()
plt.savefig("all_runs.png")


cols = [
    "Activity ID",
    "Activity Date",
    "Activity Name",
    "Activity Type",
    "Activity Description",
    "Elapsed Time",
    "Distance",
    "Max Heart Rate",
    "Relative Effort",
    "Commute",
    "Activity Private Note",
    "Activity Gear",
    "Filename",
    "Athlete Weight",
    "Bike Weight",
    "Elapsed Time.1",
    "Moving Time",
    "Distance.1",
    "Max Speed",
    "Average Speed",
    "Elevation Gain",
    "Elevation Loss",
    "Elevation Low",
    "Elevation High",
    "Max Grade",
    "Average Grade",
    "Average Positive Grade",
    "Average Negative Grade",
    "Max Cadence",
    "Average Cadence",
    "Max Heart Rate.1",
    "Average Heart Rate",
    "Max Watts",
    "Average Watts",
    "Calories",
    "Max Temperature",
    "Average Temperature",
    "Relative Effort.1",
    "Total Work",
    "Number of Runs",
    "Uphill Time",
    "Downhill Time",
    "Other Time",
    "Perceived Exertion",
    '<span class="translation_missing" title="translation missing: en-US.lib.export.portability_exporter.activities.horton_values.type">Type</span>',
    '<span class="translation_missing" title="translation missing: en-US.lib.export.portability_exporter.activities.horton_values.start_time">Start Time</span>',
    "Weighted Average Power",
    "Power Count",
    "Prefer Perceived Exertion",
    "Perceived Relative Effort",
    "Commute.1",
    "Total Weight Lifted",
    "From Upload",
    "Grade Adjusted Distance",
    "Weather Observation Time",
    "Weather Condition",
    "Weather Temperature",
    "Apparent Temperature",
    "Dewpoint",
    "Humidity",
    "Weather Pressure",
    "Wind Speed",
    "Wind Gust",
    "Wind Bearing",
    "Precipitation Intensity",
    "Sunrise Time",
    "Sunset Time",
    "Moon Phase",
    "Bike",
    "Gear",
    "Precipitation Probability",
    "Precipitation Type",
    "Cloud Cover",
    "Weather Visibility",
    "UV Index",
    "Weather Ozone",
    '<span class="translation_missing" title="translation missing: en-US.lib.export.portability_exporter.activities.horton_values.jump_count">Jump Count</span>',
    '<span class="translation_missing" title="translation missing: en-US.lib.export.portability_exporter.activities.horton_values.total_grit">Total Grit</span>',
    '<span class="translation_missing" title="translation missing: en-US.lib.export.portability_exporter.activities.horton_values.avg_flow">Avg Flow</span>',
    '<span class="translation_missing" title="translation missing: en-US.lib.export.portability_exporter.activities.horton_values.flagged">Flagged</span>',
    '<span class="translation_missing" title="translation missing: en-US.lib.export.portability_exporter.activities.horton_values.avg_elapsed_speed">Avg Elapsed Speed</span>',
    '<span class="translation_missing" title="translation missing: en-US.lib.export.portability_exporter.activities.horton_values.dirt_distance">Dirt Distance</span>',
    '<span class="translation_missing" title="translation missing: en-US.lib.export.portability_exporter.activities.horton_values.newly_explored_distance">Newly Explored Distance</span>',
    '<span class="translation_missing" title="translation missing: en-US.lib.export.portability_exporter.activities.horton_values.newly_explored_dirt_distance">Newly Explored Dirt Distance</span>',
    '<span class="translation_missing" title="translation missing: en-US.lib.export.portability_exporter.activities.horton_values.sport_type">Sport Type</span>',
    '<span class="translation_missing" title="translation missing: en-US.lib.export.portability_exporter.activities.horton_values.total_steps">Total Steps</span>',
    "Media",
]
