import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def create_actual_2020_results():
    """Create visualizations showing actual 2020 election results"""
    
    # Actual 2020 election results (Biden won Georgia)
    actual_results = pd.DataFrame({
        'state': ['GEORGIA', 'TEXAS'],
        'Biden': [49.5, 46.9],  # Biden won Georgia with 49.5%
        'Trump': [49.3, 52.1],   # Trump got 49.3% in Georgia
        'Other': [1.2, 1.0]      # Other candidates
    })
    
    # 1. Create a clear winner visualization
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Georgia results
    ga_data = actual_results[actual_results['state'] == 'GEORGIA']
    colors = ['#1f77b4', '#d62728', '#2ca02c']  # Blue for Biden, Red for Trump, Green for Other
    ax1.pie([ga_data['Biden'].iloc[0], ga_data['Trump'].iloc[0], ga_data['Other'].iloc[0]], 
             labels=['Biden (49.5%)', 'Trump (49.3%)', 'Other (1.2%)'],
             colors=colors, autopct='%1.1f%%', startangle=90)
    ax1.set_title('Georgia 2020 Election Results\n(Biden Won)', fontsize=14, fontweight='bold')
    
    # Texas results
    tx_data = actual_results[actual_results['state'] == 'TEXAS']
    ax2.pie([tx_data['Biden'].iloc[0], tx_data['Trump'].iloc[0], tx_data['Other'].iloc[0]], 
             labels=['Biden (46.9%)', 'Trump (52.1%)', 'Other (1.0%)'],
             colors=colors, autopct='%1.1f%%', startangle=90)
    ax2.set_title('Texas 2020 Election Results\n(Trump Won)', fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('visualizations/actual_2020_results.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 2. Create a bar chart showing the margin of victory
    plt.figure(figsize=(12, 6))
    
    # Calculate margins
    actual_results['margin'] = actual_results['Biden'] - actual_results['Trump']
    
    bars = plt.bar(actual_results['state'], actual_results['margin'], 
                   color=['#1f77b4' if x > 0 else '#d62728' for x in actual_results['margin']])
    
    # Add value labels on bars
    for bar, margin in zip(bars, actual_results['margin']):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + (0.1 if margin > 0 else -0.1), 
                f'{margin:+.1f}%', ha='center', va='bottom' if margin > 0 else 'top', 
                fontweight='bold', fontsize=12)
    
    plt.axhline(y=0, color='black', linestyle='-', alpha=0.3)
    plt.title('2020 Election: Biden vs Trump Margin of Victory', fontsize=14, fontweight='bold')
    plt.ylabel('Margin (Biden % - Trump %)', fontsize=12)
    plt.xlabel('State', fontsize=12)
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig('visualizations/2020_margin_of_victory.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print("✓ Generated actual 2020 election results visualizations")
    print("\nActual 2020 Results:")
    print(actual_results.to_string(index=False))
    
    return actual_results

def main():
    """Generate visualizations showing actual 2020 election results"""
    print("Creating visualizations with actual 2020 election results...")
    
    # Set style
    plt.style.use('default')
    sns.set_palette("husl")
    
    # Create visualizations
    actual_results = create_actual_2020_results()
    
    print("\n✓ Generated visualizations showing Biden's victory in Georgia")

if __name__ == "__main__":
    main() 