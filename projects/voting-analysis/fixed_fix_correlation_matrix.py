import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

def create_county_correlation_matrix():
    """Create a meaningful correlation matrix using county-level vote data"""

    try:
        df = pd.read_csv('county_vote_percentages.csv')
    except FileNotFoundError:
        print("❌ Error: 'county_vote_percentages.csv' not found.")
        return

    # Filter for Georgia and Texas only
    if 'state' not in df.columns:
        print("❌ Error: 'state' column missing in data.")
        return

    ga_tx_df = df[df['state'].isin(['GEORGIA', 'TEXAS'])]

    # Required columns
    required_cols = ['Biden_pct', 'Trump_pct', 'Jorgensen_pct', 'total_votes']
    corr_data = pd.DataFrame(ga_tx_df[required_cols].copy())

    corr_data['margin'] = abs(corr_data['Biden_pct'] - corr_data['Trump_pct'])
    corr_data['biden_advantage'] = corr_data['Biden_pct'] - corr_data['Trump_pct']
    corr_data['total_votes_log'] = np.log10(corr_data['total_votes'] + 1)

    corr_matrix = corr_data.corr()

    # Ensure output directory exists
    os.makedirs('visualizations', exist_ok=True)

    # Create the heatmap
    plt.figure(figsize=(10, 8))
    mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
    sns.heatmap(
        corr_matrix,
        annot=True,
        cmap='coolwarm',
        fmt='.2f',
        linewidths=0.5,
        mask=mask,
        square=True,
        cbar_kws={"shrink": .8}
    )

    plt.title('Correlation Matrix: County-Level Voting Patterns', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig('visualizations/county_correlation_matrix.png', dpi=300, bbox_inches='tight')
    plt.close()

    print("✓ Generated county-level correlation matrix")
    print("\nCorrelation Matrix:")
    print(corr_matrix.round(3))

    return corr_matrix

def main():
    """Generate a meaningful correlation matrix"""
    print("Creating county-level correlation matrix...")
    plt.style.use('default')
    sns.set_palette("husl")
    create_county_correlation_matrix()

if __name__ == "__main__":
    main()
