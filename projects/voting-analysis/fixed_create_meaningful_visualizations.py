
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

def create_county_vote_analysis():
    """Create meaningful visualizations using county-level vote data"""

    # Ensure output directory exists
    os.makedirs('visualizations', exist_ok=True)

    try:
        df = pd.read_csv('county_vote_percentages.csv')
    except FileNotFoundError:
        print("❌ Error: 'county_vote_percentages.csv' not found.")
        return

    required_cols = ['state', 'county_name', 'Biden_pct', 'Trump_pct']
    for col in required_cols:
        if col not in df.columns:
            print(f"❌ Error: Required column '{col}' is missing.")
            return

    # Filter for Georgia and Texas only
    ga_tx_df = df[df['state'].isin(['GEORGIA', 'TEXAS'])].copy()

    print(f"Found {len(ga_tx_df)} counties in Georgia and Texas")
    print(f"Georgia counties: {len(ga_tx_df[ga_tx_df['state'] == 'GEORGIA'])}")
    print(f"Texas counties: {len(ga_tx_df[ga_tx_df['state'] == 'TEXAS'])}")

    # 1. Scatter plot: Biden vs Trump
    plt.figure(figsize=(12, 8))
    ga = ga_tx_df[ga_tx_df['state'] == 'GEORGIA']
    tx = ga_tx_df[ga_tx_df['state'] == 'TEXAS']

    plt.scatter(ga['Trump_pct'], ga['Biden_pct'], alpha=0.7, color='blue', s=50, label='Georgia Counties')
    plt.scatter(tx['Trump_pct'], tx['Biden_pct'], alpha=0.7, color='red', s=50, label='Texas Counties')

    max_val = max(ga_tx_df['Biden_pct'].max(), ga_tx_df['Trump_pct'].max())
    x_vals = np.array([0, max_val])
    plt.plot(x_vals, x_vals, 'k--', alpha=0.5, label='Equal Vote Share')

    plt.xlabel('Trump Vote Percentage (%)', fontsize=12)
    plt.ylabel('Biden Vote Percentage (%)', fontsize=12)
    plt.title('County-Level Biden vs Trump Vote Percentages: Georgia vs Texas', fontsize=14, fontweight='bold')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('visualizations/county_biden_vs_trump.png', dpi=300, bbox_inches='tight')
    plt.close()

    # 2. Vote distributions
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    ax1.hist(ga['Biden_pct'], bins=20, alpha=0.7, color='blue', label='Biden')
    ax1.hist(ga['Trump_pct'], bins=20, alpha=0.7, color='red', label='Trump')
    ax1.set_xlabel('Vote Percentage (%)')
    ax1.set_ylabel('Number of Counties')
    ax1.set_title('Georgia County Vote Distribution', fontsize=14, fontweight='bold')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    ax2.hist(tx['Biden_pct'], bins=20, alpha=0.7, color='blue', label='Biden')
    ax2.hist(tx['Trump_pct'], bins=20, alpha=0.7, color='red', label='Trump')
    ax2.set_xlabel('Vote Percentage (%)')
    ax2.set_ylabel('Number of Counties')
    ax2.set_title('Texas County Vote Distribution', fontsize=14, fontweight='bold')
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('visualizations/county_vote_distributions.png', dpi=300, bbox_inches='tight')
    plt.close()

    # 3. Summary statistics
    print("\nSummary Statistics:")
    print("Georgia - Biden avg:", round(ga['Biden_pct'].mean(), 2), "| Trump avg:", round(ga['Trump_pct'].mean(), 2))
    print("Texas - Biden avg:", round(tx['Biden_pct'].mean(), 2), "| Trump avg:", round(tx['Trump_pct'].mean(), 2))

    # 4. Closest counties
    ga_tx_df['margin'] = (ga_tx_df['Biden_pct'] - ga_tx_df['Trump_pct']).abs()
    closest_races = ga_tx_df.nsmallest(10, 'margin')[['state', 'county_name', 'Biden_pct', 'Trump_pct', 'margin']]

    print("\n10 Closest County Races:")
    print(closest_races.to_string(index=False))

    return ga_tx_df

def main():
    print("Creating county-level vote analysis visualizations...")
    plt.style.use('default')
    sns.set_palette("husl")
    create_county_vote_analysis()
    print("\n✓ All visualizations and summaries generated.")

if __name__ == "__main__":
    main()
