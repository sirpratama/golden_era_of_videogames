import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.patches import Rectangle
import warnings
warnings.filterwarnings('ignore')

# Set style for professional-looking plots
plt.style.use('default')
sns.set_palette("husl")

# Create the datasets based on SQL analysis results
def create_datasets():
    # Best Selling Games data
    best_selling_games = pd.DataFrame({
        'name': [
            'Wii Sports for Wii',
            'Super Mario Bros. for NES', 
            'Counter-Strike: Global Offensive for PC',
            'Mario Kart Wii for Wii',
            "PLAYERUNKNOWN'S BATTLEGROUNDS for PC",
            'Minecraft for PC',
            'Wii Sports Resort for Wii',
            'Pokemon Red / Green / Blue Version for GB',
            'New Super Mario Bros. for DS',
            'New Super Mario Bros. Wii for Wii'
        ],
        'games_sold': [82.9, 40.24, 40, 37.32, 36.6, 33.15, 33.13, 31.38, 30.8, 30.3],
        'year': [2006, 1985, 2012, 2008, 2017, 2010, 2009, 1998, 2006, 2009],
        'platform': ['Wii', 'NES', 'PC', 'Wii', 'PC', 'PC', 'Wii', 'GB', 'DS', 'Wii']
    })
    
    # Critics Top Ten Years data
    critics_top_years = pd.DataFrame({
        'year': [1998, 2004, 2002, 1999, 2001, 2011, 2016, 2013, 2008, 2017],
        'num_games': [10, 11, 9, 11, 13, 26, 13, 18, 20, 13],
        'avg_critic_score': [9.32, 9.03, 8.99, 8.93, 8.82, 8.76, 8.67, 8.66, 8.63, 8.62]
    })

    user_score_top_ten_years = pd.DataFrame({
        'year': [1997, 1998, 2010, 2009, 2008, 1996, 2005, 2006, 2000, 2002],
        'num_games': [8, 10, 23, 20, 20, 5, 13, 16, 8, 9],
        'avg_user_score': [9.5, 9.4, 9.24, 9.18, 9.03, 9, 8.95, 8.95, 8.80, 8.80]
    })
    
    # Golden Years data
    golden_years = pd.DataFrame({
        'year': [1997, 1998, 2004, 2008, 2009, 2010],
        'num_games': [8, 10, 11, 20, 20, 23],
        'avg_user_score': [9.5, 9.4, 8.55, 9.03, 9.18, 9.24],
        'avg_critic_score': [7.93, 9.32, 9.03, 8.63, 8.55, 8.41],
        'diff': [-1.57, -0.08, 0.48, -0.4, -0.63, -0.83]
    })
    
    return best_selling_games, critics_top_years, golden_years, user_score_top_ten_years

