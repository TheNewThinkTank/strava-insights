"""
Analyze and plot strava activities
"""

import matplotlib.pyplot as plt  # type: ignore
import pandas as pd  # type: ignore
import seaborn as sns  # type: ignore


def get_run_data() -> pd.DataFrame:
    df = pd.read_csv("data/activities.csv")
    # print(df.head())
    # print(df.columns)
    df = df[df["Activity Type"] == "Run"]
    df = df[
        ["Activity Date", "Elapsed Time", "Distance", "Moving Time", "Average Speed"]
    ]
    df = df.set_index(df["Activity Date"])
    df = df.drop(columns=["Activity Date"])
    df.index = pd.to_datetime(df.index)  # Convert index to datetime if needed
    return df


def time_series_plot(df) -> None:
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df["Distance"], marker="o")
    plt.xlabel("Activity Date")
    plt.ylabel("Distance")
    plt.title("Distance Over Time")
    plt.xticks(rotation=45)
    plt.tight_layout()
    # plt.show()
    plt.savefig("img/time_series_plot.png")


def scatter_plot(df) -> None:
    plt.figure(figsize=(8, 6))
    plt.scatter(df["Elapsed Time"], df["Distance"])
    plt.xlabel("Elapsed Time")
    plt.ylabel("Distance")
    plt.title("Scatter Plot: Elapsed Time vs. Distance")
    plt.tight_layout()
    # plt.show()
    plt.savefig("img/scatter_plot.png")


def activities_over_time_bar_plot(df) -> None:
    # (assuming 'Activity Date' is in datetime format)
    df["Month"] = df.index.to_period("M")
    activity_counts = df["Month"].value_counts().sort_index()
    plt.figure(figsize=(10, 6))
    sns.barplot(x=activity_counts.index, y=activity_counts.values)
    plt.xlabel("Month")
    plt.ylabel("Number of Activities")
    plt.title("Number of Activities per Month")
    plt.xticks(rotation=45)
    plt.tight_layout()
    # plt.show()
    plt.savefig("img/activities_over_time_bar_plot.png")


def average_speed_line_plot(df) -> None:
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df["Average Speed"], marker="o")
    plt.xlabel("Activity Date")
    plt.ylabel("Average Speed")
    plt.title("Average Speed Over Time")
    plt.xticks(rotation=45)
    plt.tight_layout()
    # plt.show()
    plt.savefig("img/average_speed_line_plot.png")


def correlation_heatmap(df) -> None:
    # TODO: fix df.corr() call issue
    correlation_matrix = df.corr()

    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    # plt.show()
    plt.savefig("img/correlation_heatmap.png")


def pair_plot(df) -> None:
    sns.pairplot(df[["Elapsed Time", "Distance", "Moving Time", "Average Speed"]])
    plt.suptitle("Pair Plot")
    plt.tight_layout()
    # plt.show()
    plt.savefig("img/pair_plot.png")


def main():
    df = get_run_data()
    # print(df.head())
    # print(df.columns)
    # df = df.sort_values(ascending=False)

    time_series_plot(df)
    scatter_plot(df)
    activities_over_time_bar_plot(df)
    average_speed_line_plot(df)

    # print(df)
    # correlation_heatmap(df)

    pair_plot(df)


if __name__ == "__main__":
    main()
