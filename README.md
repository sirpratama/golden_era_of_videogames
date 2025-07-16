# Golden Age of Video Games Analysis

![Video Game Analysis Visualizations](video_game_analysis_visualization)

## Project Goal

This project analyzes video game critic scores, user scores, and sales data for the top 400 video games released since 1977 to investigate whether a "golden age" of video games exists. The analysis aims to identify the best-selling games, the years most favored by critics and users, and periods where both critics and users highly rated games.

## Data

The analysis uses a database containing information on ~400 top video games. The primary tables used are:

*   **`game_sales`**: Contains game titles, platform, publisher, developer, sales figures (in millions), and release year.
*   **`reviews`**: Contains game titles, critic scores (Metacritic), and user scores (Metacritic).
*   **`users_avg_year_rating`**: Contains aggregated average user scores per year.
*   **`critics_avg_year_rating`**: Contains aggregated average critic scores per year.

*(Note: The dataset used is a subset of a larger Kaggle dataset.)*

## Analysis Overview

The analysis was performed using SQL queries within a Jupyter Notebook environment and comprehensive data visualizations using Python. Key analyses included:

### 1. Top 10 Best-Selling Games Analysis
- **Query Focus**: Identifying the all-time best-selling games based on the `games_sold` column
- **Key Finding**: **Wii Sports** dominates with 82.9M sales, followed by Super Mario Bros. (40.24M)
- **Platform Dominance**: Wii platform has 4 games in the top 10 best-sellers
- **Time Range**: Best-sellers span from 1985 to 2017, showing gaming's evolution

### 2. Critics' Top-Rated Years Analysis
- **Query Focus**: Determining years with highest average critic scores (minimum 4 games per year)
- **Golden Critic Year**: **1998** stands out with the highest average critic score of 9.32
- **Score Range**: Top critic years range from 8.62 to 9.32 average scores
- **Most Productive Year**: **2011** had 26 games released among top-rated years

### 3. Golden Years Identification
- **Methodology**: Finding years where user scores OR critic scores exceeded 9.0
- **Golden Years Identified**: **1997, 1998, 2004, 2008, 2009, 2010**
- **Best User Year**: **1997** with 9.5 average user score
- **Best Critic Year**: **1998** with 9.32 average critic score
- **Biggest Disagreement**: **1997** (-1.57 difference, users loved it more than critics)

## Key Insights

📊 **Sales Performance**
- Wii Sports (82.9M) outsold the second-place game by more than 2x
- Nintendo dominates the best-seller list with multiple titles
- PC gaming shows strong presence with modern titles like PUBG and Minecraft

🏆 **Critical Reception Timeline**
- Late 1990s and early 2000s represent peak critical appreciation
- 1998-2004 period shows consistently high critic scores
- Modern gaming (2008-2017) maintains quality but with different dynamics

🌟 **Golden Era Analysis**
- The "Golden Age" spans approximately **1997-2010**
- Users and critics don't always agree - users were more enthusiastic in 1997
- 1998 represents the convergence point of both user and critic appreciation

## Visualizations

The project includes comprehensive data visualizations created with Python (matplotlib/seaborn):

1. **Best-Selling Games** - Horizontal bar chart showing top 10 games by sales
2. **Critics' Timeline** - Line chart displaying critic score trends over top years
3. **Game Production** - Bar chart showing number of games released in top years
4. **User vs Critic Comparison** - Side-by-side comparison for golden years
5. **Score Differences** - Diverging bar chart showing agreement/disagreement
6. **Platform Distribution** - Pie chart of sales by gaming platform
7. **Timeline Overview** - Combined view of sales performance vs golden years

## Project Structure

```
golden_era_of_videogames/
├── notebook.ipynb                          # Main SQL analysis notebook
├── video_game_visualizations.py            # Python visualization script
├── requirements.txt                        # Python dependencies
├── README.md                               # Project documentation
├── video_game_analysis_visualizations.png  # Generated charts (output)
└── video_game.jpg                         # Project header image
```

## Tools & Technologies Used

- **SQL (PostgreSQL)** - Data querying and analysis
- **Jupyter Notebook** - Interactive analysis environment
- **Python** - Data visualization and processing
  - pandas - Data manipulation
  - matplotlib - Chart creation
  - seaborn - Statistical visualization
  - numpy - Numerical operations

## How to Run the Analysis

### Prerequisites
```bash
pip install -r requirements.txt
```

### Generate Visualizations
```bash
python video_game_visualizations.py
```

This will:
- Create comprehensive visualizations of all key findings
- Save high-quality charts as `video_game_analysis_visualizations.png`
- Display summary statistics in the terminal

### View SQL Analysis
Open `notebook.ipynb` in Jupyter Notebook to explore the original SQL queries and data analysis.

## Results & Conclusions

### Does a Golden Age of Video Games Exist?

**Yes**, based on our analysis, there was indeed a "Golden Age" of video games spanning approximately **1997-2010**. This period is characterized by:

- **Exceptional Quality**: Both users and critics rated games above 9.0 during these years
- **Diverse Excellence**: Multiple years showing consistently high ratings
- **Balanced Perspective**: Both user enthusiasm and critical acclaim aligned
- **Innovation Period**: This era saw revolutionary games that defined modern gaming

### The Golden Age Characteristics:

1. **Peak Critical Appreciation (1998)**: Highest critic scores in gaming history
2. **User Enthusiasm (1997)**: Maximum user satisfaction and engagement  
3. **Sustained Quality (1997-2010)**: 6 consecutive golden years
4. **Commercial Success**: Many golden age games became best-sellers

The data suggests that while great games continue to be made, the late 1990s to early 2010s represented a unique convergence of innovation, quality, and widespread appreciation that defines the "Golden Age of Video Games."

---

*Analysis conducted as part of data science portfolio project exploring gaming industry trends and consumer behavior.* 
