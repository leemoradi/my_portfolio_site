
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

def create_actual_2020_results():
    """Create visualizations showing actual 2020 election results"""

    # Ensure output directory exists
    os.makedirs('visualizations', exist_ok=True)

    # Actual 2020 election results (Biden won Georgia)
    actual_results = pd.DataFrame({
        'state': ['GEORGIA', 'TEXAS'],
        'Biden': [49.5, 46.9],
        'Trump': [49.3, 52.1],
        'Other': [1.2, 1.0]
    })

    # 1. Create a pie chart visualization
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    colors = ['#1f77b4', '#d62728', '#2ca02c']  # Blue, Red, Green

    try:
        ga_data = actual_results[actual_results['state'] == 'GEORGIA'].iloc[0]
        ax1.pie([ga_data['Biden'], ga_data['Trump'], ga_data['Other']], 
                labels=[f'Biden ({ga_data["Biden"]}%)', f'Trump ({ga_data["Trump"]}%)', f'Other ({ga_data["Other"]}%)'],
                colors=colors, autopct='%1.1f%%', startangle=90)
        ax1.set_title('Georgia 2020 Election Results\n(Biden Won)', fontsize=14, fontweight='bold')
    except IndexError:
        print("❌ Georgia data missing")

    try:
        tx_data = actual_results[actual_results['state'] == 'TEXAS'].iloc[0]
        ax2.pie([tx_data['Biden'], tx_data['Trump'], tx_data['Other']], 
                labels=[f'Biden ({tx_data["Biden"]}%)', f'Trump ({tx_data["Trump"]}%)', f'Other ({tx_data["Other"]}%)'],
                colors=colors, autopct='%1.1f%%', startangle=90)
        ax2.set_title('Texas 2020 Election Results\n(Trump Won)', fontsize=14, fontweight='bold')
    except IndexError:
        print("❌ Texas data missing")

    plt.tight_layout()
    plt.savefig('visualizations/actual_2020_results.png', dpi=300, bbox_inches='tight')
    plt.close()

    # 2. Bar chart for margin of victory
    actual_results['margin'] = actual_results['Biden'] - actual_results['Trump']

    plt.figure(figsize=(12, 6))
    bars = plt.bar(actual_results['state'], actual_results['margin'], 
                   color=['#1f77b4' if x > 0 else '#d62728' for x in actual_results['margin']])

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
    print("Creating visualizations with actual 2020 election results...")
    plt.style.use('default')
    sns.set_palette("husl")
    create_actual_2020_results()

if __name__ == "__main__":
    main()
