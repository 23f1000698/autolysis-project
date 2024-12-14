# README.md

## Data Overview

The dataset consists of **2,652 rows** and **8 columns** that provide information about various entries, including movies, their ratings, and review authors. Here are the key summary details:

- **Columns** include: `date`, `language`, `type`, `title`, `by`, `overall`, `quality`, `repeatability`.
- **Missing Values**: There are **99 missing dates** and **262 missing authors**.
- The **overall** rating's mean is approximately **3.05** with a standard deviation of **0.76**.
- The **quality** rating's mean is approximately **3.21**, while for **repeatability**, the mean is roughly **1.49**.
- **Sample of Recent Entries**:
    - "Meiyazhagan" - 4 Overall, 5 Quality, by Arvind Swamy, Karthi
    - "Vettaiyan" - 2 Overall, 2 Quality, by Rajnikanth, Fahad Fazil
    - "Amaran" - 4 Overall, 4 Quality, by Siva Karthikeyan, Sai Pallavi

## Analysis Performed

1. **Descriptive Statistics**: Basic stats were computed, revealing unique counts and distributions.
2. **Correlation Analysis**: Determined relationships between the `overall`, `quality`, and `repeatability` ratings.
3. **Clustering Analysis**: Implemented clustering to identify potential groups within the data based on ratings.

## Key Insights

- **Correlation**: High correlation observed between `overall` and `quality` ratings (0.83), suggesting films rated higher generally provide better quality experiences.
- **Cluster Breakdown**:
    - **Cluster 1 (1,395 entries)**: Represents a substantial group likely with average ratings.
    - **Cluster 2 (1,091 entries)**: Slightly fewer high-rated titles, indicating a moderate level of quality.
    - **Cluster 0 (166 entries)**: May represent lower-rated films needing attention for quality improvement.
    
  ![Correlation Heatmap](media_output/correlation_heatmap.png)
  
- **Overall Ratings Distribution**: The distribution shows the concentration of ratings around the 3-4 mark, indicating a tendency toward average to good ratings.
  
  ![Overall Distribution](media_output/overall_distribution.png)

## Implications

- **Quality Improvement Strategy**: Focus on films in Cluster 0 for enhancements in content and production quality, possibly utilizing insights from the higher-rated clusters.
- **Market Trends in Ratings**: The popularity of English and Tamil films suggests targeting these languages for future content development, as they appear to dominate the dataset.
  
  ![Top Categories by Title](media_output/title_top_categories.png)
  
  ![Top Categories by Author](media_output/by_top_categories.png)

- **User Engagement Initiatives**: Enhancing interactions with reviewers could fill gaps for entries with missing authors and boost engagement through community-building practices.

![Clusters](media_output/clusters.png) 

In summary, leveraging these insights will provide pathways to enhancing film quality and viewer satisfaction significantly as well as inform marketing strategies around language and film type.