# Week 2 Activity 1

GitHub repository: https://github.com/wadewong7777/803-data-analytics

This activity uses the official **Beijing Multi-Site Air Quality** dataset from UCI:
https://archive.ics.uci.edu/dataset/501/beijing+multi+site+air+quality+data

## Data Structure

The dataset is a multivariate time-series collected from **12 air-quality monitoring sites** in Beijing.

- Time span: **2013-03-01 to 2017-02-28**
- Total rows after combining all site files: **420,768**
- Total columns: **18**
- Missing values are marked as **NA**
- Main variable groups:
  - Time fields: `No`, `year`, `month`, `day`, `hour`
  - Air pollutants: `PM2.5`, `PM10`, `SO2`, `NO2`, `CO`, `O3`
  - Weather fields: `TEMP`, `PRES`, `DEWP`, `RAIN`, `wd`, `WSPM`
  - Site label: `station`

## Data and Result

The script in this folder loads the data and prints the requested result:

- Load the dataset
- Display the first 5 rows
- Identify column names and data types
- Count total rows and columns

## Files

- `analyse_w2a1.py` - combines the local CSV files and prints the output.
- `data/` - extracted original UCI CSV files used by the script.

## How to Run

From the project root, run:

```bash
.venv/bin/python 'week 2/activity 1/analyse_w2a1.py'
```

This prints the dataset structure, first 5 rows, column names, and data types.