def create_visualizations():
    # Get datasets
    best_selling_games, critics_top_years, golden_years, user_score_top_ten_years = create_datasets()
    
    # Create a figure with multiple subplots - increased size and better spacing
    fig = plt.figure(figsize=(24, 30))
    
    # 1. Best Selling Games - Horizontal Bar Chart
    ax1 = plt.subplot(4, 2, (1, 2))
    
    # Simplify game names for better display
    simplified_names = [name.split(' for ')[0] for name in best_selling_games['name']]
    colors = plt.cm.viridis(np.linspace(0, 1, len(best_selling_games)))
    
    bars = ax1.barh(range(len(best_selling_games)), best_selling_games['games_sold'], 
                    color=colors, alpha=0.8, edgecolor='black', linewidth=0.5)
    
    ax1.set_yticks(range(len(best_selling_games)))
    ax1.set_yticklabels(simplified_names, fontsize=10)
    ax1.set_xlabel('Games Sold (Millions)', fontsize=11, fontweight='bold')
    ax1.set_title('Top 10 Best-Selling Video Games of All Time', fontsize=14, fontweight='bold', pad=15)
    ax1.grid(axis='x', alpha=0.3)
    ax1.invert_yaxis()  # Highest selling at top
    
    # Add value labels on bars
    for i, (bar, value) in enumerate(zip(bars, best_selling_games['games_sold'])):
        ax1.text(value + 1, bar.get_y() + bar.get_height()/2, 
                f'{value}M', va='center', fontsize=9, fontweight='bold')
    
    # 2. Critics Top Years - Bar Chart (Ordered by Score)
    ax2 = plt.subplot(4, 2, 3)
    
    # Sort data by critic score in descending order (highest first)
    critics_sorted = critics_top_years.sort_values('avg_critic_score', ascending=False)
    
    bars = ax2.bar(critics_sorted['year'].astype(str), critics_sorted['avg_critic_score'], 
                   color='#e74c3c', alpha=0.7, edgecolor='black', linewidth=0.5)
    
    ax2.set_xlabel('Year', fontsize=9, fontweight='bold')
    ax2.set_ylabel('Average Critic Score', fontsize=11, fontweight='bold')
    ax2.set_title('Top 10 Years with Highest Critic Ratings (Ranked)', fontsize=12, fontweight='bold', pad=15)
    ax2.grid(axis='y', alpha=0.3)
    ax2.set_ylim(8.4, 9.5)
    
    # Rotate x-axis labels for better readability
    plt.setp(ax2.xaxis.get_majorticklabels(), rotation=0, fontsize=9)
    
    # Add value labels on top of bars
    for bar, score in zip(bars, critics_sorted['avg_critic_score']):
        ax2.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.02,
                f'{score:.2f}', ha='center', va='bottom', fontsize=8, fontweight='bold')
    
    # 3. User Score Top Years - Ranked by Average User Score
    ax3 = plt.subplot(4, 2, 4)
    user_score_top_ten_years_sorted = user_score_top_ten_years.sort_values('avg_user_score', ascending=False)

    bars = ax3.bar(user_score_top_ten_years_sorted['year'].astype(str), user_score_top_ten_years_sorted['avg_user_score'], 
                   color='#3498db', alpha=0.7, edgecolor='black', linewidth=0.5)
    
    ax3.set_xlabel('Year', fontsize=9, fontweight='bold')
    ax3.set_ylabel('Average User Score', fontsize=11, fontweight='bold')
    ax3.set_title('Top 10 Years with Highest User Ratings (Ranked)', fontsize=12, fontweight='bold', pad=15)
    ax3.grid(axis='y', alpha=0.3)
    ax3.set_ylim(8.5, 9.7)
    plt.setp(ax3.xaxis.get_majorticklabels(), rotation=0, fontsize=9)
    
    # Add value labels on bars
    for bar, score in zip(bars, user_score_top_ten_years_sorted['avg_user_score']):
        ax3.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.02,
                f'{score:.2f}', ha='center', va='bottom', fontsize=8, fontweight='bold')
    
    # 4. Golden Years - User vs Critic Scores Comparison
    ax4 = plt.subplot(4, 2, 5)
    
    x = np.arange(len(golden_years))
    width = 0.35
    
    bars1 = ax4.bar(x - width/2, golden_years['avg_user_score'], width, 
                    label='User Score', color='#2ecc71', alpha=0.8, edgecolor='black', linewidth=0.5)
    bars2 = ax4.bar(x + width/2, golden_years['avg_critic_score'], width,
                    label='Critic Score', color='#e67e22', alpha=0.8, edgecolor='black', linewidth=0.5)
    
    ax4.set_xlabel('Year', fontsize=9, fontweight='bold')
    ax4.set_ylabel('Average Score', fontsize=11, fontweight='bold')
    ax4.set_title('Golden Years: User vs Critic Scores Comparison', fontsize=12, fontweight='bold', pad=15)
    ax4.set_xticks(x)
    ax4.set_xticklabels(golden_years['year'], fontsize=9)
    ax4.legend(fontsize=10)
    ax4.grid(axis='y', alpha=0.3)
    ax4.set_ylim(7, 10)
    
    # Add value labels
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax4.text(bar.get_x() + bar.get_width()/2., height + 0.05,
                    f'{height:.1f}', ha='center', va='bottom', fontsize=8, fontweight='bold')
    
    # 5. Golden Years - Score Difference Analysis
    ax5 = plt.subplot(4, 2, 6)
    
    colors = ['#e74c3c' if diff < 0 else '#27ae60' for diff in golden_years['diff']]
    bars = ax5.bar(golden_years['year'].astype(str), golden_years['diff'], 
                   color=colors, alpha=0.7, edgecolor='black', linewidth=0.5)
    
    ax5.axhline(y=0, color='black', linestyle='-', linewidth=1)
    ax5.set_xlabel('Year', fontsize=9, fontweight='bold')
    ax5.set_ylabel('Critic - User Score', fontsize=11, fontweight='bold')
    ax5.set_title('Golden Years: Critic vs User Score Differences', fontsize=12, fontweight='bold', pad=15)
    ax5.grid(axis='y', alpha=0.3)
    
    # Add value labels
    for bar, diff in zip(bars, golden_years['diff']):
        height = bar.get_height()
        ax5.text(bar.get_x() + bar.get_width()/2., 
                height + (0.05 if height >= 0 else -0.1),
                f'{diff:.2f}', ha='center', 
                va='bottom' if height >= 0 else 'top', 
                fontsize=9, fontweight='bold')
    
    # 6. Sales Performance Ranked by Year
    ax6 = plt.subplot(4, 2, 7)
    
    # Group sales by year and sort by total sales in descending order
    sales_by_year = best_selling_games.groupby('year')['games_sold'].sum().sort_values(ascending=False)
    
    bars = ax6.bar(sales_by_year.index.astype(str), sales_by_year.values, 
                   color='#9b59b6', alpha=0.7, edgecolor='black', linewidth=0.5)
    
    ax6.set_xlabel('Year', fontsize=9, fontweight='bold')
    ax6.set_ylabel('Total Sales (Millions)', fontsize=11, fontweight='bold')
    ax6.set_title('Sales Performance Ranked by Year (Top 10 Games)', fontsize=12, fontweight='bold', pad=15)
    ax6.grid(axis='y', alpha=0.3)
    plt.setp(ax6.xaxis.get_majorticklabels(), rotation=0, fontsize=9)
    
    # Add value labels on bars
    for bar, sales in zip(bars, sales_by_year.values):
        ax6.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 1,
                f'{sales:.1f}M', ha='center', va='bottom', fontsize=8, fontweight='bold')
    
    # 7. Timeline Analysis - Golden Years vs Sales
    ax7 = plt.subplot(4, 2, 8)
    
    # Create timeline data
    timeline_years = range(1985, 2018)
    sales_by_year = best_selling_games.groupby('year')['games_sold'].sum()
    
    # Plot sales timeline
    ax7_twin = ax7.twinx()
    
    # Sales bars
    years_with_sales = sales_by_year.index
    sales_values = sales_by_year.values
    ax7.bar(years_with_sales, sales_values, alpha=0.6, color='#95a5a6', 
            label='Total Sales (Top 10)', width=0.8)
    
    # Golden years markers
    golden_year_list = golden_years['year'].tolist()
    for year in golden_year_list:
        ax7_twin.axvline(x=year, color='#f39c12', linewidth=3, alpha=0.8, 
                        linestyle='--', label='Golden Years' if year == golden_year_list[0] else "")
    
    ax7.set_xlabel('Year', fontsize=9, fontweight='bold')
    ax7.set_ylabel('Sales (Millions)', fontsize=11, fontweight='bold', color='#95a5a6')
    ax7.set_title('Timeline: Sales Performance vs Golden Years', fontsize=12, fontweight='bold', pad=15)
    ax7.tick_params(axis='y', labelcolor='#95a5a6')
    ax7_twin.set_ylabel('Golden Years', fontsize=11, fontweight='bold', color='#f39c12')
    ax7_twin.tick_params(axis='y', labelcolor='#f39c12')
    ax7_twin.set_ylim(0, 1)
    ax7_twin.set_yticks([])
    
    # Add legends
    lines1, labels1 = ax7.get_legend_handles_labels()
    lines2, labels2 = ax7_twin.get_legend_handles_labels()
    ax7.legend(lines1 + lines2, labels1 + labels2, loc='upper left', fontsize=9)
    
    # Adjust layout with more spacing
    plt.subplots_adjust(
        left=0.08,      # Left margin
        bottom=0.08,    # Bottom margin  
        right=0.95,     # Right margin
        top=0.96,       # Top margin
        wspace=0.3,     # Width spacing between subplots
        hspace=0.4      # Height spacing between subplots
    )
    
    plt.savefig('video_game_analysis_visualizations.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # Create summary statistics
    print("=" * 60)
    print("VIDEO GAME ANALYSIS - KEY INSIGHTS")
    print("=" * 60)
    
    print(f"\n[CHART] BEST SELLING GAMES:")
    print(f"• Top game: {best_selling_games.iloc[0]['name']} ({best_selling_games.iloc[0]['games_sold']}M sales)")
    print(f"• Platform dominance: {best_selling_games['platform'].value_counts().index[0]} ({best_selling_games['platform'].value_counts().iloc[0]} games)")
    print(f"• Year range: {best_selling_games['year'].min()} - {best_selling_games['year'].max()}")
    
    print(f"\n[TROPHY] CRITICS' FAVORITE YEARS:")
    print(f"• Best year: {critics_top_years.iloc[0]['year']} (Score: {critics_top_years.iloc[0]['avg_critic_score']})")
    print(f"• Most productive year: {critics_top_years.loc[critics_top_years['num_games'].idxmax(), 'year']} ({critics_top_years['num_games'].max()} games)")
    print(f"• Average score range: {critics_top_years['avg_critic_score'].min():.2f} - {critics_top_years['avg_critic_score'].max():.2f}")
    
    print(f"\n[STAR] GOLDEN YEARS (User/Critic Score > 9.0):")
    print(f"• Golden years identified: {', '.join(map(str, golden_years['year'].tolist()))}")
    print(f"• Best user score: {golden_years['avg_user_score'].max():.1f} (Year: {golden_years.loc[golden_years['avg_user_score'].idxmax(), 'year']})")
    print(f"• Best critic score: {golden_years['avg_critic_score'].max():.2f} (Year: {golden_years.loc[golden_years['avg_critic_score'].idxmax(), 'year']})")
    print(f"• Biggest disagreement: {golden_years['diff'].min():.2f} (Year: {golden_years.loc[golden_years['diff'].idxmin(), 'year']})")
    
    print("\n" + "=" * 60)
    print("Visualization saved as 'video_game_analysis_visualizations.png'")
    print("=" * 60)

if __name__ == "__main__":
    create_visualizations() 