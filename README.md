![commit activity](https://img.shields.io/github/commit-activity/m/TheNewThinkTank/strava-insights)
![CI](https://github.com/TheNewThinkTank/strava-insights/actions/workflows/wf.yml/badge.svg)
[![GitHub repo size](https://img.shields.io/github/repo-size/TheNewThinkTank/strava-insights?style=flat&logo=github&logoColor=whitesmoke&label=Repo%20Size)](https://github.com/TheNewThinkTank/strava-insights/archive/refs/heads/main.zip)

# strava-insights
Analysis and visualization of Strava activities

Below: all runs uploaded to Strava
![All Strava runs](img/all_runs.png)

## Data

[Requesting a bulk data export](https://support.strava.com/hc/en-us/articles/216918437-Exporting-your-Data-and-Bulk-Export#h_01GG58HC4F1BGQ9PQZZVANN6WF)

main file used in this project: `data/activities.csv`

## Usage

running the Python module to create figures:<br>
`python3 src/plot.py`

running the TypeScript module to calculate statistics:<br>
compilation: `tsc src/calc.ts`<br>
running: `node src/calc.js`
