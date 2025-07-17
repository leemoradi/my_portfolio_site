import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def create_county_correlation_matrix():
    """Create a meaningful correlation matrix using county-level vote data"""
    
    # Load county vote percentages
    df = pd.read_csv('county_vote_percentages.csv')
    
    # Filter for Georgia and Texas only
    ga_tx_df = df[df['state'].isin(['GEORGIA', 'TEXAS'])]
    
    # Create correlation matrix with vote percentages and derived metrics
    corr_data = ga_tx_df[['Biden_pct', 'Trump_pct', 'Jorgensen_pct', 'total_votes']].copy()
    
    # Add derived metrics
    corr_data['margin'] = abs(corr_data['Biden_pct'] - corr_data['Trump_pct'])
    corr_data['biden_advantage'] = corr_data['Biden_pct'] - corr_data['Trump_pct']
    corr_data['total_votes_log'] = np.log10(corr_data['total_votes'])
    
    # Calculate correlation matrix
    corr_matrix = corr_data.corr()
    
    # Create the heatmap
    plt.figure(figsize=(10, 8))
    mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
    sns.heatmap(corr_matrix, 
               annot=True, 
               cmap='coolwarm', 
               fmt='.2f', 
               linewidths=0.5,
               mask=mask,
               square=True,
               cbar_kws={"shrink": .8})
    
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
    
    # Set style
    plt.style.use('default')
    sns.set_palette("husl")
    
    # Create correlation matrix
    corr_matrix = create_county_correlation_matrix()
    
    print("\n✓ Generated meaningful correlation matrix with county-level data")

if __name__ == "__main__":
    main() 