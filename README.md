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
  <img src="img/2022_first_half_run_distances_bar_plot.png" width="400"/>
  <img src="img/2022_second_half_run_distances_bar_plot.png" width="400"/>
  <img src="img/2021_first_half_run_distances_bar_plot.png" width="400"/>
  <img src="img/2021_second_half_run_distances_bar_plot.png" width="400"/>
</p>


## Running routes

- The central lakes
- [The Blue Circle / the harbor circle](https://www.visitcopenhagen.com/copenhagen/planning/harbour-circle-gdk1117372)
- [Forest and Highway trail skovlunde](https://www.mypacer.com/routes/56211/forest-and-highway-walk-trail-skovlunde-capital-region-of-denmark-denmark)
