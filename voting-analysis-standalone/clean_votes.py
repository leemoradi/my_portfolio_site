import pandas as pd

# Load the voting dataset
vote_df: pd.DataFrame = pd.read_csv('~/Visual Studio Code/my_portfolio_site/projects/voting-analysis/vote_percentages.csv')

# Automatically clean column names
vote_df.columns = [col.strip() for col in vote_df.columns]

# Ensure 'Year' column exists and is standardized
year_col = None
for col in vote_df.columns:
    if col.lower() == 'year':
        year_col = col
        break
if year_col and year_col != 'Year':
    vote_df.rename(columns={year_col: 'Year'}, inplace=True)
if 'Year' not in vote_df.columns:
    vote_df['Year'] = '2020'
vote_df['Year'] = vote_df['Year'].astype(str).str.strip()

# Standardize state names
if 'state' in vote_df.columns:
    vote_df['state'] = vote_df['state'].astype(str).str.strip().str.upper()
    print("Unique state values after cleaning:", vote_df['state'].unique())
    vote_df = vote_df[vote_df['state'].isin(['GEORGIA', 'TEXAS'])]  # type: ignore
elif 'Geographic Area Name' in vote_df.columns:
    vote_df['Geographic Area Name'] = vote_df['Geographic Area Name'].astype(str).str.strip().str.upper()
    print("Unique state values after cleaning:", vote_df['Geographic Area Name'].unique())
    vote_df = vote_df[vote_df['Geographic Area Name'].isin(['GEORGIA', 'TEXAS'])]  # type: ignore
else:
    print("No state column found!")

# If you want to use national data for merging:
vote_df['state'] = 'UNITED STATES'

# Remove any duplicate rows
vote_df = vote_df.drop_duplicates()

# Remove rows with missing state data (check which column exists)
if 'state' in vote_df.columns:
    vote_df = vote_df.dropna(subset=['state'])
elif 'Geographic Area Name' in vote_df.columns:
    vote_df = vote_df.dropna(subset=['Geographic Area Name'])
else:
    # If neither column exists, just drop any completely empty rows
    vote_df = vote_df.dropna(how='all')

# View the cleaned dataset
print("Cleaned DataFrame:\n", vote_df.head())

# Save the cleaned voting data
vote_df.to_csv('cleaned_vote_percentages.csv', index=False)



