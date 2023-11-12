"""
Analyze and plot strava activities
"""

import matplotlib.pyplot as plt  # type: ignore
import pandas as pd  # type: ignore
import seaborn as sns  # type: ignore


def get_run_data(in_file, year, activity_type) -> pd.DataFrame:
    df = pd.read_csv(in_file)
    # print(df.head())
    # print(df.columns)
    df = df[df["Activity Type"] == activity_type]
    df["Activity Date"] = pd.to_datetime(
        df["Activity Date"], format="%b %d, %Y, %H:%M:%S %p", errors="coerce"
    )
    df = df[df["Activity Date"].dt.year == year]
    df = df[
        # ["Activity Date", "Elapsed Time", "Distance", "Moving Time", "Average Speed"]
        ["Activity Date", "Elapsed Time", "Distance"]
    ]
    df = df.set_index(df["Activity Date"])
    df = df.drop(columns=["Activity Date"])
    # df.index = pd.to_datetime(df.index)
    return df


def merge_dfs(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([df1, df2]).sort_index()


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


def monthly_activity_count_bar_plot(df, year) -> None:
    # (assuming 'Activity Date' is in datetime format)
    df["Month"] = df.index.to_period("M")
    activity_counts = df["Month"].value_counts().sort_index()
    plt.figure(figsize=(10, 6))
    sns.barplot(x=activity_counts.index, y=activity_counts.values)
    plt.xlabel("Month")
    plt.ylabel("Number of Activities")
    plt.title(f"Activities per Month - {year}")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    # plt.savefig(f"img/{year}_activities_over_time_bar_plot.png")


def annual_distances_bar_plot(df, year, activity_type) -> None:
    plt.figure(figsize=(10, 6))
    sns.barplot(x=df.index, y=df["Distance"].values)
    plt.xlabel("Date")
    plt.ylabel("Distance [km]")
    plt.title(f"{activity_type} distances - {year}")

    # print(df.index)

    # TODO: fix x labels and xaxis data offset
    plt.xticks(rotation=45, ha="right")
    # plt.xticks(
    #     ticks=df.index,
    #     # labels=df.index,  # .strftime("%Y-%m-%d"),
    #     rotation=45
    # )

    plt.tight_layout()
    # plt.show()
    plt.savefig(f"img/{year}_{activity_type.lower()}_distances_bar_plot.png")


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
    activity_type = "Run"
    years = [2021, 2022, 2023]

    for year in years:
        df_bulk = get_run_data("data/activities.csv", year, activity_type)
        df_manual = get_run_data("data/manual_activities.csv", year, activity_type)
        df = merge_dfs(df_bulk, df_manual)
        annual_distances_bar_plot(df, year, activity_type)

    # print(df.head())
    # print(df.columns)
    # df = df.sort_values(ascending=False)

    # time_series_plot(df)
    # scatter_plot(df)
    # monthly_activity_count_bar_plot(df, year)
    # average_speed_line_plot(df)
    # print(df)
    # correlation_heatmap(df)
    # pair_plot(df)


if __name__ == "__main__":
    main()
