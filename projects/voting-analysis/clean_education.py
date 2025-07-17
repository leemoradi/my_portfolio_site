import pandas as pd
import os

# Create a directory for visualizations
os.makedirs('visualizations', exist_ok=True)

# Load the education dataset
education_df = pd.read_csv('~/Visual Studio Code/my_portfolio_site/projects/voting-analysis/merged_education.csv')

# Automatically clean column names
education_df.columns = [col.strip() for col in education_df.columns]

# Ensure 'Year' column exists and is standardized
year_col = None
for col in education_df.columns:
    if col.lower() == 'year':
        year_col = col
        break
if year_col and year_col != 'Year':
    education_df.rename(columns={year_col: 'Year'}, inplace=True)
if 'Year' not in education_df.columns:
    education_df['Year'] = '2020'
education_df['Year'] = education_df['Year'].astype(str).str.strip()

# Standardize state names
if 'Geographic Area Name' in education_df.columns:
    education_df['Geographic Area Name'] = education_df['Geographic Area Name'].astype(str).str.strip().str.upper()
    print("Unique state values after cleaning:", education_df['Geographic Area Name'].unique())
    # Filter by relevant states
    education_df = education_df[education_df['Geographic Area Name'] == 'UNITED STATES']
elif 'state' in education_df.columns:
    education_df['state'] = education_df['state'].astype(str).str.strip().str.upper()
    print("Unique state values after cleaning:", education_df['state'].unique())
    education_df = education_df[education_df['state'].isin(['GEORGIA', 'TEXAS'])]
else:
    print("No state column found!")

# Remove duplicates and missing data
education_df = education_df.drop_duplicates()
education_df = education_df.dropna(subset=['Geographic Area Name'])

# View the cleaned dataset
print("Cleaned DataFrame:\n", education_df.head())

# Save the cleaned data to a new CSV file
education_df.to_csv('cleaned_education.csv', index=False)

# For national data
education_df = education_df[education_df['Geographic Area Name'] == 'UNITED STATES']



