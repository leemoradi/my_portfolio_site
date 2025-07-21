# Voting Analysis Project

This project analyzes voting patterns in the 2020 U.S. Presidential Election, focusing on the states of Georgia and Texas. It combines county-level voting data with income and education statistics to explore correlations and visualize key trends.

## Features

- Cleans and merges voting, income, and education datasets.
- Calculates and visualizes vote percentages for major candidates.
- Produces county-level and state-level visualizations.
- Analyzes correlations between voting patterns, income, and education.
- Highlights competitive counties and key statistical insights.

## Data Sources

- County-level voting data: `data/county_info.xlsx`
- Income data: Merged from multiple CSVs in `/Users/leahmoradi/Desktop/Income`
- Education data: Merged from multiple CSVs in `/Users/leahmoradi/Desktop/Education`

## Workflow

1. **Data Cleaning**
   - `clean_votes.py`, `clean_income.py`, `clean_education.py`: Standardize and clean raw datasets.
2. **Data Merging**
   - `merge_income_data.py`, `merge_education_data.py`: Merge annual CSVs into comprehensive datasets.
   - `combine_all_data.py`: Merge voting, income, and education data into a single dataset.
3. **Analysis & Visualization**
   - `analyze_data.py`: Merges datasets, creates scatter plots, and computes correlation matrices.
   - `county_vote_percentages.py`: Calculates county-level vote percentages.
   - `create_meaningful_visualizations.py`: Generates county-level scatter plots, histograms, and summary statistics.
   - `generate_all_figures.py`: Automates the creation of all major figures.
   - `create_actual_2020_results.py`: Visualizes actual 2020 election results and margins.
   - `fix_correlation_matrix.py`: Produces a detailed county-level correlation matrix.

## Outputs

- Cleaned and merged CSVs (e.g., `cleaned_education.csv`, `merged_voting_data.csv`, `combined_voting_dataset.csv`)
- Visualizations in the `visualizations/` folder:
  - County-level scatter plots and histograms
  - Vote percentage bar charts
  - Correlation matrices
  - Actual 2020 results and margin of victory charts

## How to Run

1. Ensure you have Python 3 and the required libraries:
   ```
   pip install pandas matplotlib seaborn numpy
   ```
2. Run the scripts in the following order for a full analysis:
   - Data cleaning: `python clean_votes.py`, `python clean_income.py`, `python clean_education.py`
   - Data merging: `python merge_income_data.py`, `python merge_education_data.py`, `python combine_all_data.py`
   - Analysis and visualization: `python analyze_data.py`, `python county_vote_percentages.py`, `python create_meaningful_visualizations.py`, `python generate_all_figures.py`, `python create_actual_2020_results.py`, `python fix_correlation_matrix.py`

## Notes

- Update file paths in scripts if your data directories differ.
- Visualizations are saved in the `visualizations/` directory for easy access. 