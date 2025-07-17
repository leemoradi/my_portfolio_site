import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned datasets
vote_df = pd.read_csv('cleaned_vote_percentages.csv')
income_df = pd.read_csv('cleaned_income.csv')
education_df = pd.read_csv('cleaned_education.csv')

# Merge the datasets on 'state' and 'year'
merged_df = vote_df.merge(income_df, how='inner', left_on=['state', 'Year'], right_on=['Geographic Area Name', 'Year'])
merged_df = merged_df.merge(education_df, how='inner', left_on=['state', 'Year'], right_on=['Geographic Area Name', 'Year'])

# View the merged dataset
print(merged_df.head())

# Save the merged dataset to a new CSV file
merged_df.to_csv('merged_voting_data.csv', index=False)

# Scatter plot: Income vs. Biden vote percentage
plt.figure(figsize=(10, 6))
plt.scatter(merged_df['Estimate!!Median household income in the past 12 months (in 2020 inflation-adjusted dollars)'], 
            merged_df['Biden'], alpha=0.5, color='blue')
plt.title('Income vs. Biden Vote Percentage')
plt.xlabel('Median Household Income (2020, Inflation-adjusted)')
plt.ylabel('Biden Vote Percentage')
plt.grid(True)
plt.savefig('visualizations/income_vs_biden.png')  # Save the plot as an image
plt.show()

# Calculate the correlation matrix
corr_columns = [
    'Biden', 
    'Trump', 
    'Jorgensen', 
    'Estimate!!Median household income in the past 12 months (in 2020 inflation-adjusted dollars)',
    "Estimate!!Total!!Bachelor's degree"
]
# Ensure all columns exist in the merged_df before calculating correlation
missing_cols = [col for col in corr_columns if col not in merged_df.columns]
if missing_cols:
    print(f"Warning: The following columns are missing from merged_df and will be skipped in correlation: {missing_cols}")
    corr_columns = [col for col in corr_columns if col in merged_df.columns]

if len(corr_columns) >= 2:
    corr_matrix = merged_df.loc[:, corr_columns].corr()
    # Plot the correlation matrix using seaborn
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title('Correlation Matrix: Voting Patterns, Income, and Education')
    plt.savefig('visualizations/correlation_matrix.png')  # Save the plot as an image
    plt.show()
else:
    print("Not enough valid columns available for correlation matrix.")

# Check column names in each dataset
print("Vote Data Columns:", vote_df.columns)
print("Income Data Columns:", income_df.columns)
print("Education Data Columns:", education_df.columns)
# Check column names in each dataset
print("Vote Data Columns:", vote_df.columns)
print("Income Data Columns:", income_df.columns)
print("Education Data Columns:", education_df.columns)

# Inspect the first few rows of each dataset to check the data
print("First few rows of Vote Data:\n", vote_df.head())
print("First few rows of Income Data:\n", income_df.head())
print("First few rows of Education Data:\n", education_df.head())
