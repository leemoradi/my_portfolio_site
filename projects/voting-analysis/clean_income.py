import pandas as pd

# Load the income dataset
income_df = pd.read_csv('~/Visual Studio Code/my_portfolio_site/projects/voting-analysis/merged_income.csv')

# Automatically clean column names
income_df.columns = [col.strip() for col in income_df.columns]

# Ensure 'Year' column exists and is standardized
year_col = None
for col in income_df.columns:
    if col.lower() == 'year':
        year_col = col
        break
if year_col and year_col != 'Year':
    income_df.rename(columns={year_col: 'Year'}, inplace=True)
if 'Year' not in income_df.columns:
    income_df['Year'] = '2020'
income_df['Year'] = income_df['Year'].astype(str).str.strip()

# Standardize state names
if 'Geographic Area Name' in income_df.columns:
    income_df['Geographic Area Name'] = income_df['Geographic Area Name'].astype(str).str.strip().str.upper()
    print("Unique state values after cleaning:", income_df['Geographic Area Name'].unique())
    # Removed filter for GEORGIA and TEXAS
elif 'state' in income_df.columns:
    income_df['state'] = income_df['state'].astype(str).str.strip().str.upper()
    print("Unique state values after cleaning:", income_df['state'].unique())
    # Removed filter for GEORGIA and TEXAS
else:
    print("No state column found!")

# Remove duplicates and missing data
income_df = income_df.drop_duplicates()
income_df = income_df.dropna(subset=['Geographic Area Name'])

# Filter the DataFrame to include only rows where 'Geographic Area Name' is 'UNITED STATES'
income_df = income_df[income_df['Geographic Area Name'] == 'UNITED STATES']

# View the cleaned dataset
print("Cleaned DataFrame:\n", income_df.head())

# Save the cleaned data to a new CSV file
income_df.to_csv('cleaned_income.csv', index=False)

