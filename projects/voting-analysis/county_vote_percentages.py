import pandas as pd

def main():
    # Load the county-level voting data
    df = pd.read_excel('data/county_info.xlsx')

    # Only keep rows with valid vote counts
    vote_cols = ['biden_official', 'trump_official', 'jorgensen_official']
    df = df.dropna(subset=vote_cols, how='all')

    # Fill missing values with 0 for vote counts
    df[vote_cols] = df[vote_cols].fillna(0)

    # Calculate total votes per county
    df['total_votes'] = df['biden_official'] + df['trump_official'] + df['jorgensen_official']

    # Avoid division by zero
    df = df[df['total_votes'] > 0]

    # Calculate vote percentages
    df['Biden_pct'] = df['biden_official'] / df['total_votes'] * 100
    df['Trump_pct'] = df['trump_official'] / df['total_votes'] * 100
    df['Jorgensen_pct'] = df['jorgensen_official'] / df['total_votes'] * 100

    # Select relevant columns
    out_cols = ['state', 'county_name', 'Biden_pct', 'Trump_pct', 'Jorgensen_pct', 'total_votes']
    out_df = df[out_cols].copy()

    # Save to CSV (ensure out_df is a DataFrame)
    if isinstance(out_df, pd.DataFrame):
        out_df.to_csv('county_vote_percentages.csv', index=False)
        print('Saved county_vote_percentages.csv with', len(out_df), 'rows.')

if __name__ == "__main__":
    main() 