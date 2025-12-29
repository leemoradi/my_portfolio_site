import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def generate_vote_percentages_chart():
    """Generate the main vote percentages comparison chart"""
    # Load the vote percentages data
    vote_percentages = pd.read_csv('vote_percentages.csv')
    
    # Melt data for plotting
    melted = vote_percentages.melt(
        id_vars='state',
        var_name='Candidate',
        value_name='Percentage'
    )
    
    # Create the plot
    plt.figure(figsize=(10, 6))
    colors = ['#1f77b4', '#d62728', '#2ca02c']  # Blue for Biden, Red for Trump, Green for Jorgensen
    sns.barplot(data=melted, x='state', y='Percentage', hue='Candidate', palette=colors)
    plt.title('Vote Percentages by Candidate: Georgia vs. Texas (2020 Election)', fontsize=14, fontweight='bold')
    plt.xlabel('State', fontsize=12)
    plt.ylabel('Percentage of Total Votes (%)', fontsize=12)
    plt.legend(title='Candidate', title_fontsize=12)
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig('vote_percentages_chart.png', dpi=300, bbox_inches='tight')
    plt.close()

def generate_income_vs_biden_scatter():
    """Generate scatter plot of income vs Biden vote percentage"""
    # Load the merged dataset
    merged_df = pd.read_csv('merged_voting_data.csv')
    
    # Create scatter plot
    plt.figure(figsize=(12, 8))
    plt.scatter(merged_df['Estimate!!Median household income in the past 12 months (in 2020 inflation-adjusted dollars)'], 
                merged_df['Biden'], alpha=0.7, color='#1f77b4', s=100)
    
    # Add trend line
    x = merged_df['Estimate!!Median household income in the past 12 months (in 2020 inflation-adjusted dollars)']
    y = merged_df['Biden']
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    plt.plot(x, p(x), "r--", alpha=0.8, linewidth=2)
    
    plt.title('Income vs. Biden Vote Percentage', fontsize=14, fontweight='bold')
    plt.xlabel('Median Household Income (2020, Inflation-adjusted dollars)', fontsize=12)
    plt.ylabel('Biden Vote Percentage (%)', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('visualizations/income_vs_biden.png', dpi=300, bbox_inches='tight')
    plt.close()

def generate_correlation_matrix():
    """Generate correlation matrix heatmap"""
    # Load the merged dataset
    merged_df = pd.read_csv('merged_voting_data.csv')
    
    # Select relevant columns for correlation
    corr_columns = [
        'Biden', 
        'Trump', 
        'Jorgensen', 
        'Estimate!!Median household income in the past 12 months (in 2020 inflation-adjusted dollars)',
        "Estimate!!Total!!Bachelor's degree"
    ]
    
    # Ensure all columns exist
    available_cols = [col for col in corr_columns if col in merged_df.columns]
    
    if len(available_cols) >= 2:
        corr_matrix = merged_df.loc[:, available_cols].corr()
        
        # Create heatmap
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
        plt.title('Correlation Matrix: Voting Patterns, Income, and Education', fontsize=14, fontweight='bold')
        plt.tight_layout()
        plt.savefig('visualizations/correlation_matrix.png', dpi=300, bbox_inches='tight')
        plt.close()

def generate_county_comparison():
    """Generate county count comparison chart"""
    # Load the original data
    file_path = 'data/county_info.xlsx'
    df = pd.read_excel(file_path)
    
    # Standardize state names and filter
    df['state'] = df['state'].str.upper()
    states_of_interest = ['GEORGIA', 'TEXAS']
    filtered_df = df[df['state'].isin(states_of_interest)]
    
    # Count counties
    state_counts = pd.Series(filtered_df['state']).value_counts()
    
    # Create bar chart
    plt.figure(figsize=(10, 6))
    colors = ['#1f77b4', '#d62728']  # Blue for Georgia, Red for Texas
    bars = plt.bar(state_counts.index, state_counts.values, color=colors, alpha=0.8)
    
    # Add value labels on bars
    for bar, value in zip(bars, state_counts.values):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, 
                str(value), ha='center', va='bottom', fontweight='bold')
    
    plt.title('Number of Counties: Georgia vs. Texas', fontsize=14, fontweight='bold')
    plt.xlabel('State', fontsize=12)
    plt.ylabel('Number of Counties', fontsize=12)
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig('visualizations/county_comparison.png', dpi=300, bbox_inches='tight')
    plt.close()

def main():
    """Generate all figures for the voting analysis project"""
    print("Generating all figures for the voting analysis project...")
    
    # Set style
    plt.style.use('default')
    sns.set_palette("husl")
    
    # Generate all figures
    try:
        generate_vote_percentages_chart()
        print("✓ Generated vote percentages chart")
        
        generate_income_vs_biden_scatter()
        print("✓ Generated income vs Biden scatter plot")
        
        generate_correlation_matrix()
        print("✓ Generated correlation matrix")
        
        generate_county_comparison()
        print("✓ Generated county comparison chart")
        
        print("\nAll figures generated successfully!")
        
    except Exception as e:
        print(f"Error generating figures: {e}")

if __name__ == "__main__":
    main() 