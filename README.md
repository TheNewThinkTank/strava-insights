![commit activity](https://img.shields.io/github/commit-activity/m/TheNewThinkTank/strava-insights)
![CI](https://github.com/TheNewThinkTank/strava-insights/actions/workflows/wf.yml/badge.svg)
[![GitHub repo size](https://img.shields.io/github/repo-size/TheNewThinkTank/strava-insights?style=flat&logo=github&logoColor=whitesmoke&label=Repo%20Size)](https://github.com/TheNewThinkTank/strava-insights/archive/refs/heads/main.zip)
[![codecov](https://codecov.io/gh/TheNewThinkTank/strava-insights/branch/main/graph/badge.svg)](https://codecov.io/gh/TheNewThinkTank/strava-insights)

# strava-insights
Analysis and visualization of Strava activities

## Data

[Requesting a bulk data export](https://support.strava.com/hc/en-us/articles/216918437-Exporting-your-Data-and-Bulk-Export#h_01GG58HC4F1BGQ9PQZZVANN6WF)

## Usage

<details>
  <summary>calculating statistics and creating figures</summary>

running the Python module to create figures:<br>
`python3 src/plot.py`

running the TypeScript module to calculate statistics:<br>
compilation: `tsc src/calc.ts`<br>
running: `node src/calc.js`

</details>

## Plots

<p align="center">
  <img src="img/2023_first_half_run_distances_bar_plot.png" width="400"/>
  <img src="img/2023_second_half_run_distances_bar_plot.png" width="400"/>
</p>



<!-- Below: all runs uploaded to Strava
![All Strava runs](img/all_runs.png) -->

<!-- <p align="center">
  <img src="img/2023_run_distances_bar_plot.png" width="400"/>
</p>

<p align="center">
  <img src="img/2022_run_distances_bar_plot.png" width="400"/>
</p>

<p align="center">
  <img src="img/2021_run_distances_bar_plot.png" width="400"/>
</p> -->
