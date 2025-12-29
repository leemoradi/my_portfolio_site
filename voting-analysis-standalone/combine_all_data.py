import pandas as pd

# Load existing vote data (replace with your actual filename if different)
votes_df = pd.read_csv("vote_percentages.csv")

# Load Census data
income_df = pd.read_csv("merged_income.csv")
education_df = pd.read_csv("merged_education.csv")

# Standardize column names for merging
votes_df['state'] = votes_df['state'].astype(str).str.strip().str.upper()
if 'Year' not in votes_df.columns:
    votes_df['Year'] = '2020'
votes_df['Year'] = votes_df['Year'].astype(str).str.strip()
income_df['Geographic Area Name'] = income_df['Geographic Area Name'].astype(str).str.strip().str.upper()
income_df['Year'] = income_df['Year'].astype(str).str.strip()
education_df['Geographic Area Name'] = education_df['Geographic Area Name'].astype(str).str.strip().str.upper()
education_df['Year'] = education_df['Year'].astype(str).str.strip()

# Merge datasets on state and year
combined_df = votes_df.merge(income_df, how="left", left_on=["state", "Year"], right_on=["Geographic Area Name", "Year"])
combined_df = combined_df.merge(education_df, how="left", left_on=["state", "Year"], right_on=["Geographic Area Name", "Year"])

# Save result
combined_df.to_csv("combined_voting_dataset.csv", index=False)
print("✅ Combined dataset saved as combined_voting_dataset.csv")
