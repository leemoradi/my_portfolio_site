import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # Load Excel file
    file_path = 'data/county_info.xlsx'
    df = pd.read_excel(file_path)

    # Display first few rows and columns
    print("First 5 rows of the dataset:")
    print(df.head())
    print("\nColumns in dataset:")
    print(df.columns)

    # Standardize state names
    df['state'] = df['state'].str.upper()

    # Filter for GEORGIA and TEXAS
    states_of_interest = ['GEORGIA', 'TEXAS']
    filtered_df = df[df['state'].isin(states_of_interest)]

    # Count counties in each state
    print(f"\nNumber of counties in GEORGIA and TEXAS: {filtered_df['state'].value_counts().to_dict()}")

    # --- Chart 1: Number of Counties ---
    state_counts = filtered_df['state'].value_counts()
    sns.barplot(
        x=state_counts.index,
        y=state_counts.values,
        hue=state_counts.index,
        palette='viridis',
        legend=False
    )
    plt.title('Number of Counties in Georgia and Texas')
    plt.xlabel('State')
    plt.ylabel('County Count')
    plt.tight_layout()
    plt.show()

    # --- Chart 2: Vote Percentages by Candidate ---
    # Group by state and sum official votes
    vote_totals = filtered_df.groupby('state')[
        ['biden_official', 'trump_official', 'jorgensen_official']
    ].sum().reset_index()

    # Calculate total votes
    vote_totals['total_votes'] = vote_totals[
        ['biden_official', 'trump_official', 'jorgensen_official']
    ].sum(axis=1)

    # Calculate percentage of votes
    vote_totals['Biden'] = (vote_totals['biden_official'] / vote_totals['total_votes']) * 100
    vote_totals['Trump'] = (vote_totals['trump_official'] / vote_totals['total_votes']) * 100
    vote_totals['Jorgensen'] = (vote_totals['jorgensen_official'] / vote_totals['total_votes']) * 100

    # Keep only relevant percentage columns
    vote_percentages = vote_totals[['state', 'Biden', 'Trump', 'Jorgensen']]

    # Melt data for plotting
    melted = vote_percentages.melt(
        id_vars='state',
        var_name='Candidate',
        value_name='Percentage'
    )

    # Plot percentages
    plt.figure(figsize=(8, 5))
    sns.barplot(data=melted, x='state', y='Percentage', hue='Candidate', palette='pastel')
    plt.title('Vote Percentages by Candidate (Georgia vs. Texas)')
    plt.xlabel('State')
    plt.ylabel('Percentage of Total Votes')
    plt.tight_layout()
    plt.show()

    # Fill missing values with zero for all candidate columns
    for col in ['biden_official', 'trump_official', 'jorgensen_official']:
        filtered_df[col] = filtered_df[col].fillna(0)

    print(vote_percentages)
    print("\nCount of non-NaN Jorgensen votes by state:")
    print(filtered_df.groupby('state')['jorgensen_official'].count())

if __name__ == "__main__":
    main()

