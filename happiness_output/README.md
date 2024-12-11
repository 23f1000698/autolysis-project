# README.md

## Data Overview

The dataset consists of 2,363 rows and 11 columns, providing insights into the life satisfaction and wellbeing of individuals across 165 countries from the years 2005 to 2023. The following key columns are included:

- **Country name**: The name of the country.
- **Year**: The year of data collection.
- **Life Ladder**: A metric representing life satisfaction.
- **Log GDP per capita**: A measurement of economic wellbeing.
- **Social support**: Level of perceived support from family and friends.
- **Healthy life expectancy at birth**: The average number of years a newborn is expected to live in good health.
- **Freedom to make life choices**: A measure of personal autonomy.
- **Generosity**: A measure reflecting societal generosity.
- **Perceptions of corruption**: Levels of perceived corruption in the government.
- **Positive affect** and **Negative affect**: Indicators of emotional experiences.

### Missing Values

The dataset contains various missing values, particularly in the **Generosity** column (81 missing values) and **Perceptions of corruption** (125 missing values).

## Analysis Performed

The analysis involved several steps:
1. **Descriptive Statistics**: Summary statistics were computed to understand the distribution of the data, including means, standard deviations, and ranges for critical columns.
2. **Correlation Analysis**: Correlations between different variables were investigated to identify potential relationships.
3. **Clustering**: The data was segmented into three clusters based on correlated features to identify groups with similar life satisfaction characteristics.
4. **Visualization**: Key insights were illustrated using graphics, including a correlation heatmap, distribution of years, clustering outcomes, and top categories per country.

## Key Insights

- **Correlation Highlights**: 
  - The **Life Ladder** correlates highly with **Log GDP per capita** (0.78) and **Social support** (0.72), suggesting that economic factors and social networks significantly influence life satisfaction.
  - **Perceptions of corruption** negatively correlate with **Life Ladder** (-0.43), indicating that higher corruption perception results in lower life satisfaction.

- **Cluster Analysis**: 
  - The data revealed three distinct clusters based on characteristics such as GDP, life satisfaction levels, and social support. The largest cluster, containing 982 entries, likely includes countries with moderate life satisfaction and GDP.

- **Trends Over Time**: 
  - Life satisfaction has varied across the years, which is depicted in the distribution chart, showing fluctuations likely corresponding to global events and economic changes.

![Correlation Heatmap](happiness_output/correlation_heatmap.png)  
*Figure 1: Correlation heatmap illustrating relationships between key variables*

![Year Distribution](happiness_output/year_distribution.png)  
*Figure 2: Distribution of data over the years*

![Clusters](happiness_output/clusters.png)  
*Figure 3: Clustering of countries based on wellbeing metrics*

![Top Categories](happiness_output/Country name_top_categories.png)  
*Figure 4: Top categories for life satisfaction across different countries*

## Implications

The results of this analysis indicate that:
- **Policy Focus on GDP and Social Support**: Countries registered with lower life satisfaction should consider enhancing economic policies and social support structures to improve overall wellbeing.
- **Address Perceptions of Corruption**: Tackling corruption could directly improve the happiness index in countries with high levels of perceived corruption.
- **Targeted Interventions**: Development programs focused on the most dissatisfied clusters could lead to effective interventions tailored to the unique needs of these populations.

By leveraging these insights, governments and organizations can design more effective strategies to enhance quality of life and satisfaction for their citizens.