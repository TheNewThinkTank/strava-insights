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

# TODO: string to datetime, example: Feb 22, 2021, 10:30:06 AM

# df = df.set_index(df["Activity Date"])
# df = df.drop(columns=["Activity Date"])
print(df.head())
# df = df.sort_values(ascending=False)

# plt.figure(figsize=(12, 6))
# plt.subplots_adjust(bottom=0.4)

# ax = sns.barplot(
#     x=df.index,
#     y=df["Distance"],
#     # hue=df["Elapsed Time"]  # df["Moving Time"]
#     )

# ax.set(xlabel="Date & time", ylabel="Distance (km)")
# plt.title("Runs")
# plt.xticks(rotation=90)
# plt.ylabel("", rotation=0)
# ax.yaxis.set_label_coords(-0.1, 0.5)
# plt.show()
# plt.savefig("all_runs.png")


# Time Series Plot
plt.figure(figsize=(10, 6))
plt.plot(df["Activity Date"], df['Distance'], marker='o')
plt.xlabel('Activity Date')
plt.ylabel('Distance')
plt.title('Distance Over Time')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Histograms
plt.figure(figsize=(12, 6))
plt.subplot(1, 3, 1)
plt.hist(df['Elapsed Time'], bins=20)
plt.xlabel('Elapsed Time')
plt.ylabel('Frequency')
plt.title('Elapsed Time Histogram')

plt.subplot(1, 3, 2)
plt.hist(df['Distance'], bins=20)
plt.xlabel('Distance')
plt.ylabel('Frequency')
plt.title('Distance Histogram')

plt.subplot(1, 3, 3)
plt.hist(df['Moving Time'], bins=20)
plt.xlabel('Moving Time')
plt.ylabel('Frequency')
plt.title('Moving Time Histogram')

plt.tight_layout()
plt.show()

# Scatter Plot
plt.figure(figsize=(8, 6))
plt.scatter(df['Elapsed Time'], df['Distance'])
plt.xlabel('Elapsed Time')
plt.ylabel('Distance')
plt.title('Scatter Plot: Elapsed Time vs. Distance')
plt.tight_layout()
plt.show()

# from datetime import datetime as dt

# Bar Plot for Activities Over Time (assuming 'Activity Date' is in datetime format)
df['Month'] = df["Activity Date"].dt.to_period('M')
activity_counts = df['Month'].value_counts().sort_index()

plt.figure(figsize=(10, 6))
sns.barplot(x=activity_counts.index, y=activity_counts.values)
plt.xlabel('Month')
plt.ylabel('Number of Activities')
plt.title('Number of Activities per Month')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Line Plot for Average Speed
plt.figure(figsize=(10, 6))
plt.plot(df['Activity Date'], df['Average Speed'], marker='o')
plt.xlabel('Activity Date')
plt.ylabel('Average Speed')
plt.title('Average Speed Over Time')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Correlation Heatmap
correlation_matrix = df.corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.show()

# Pair Plot
sns.pairplot(df[['Elapsed Time', 'Distance', 'Moving Time', 'Average Speed']])
plt.suptitle('Pair Plot')
plt.tight_layout()
plt.show()


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
