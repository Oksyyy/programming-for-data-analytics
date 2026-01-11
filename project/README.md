# Wind Speed Trends and Wind Power Availability in Ireland

by Oksana Abrosimova


## Project Overview

This project analyses historical wind speed data from three Irish weather stations (Malin Head, Mace Head, and Dublin Airport) to assess wind power availability and long-term trends relevant to electricity generation. The analysis focuses on **seasonal variability**, **time-of-day availability during peak demand**, and **long-term wind speed trends**.

## Data

- Hourly wind speed (wdsp) observations.

- Locations:

    - Malin Head.
    - Mace Head.
    - Dublin Airport.

- Data source:
    - Met Éireann (via provided datasets).

- Analysis period:
    - Seasonal and diurnal analysis: most recent 10 years.
    - Long-term trend analysis: full available record.

## Methodology

- Monthly and hourly wind speed statistics were computed using time-based resampling.
- Wind turbine operational availability was estimated using assumed cut-in and cut-out wind speeds.
- Long-term trends were assessed using annual mean wind speeds and linear regression.
- Five-year rolling means were applied to reduce short-term variability.

## Requirements

### Software
- **Python 3.10+** — required to run the scripts and notebooks
  Install from: https://www.python.org  
- **Jupyter Notebook** (or VS Code + Jupyter extension)
  Installation instructions: https://jupyter.org/install

### Python Packages
All required packages are imported within each respective notebook: 
- `pandas`: enables data handling, filtering, analysis.
- `numpy`:  numerical operations and converting data into array.
- `matplotlib.pyplot`: creating charts and visualisations.
- `requests`: retrieving data from API's.
- `scikit-learn`: linear regression analysis.

## Limitations
- Wind turbine operating thresholds are assumed and not site-specific.
- Linear regression trends are descriptive and not tested for statistical significance.