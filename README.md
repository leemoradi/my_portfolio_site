# Leah's Portfolio Website

My personal portfolio showcases data analysis projects with a focus on electoral analysis and political data visualization.

## Live Demo

Visit my portfolio at: https://leemoradi.github.io/my_portfolio_site/

## Project Structure

```
my_portfolio_site/
├── index.html                 # Home page
├── projects.html              # Main projects overview
├── voting-analysis-project.html  # Detailed voting analysis page
├── style.css                  # Main stylesheet
└── projects/
    └── voting-analysis/       # Voting analysis project
        ├── data/              # Raw and processed data files
        ├── visualizations/    # Generated charts and graphs
        ├── css/              # Project-specific styles
        ├── *.py              # Python analysis scripts
        ├── *.csv             # Processed datasets
        └── *.html            # Project documentation
```

## Getting Started

### Prerequisites

- Python 3.7+
- Required Python packages:
  ```
  pip install pandas matplotlib seaborn numpy openpyxl
  ```

### Local Development

1. **Clone the repository:**
   ```bash
   git clone https://github.com/leemoradi/my_portfolio_site.git
   cd my_portfolio_site
   ```

2. **Start a local server:**
   ```bash
   python -m http.server 8000
   ```

3. **Open your browser and visit:**
   ```
   http://localhost:8000
   ```

## Featured Project: Voting Analysis

### Overview
I analyzed electoral data from Georgia and Texas to explore voting patterns, demographic correlations, and political trends across county-level data. This project combines my interests in political science with data analysis skills.

### Key Findings

- **Georgia 2020 Result:** Biden won with 49.5% vs Trump's 49.3% (0.2% margin)
- **Texas 2020 Result:** Trump won with 52.1% vs Biden's 46.9% (5.2% margin)
- **Most Competitive County:** Williamson County, TX (49.8% Biden vs 48.5% Trump)
- **County Analysis:** 89 Georgia counties vs 45 Texas counties

### What I Learned

- **Data Cleaning:** Working with messy Excel files and standardizing county-level data
- **Statistical Analysis:** Calculating vote percentages and finding correlations between demographics and voting patterns
- **Data Visualization:** Creating multiple chart types to tell different stories about the data
- **Web Development:** Building a portfolio to showcase my work
- **Geographic Analysis:** Understanding how county-level data reveals regional political dynamics

### Visualizations Created

The analysis produces several visualizations that tell different stories about the data:

1. **Vote Percentages by Candidate** - Shows how each county voted in 2020
2. **Income vs Biden Vote Correlation** - Explores the relationship between county wealth and Democratic voting
3. **Correlation Matrix** - Reveals statistical relationships between demographic and voting variables
4. **County Comparison Chart** - Side-by-side analysis of Georgia vs Texas counties
5. **County Vote Distributions** - Shows the spread of voting patterns across counties
6. **2020 Margin of Victory** - Visualizes how close each county's election was
7. **Actual 2020 Results** - Comprehensive county-level results with proper color coding

### Running the Analysis

1. **Navigate to the voting analysis directory:**
   ```bash
   cd projects/voting-analysis
   ```

2. **Generate all visualizations:**
   ```bash
   python generate_all_figures.py
   ```

3. **View the detailed analysis page:**
   Open `voting-analysis-project.html` in your browser

### Data Sources

- County-level voting data from official election results
- Demographic data including income and education statistics
- Geographic information for county mapping and analysis

## Technologies Used

- **Frontend:** HTML5, CSS3
- **Data Analysis:** Python, Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Data Processing:** Excel, CSV manipulation
- **Version Control:** Git

## Project Features

### Portfolio Website
- **Responsive Design:** Works well on mobile and desktop
- **Clean Design:** Simple, professional layout
- **Project Showcase:** Detailed descriptions and visualizations
- **Easy Navigation:** Simple menu structure

### Voting Analysis Project
- **Comprehensive Analysis:** Multiple angles on the same electoral data
- **Clear Visualizations:** Charts that tell different stories about the data
- **Statistical Insights:** Correlation analysis and demographic patterns
- **Geographic Context:** County-level analysis with mapping considerations

## Adding New Projects

1. Create a new directory in `projects/`
2. Add your project files and analysis scripts
3. Update `projects.html` with project overview
4. Create a detailed project page (optional)
5. Add any generated visualizations to the project directory

## About Me

I'm a rising junior at Tufts University majoring in Philosophy with minors in Political Science and History. My academic interests center on political theory, legal thought, and the intersection of philosophical ideas with current events. I'm especially drawn to questions about justice, rights, and power, and how they shape the legal and political systems we live under.

Outside of academics, I am passionate about activism, particularly around healthcare accessibility and reproductive justice. I am interested in how policy and philosophy intersect in these areas, and how lived experience informs both.

## Contact

- **Email:** leahjmoradi@gmail.com
- **School Email:** leah.moradi@tufts.edu
- **Phone:** (770) 820-8619
- **GitHub:** https://github.com/leemoradi
- **Portfolio:** https://leemoradi.github.io/my_portfolio_site/

---
