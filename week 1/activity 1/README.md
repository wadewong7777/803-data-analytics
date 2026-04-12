# Week 1 Activity 1

This folder contains a simple Pandas analysis of the Excel dataset and a Matplotlib bar chart.

## Files

- `Data_set_w1A1.xlsx` - the original Excel dataset.
- `analyse_w1a1.py` - Python script that reads the Excel file, summarises the data, and creates the chart.
- `w1a1_summary.txt` - text output from the analysis.
- `category_sales_bar.png` - bar chart showing total sales by category.

## Analysis Summary

The dataset has three categories: A, B, and C.

| Category | Total Sales | Average Sales | Sales Count |
| --- | ---: | ---: | ---: |
| A | 18,010 | 545.76 | 33 |
| B | 22,154 | 615.39 | 36 |
| C | 18,213 | 587.52 | 31 |

Category B had the highest total sales, with 22,154.

## Bar Chart

The file `category_sales_bar.png` shows a simple bar graph comparing total sales for each category.

## How to Run

From the project folder, run:

```bash
.venv/bin/python 'week 1/activity 1/analyse_w1a1.py'
```

This will update `w1a1_summary.txt` and `category_sales_bar.png`.
