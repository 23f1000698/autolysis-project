# README.md

## Data Overview
The dataset contains **2,652 rows** and **8 columns** related to movies, detailing various characteristics such as the release date, language, type, title, contributors, and different ratings including overall, quality, and repeatability.

### Summary of Columns
- **date**: The release date of the movie.
- **language**: Language of the movie.
- **type**: Type of the content (e.g., movie).
- **title**: Title of the movie.
- **by**: Contributors (actors) involved in the movie.
- **overall**: Overall rating of the movie.
- **quality**: Quality rating of the movie.
- **repeatability**: How likely the movie is to be revisited.

### Missing Values
- **date**: 99 missing entries
- **by**: 262 missing entries

### Descriptive Statistics
- The dataset includes **11 unique languages** and **8 unique types** of content, with a predominance of Tamil and movies.
- Ratings suggest a mean overall rating of approximately **3.05** and a quality rating of **3.21**.

## Analysis Performed
The analysis focused on the following aspects:
- **Descriptive Statistics**: Summary statistics were generated to understand distribution and central tendencies of ratings across various attributes.
- **Correlation Analysis**: Examined relationships between overall ratings, quality ratings, and repeatability.
- **Clustering**: Identified patterns in data points, resulting in **3 clusters** based on observed similarities.
  
## Key Insights
1. **Rating Distribution**: The overall ratings are concentrated predominantly around the mid-range values (as shown in the distribution charts).
    ![Overall Distribution](media/overall_distribution.png)
  
2. **Correlation Findings**: There is a strong correlation (0.83) between overall ratings and quality ratings, suggesting movies rated high in quality are likely viewed positively overall.
   ![Correlation Heatmap](media/correlation_heatmap.png)
   
3. **Influential Contributors**: By analyzing the top contributors, insights can be drawn about personalities who repeatedly engage in high-rated films, which can drive marketing decisions. These relationships are depicted in the charts below.
   ![Top Contributors](media/by_top_categories.png)

4. **Cluster Analysis**: The clustering results point towards distinct group behaviors among movie ratings, indicating varying audience segments with different preferences.
   ![Clusters](media/clusters.png)

5. **Genre Insights**: The top movie titles indicate which genres or types are more frequently reviewed and rated, informing production strategies.
   ![Top Titles by Category](media/title_top_categories.png)

## Implications
- **Marketing Strategies**: Understanding the correlation between ratings can help marketers align campaigns focused on quality-driven narratives.
- **Content Development**: Insight into the preferred languages and types suggests a strategic focus on content creation that resonates with high-rating contributors will likely lead to increased viewer ratings.
- **Audience Segmentation**: The clustering results facilitate targeted marketing based on audience preferences, helping distributors tailor their delivery strategies for segmented groups.

In sum, leveraging analysis on ratings, quality, and contributor insights can effectively guide decisions on film production and marketing strategies, ensuring alignment with audience expectations and preferences.