# Book Analysis Report

## Data Overview

This analysis is based on a dataset comprising **10,000 rows** and **23 columns** pertaining to various books. Key columns include:
- `book_id`
- `authors`
- `average_rating`
- `ratings_count`
- `work_ratings_count`
- `original_publication_year`

### Missing Values Summary
The dataset has missing values in several columns:
- `isbn`: 700 missing
- `isbn13`: 585 missing
- `original_publication_year`: 21 missing
- `original_title`: 585 missing
- `language_code`: 1084 missing

### Descriptive Statistics
- Average rating across the dataset: **4.00**
- Average ratings count: **54,001**
- Distribution of ratings demonstrates clear engagement from users, with the highest number of 5-star ratings.

## Analysis Performed

1. **Descriptive Analysis**: Summary statistics were used to understand the dataset's central tendencies and dispersions.
  
2. **Correlation Analysis**: Investigated relationships between numeric variables to identify significant correlations.

3. **Clustering**: Implemented clustering algorithms to categorize books into distinct groups based on ratings and publication year.

4. **Visualization**: Generated visual representations (heatmaps, histograms) to better comprehend distributions and correlations.

### Correlation Matrix
![Correlation Heatmap](goodreads/correlation_heatmap.png)

### Book ID Distribution
![Book ID Distribution](goodreads/book_id_distribution.png)

### Clustering Results
![Clusters](goodreads/clusters.png)

## Key Insights

1. **Rating Trends**: A negative correlation was found between `ratings_count` and `average_rating`, suggesting that as the number of ratings increases, the average rating tends to decrease slightly.

2. **Clusters of Books**: The dataset was segmented into three clusters:
   - **Cluster 0** (Large): **7,193 books**, generally lower-rated.
   - **Cluster 1** (Small): **82 books**, high ratings but very few ratings.
   - **Cluster 2** (Medium): **2,122 books**, moderate ratings.

3. **Publication Year Analysis**: Most popular books are published around the years **2000 - 2015**, indicating a potential preference for newer literature.

4. **ISBN Counts**: The analysis revealed that common ISBNs correlate with higher engagement, showing that these books have gained popularity over time.

## Implications

- **For Publishers**: Focus should be directed to developing content similar to highly rated, more recent publications, as they attract higher engagement.
  
- **For Author Marketing**: Authors or publishers can leverage trending publication years to strategize marketing campaigns directed at current readers’ preferences.

- **For Readers**: The distribution trends can guide readers in selecting popular novels that align with community ratings.

- **For Data Enrichment**: The presence of missing data indicates areas for improvement, such as the need to enrich author and publication data to enhance analysis quality.

### Conclusion
The findings from this dataset present actionable strategies for authors, publishers, and marketers to align their offerings with current literary trends and reader preferences while addressing the missing data points that could enhance this analysis further.

![Top Categories by Title](goodreads/title_top_categories.png)
![Top Categories by ISBN](goodreads/isbn_top_categories.png)