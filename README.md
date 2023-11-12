![commit activity](https://img.shields.io/github/commit-activity/m/TheNewThinkTank/strava-insights)
![CI](https://github.com/TheNewThinkTank/strava-insights/actions/workflows/wf.yml/badge.svg)
[![GitHub repo size](https://img.shields.io/github/repo-size/TheNewThinkTank/strava-insights?style=flat&logo=github&logoColor=whitesmoke&label=Repo%20Size)](https://github.com/TheNewThinkTank/strava-insights/archive/refs/heads/main.zip)

# strava-insights
Analysis and visualization of Strava activities

## Data

[Requesting a bulk data export](https://support.strava.com/hc/en-us/articles/216918437-Exporting-your-Data-and-Bulk-Export#h_01GG58HC4F1BGQ9PQZZVANN6WF)

## Usage

running the Python module to create figures:<br>
`python3 src/plot.py`

running the TypeScript module to calculate statistics:<br>
compilation: `tsc src/calc.ts`<br>
running: `node src/calc.js`

## Plots

<!-- Below: all runs uploaded to Strava
![All Strava runs](img/all_runs.png) -->

![2023 Strava runs](img/2023_run_distances_bar_plot.png)
![2022 Strava runs](img/2022_run_distances_bar_plot.png)
![2021 Strava runs](img/2021_run_distances_bar_plot.png)
