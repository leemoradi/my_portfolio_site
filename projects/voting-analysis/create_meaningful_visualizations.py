import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def create_county_vote_analysis():
    """Create meaningful visualizations using county-level vote data"""
    
    # Load county vote percentages
    df = pd.read_csv('county_vote_percentages.csv')
    
    # Filter for Georgia and Texas only
    ga_tx_df = df[df['state'].isin(['GEORGIA', 'TEXAS'])]
    
    print(f"Found {len(ga_tx_df)} counties in Georgia and Texas")
    print(f"Georgia counties: {len(ga_tx_df[ga_tx_df['state'] == 'GEORGIA'])}")
    print(f"Texas counties: {len(ga_tx_df[ga_tx_df['state'] == 'TEXAS'])}")
    
    # 1. County-level Biden vs Trump scatter plot
    plt.figure(figsize=(12, 8))
    
    # Plot Georgia counties in blue
    ga_data = ga_tx_df[ga_tx_df['state'] == 'GEORGIA']
    plt.scatter(ga_data['Trump_pct'], ga_data['Biden_pct'], 
                alpha=0.7, color='blue', s=50, label='Georgia Counties')
    
    # Plot Texas counties in red
    tx_data = ga_tx_df[ga_tx_df['state'] == 'TEXAS']
    plt.scatter(tx_data['Trump_pct'], tx_data['Biden_pct'], 
                alpha=0.7, color='red', s=50, label='Texas Counties')
    
    # Add diagonal line (equal vote share)
    max_val = float(max(ga_tx_df['Biden_pct'].max(), ga_tx_df['Trump_pct'].max()))
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
    
    # 2. Vote distribution by state
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Georgia distribution
    ga_data = ga_tx_df[ga_tx_df['state'] == 'GEORGIA']
    ax1.hist(ga_data['Biden_pct'], bins=20, alpha=0.7, color='blue', label='Biden')
    ax1.hist(ga_data['Trump_pct'], bins=20, alpha=0.7, color='red', label='Trump')
    ax1.set_xlabel('Vote Percentage (%)', fontsize=12)
    ax1.set_ylabel('Number of Counties', fontsize=12)
    ax1.set_title('Georgia County Vote Distribution', fontsize=14, fontweight='bold')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Texas distribution
    tx_data = ga_tx_df[ga_tx_df['state'] == 'TEXAS']
    ax2.hist(tx_data['Biden_pct'], bins=20, alpha=0.7, color='blue', label='Biden')
    ax2.hist(tx_data['Trump_pct'], bins=20, alpha=0.7, color='red', label='Trump')
    ax2.set_xlabel('Vote Percentage (%)', fontsize=12)
    ax2.set_ylabel('Number of Counties', fontsize=12)
    ax2.set_title('Texas County Vote Distribution', fontsize=14, fontweight='bold')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('visualizations/county_vote_distributions.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 3. Summary statistics
    print("\nSummary Statistics:")
    print("Georgia - Biden avg:", ga_data['Biden_pct'].mean(), "Trump avg:", ga_data['Trump_pct'].mean())
    print("Texas - Biden avg:", tx_data['Biden_pct'].mean(), "Trump avg:", tx_data['Trump_pct'].mean())
    
    # 4. Most competitive counties (closest races)
    ga_tx_df['margin'] = (ga_tx_df['Biden_pct'] - ga_tx_df['Trump_pct']).abs()
    closest_races = ga_tx_df.nsmallest(10, 'margin')[['state', 'county_name', 'Biden_pct', 'Trump_pct', 'margin']]

    print("\n10 Closest County Races:")
    print(closest_races.to_string(index=False))
    
    return ga_tx_df

def main():
    """Generate all county-level visualizations"""
    print("Creating county-level vote analysis visualizations...")
    
    # Set style
    plt.style.use('default')
    sns.set_palette("husl")
    
    # Create visualizations
    county_data = create_county_vote_analysis()
    
    print("\n✓ Generated county-level visualizations:")
    print("  - County Biden vs Trump scatter plot")
    print("  - County vote distributions by state")
    print("  - Summary statistics and closest races")

if __name__ == "__main__":
    main() 