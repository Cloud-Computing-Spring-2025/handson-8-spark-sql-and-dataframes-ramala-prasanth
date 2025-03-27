# handson-08-sparkSQL-dataframes-social-media-sentiment-analysis

## **Prerequisites**

Before starting the assignment, ensure you have the following software installed and properly configured on your machine:

1. **Python 3.x**:
   - [Download and Install Python](https://www.python.org/downloads/)
   - Verify installation:
     ```bash
     python3 --version
     ```

2. **PySpark**:
   - Install using `pip`:
     ```bash
     pip install pyspark
     ```

3. **Apache Spark**:
   - Ensure Spark is installed. You can download it from the [Apache Spark Downloads](https://spark.apache.org/downloads.html) page.
   - Verify installation by running:
     ```bash
     spark-submit --version
     ```

4. **Docker & Docker Compose** (Optional):
   - If you prefer using Docker for setting up Spark, ensure Docker and Docker Compose are installed.
   - [Docker Installation Guide](https://docs.docker.com/get-docker/)
   - [Docker Compose Installation Guide](https://docs.docker.com/compose/install/)

## **Setup Instructions**

### **1. Project Structure**

Ensure your project directory follows the structure below:

```
SocialMediaSentimentAnalysis/
├── input/
│   ├── posts.csv
│   └── users.csv
├── outputs/
│   ├── hashtag_trends.csv
│   ├── engagement_by_age.csv
│   ├── sentiment_engagement.csv
│   └── top_verified_users.csv
├── src/
│   ├── task1_hashtag_trends.py
│   ├── task2_engagement_by_age.py
│   ├── task3_sentiment_vs_engagement.py
│   └── task4_top_verified_users.py
├── docker-compose.yml
└── README.md
```



- **input/**: Contains the input datasets (`posts.csv` and `users.csv`)  
- **outputs/**: Directory where the results of each task will be saved.
- **src/**: Contains the individual Python scripts for each task.
- **docker-compose.yml**: Docker Compose configuration file to set up Spark.
- **README.md**: Assignment instructions and guidelines.



---

# Note
To generate the dataset execute `sudo python input_generator.py` in order for the system to overwrite the permissions.

---

### **2. Running the Analysis Tasks**

You can run the analysis tasks either locally or using Docker.

#### **a. Running Locally**

1. **Navigate to the Project Directory**:
   ```bash
   cd SocialMediaSentimentAnalysis/
   ```

2. **Execute Each Task Using `spark-submit`**:
   ```bash
 
     spark-submit src/task1_hashtag_trends.py
     spark-submit src/task2_engagement_by_age.py
     spark-submit src/task3_sentiment_vs_engagement.py
     spark-submit src/task4_top_verified_users.py
     
   ```

3. **Verify the Outputs**:
   Check the `outputs/` directory for the resulting files:
   ```bash
   ls outputs/
   ```


## **Overview**

In this assignment, you will leverage Spark Structured APIs to analyze a dataset containing employee information from various departments within an organization. Your goal is to extract meaningful insights related to employee satisfaction, engagement, concerns, and job titles. This exercise is designed to enhance your data manipulation and analytical skills using Spark's powerful APIs.

## **Objectives**

By the end of this assignment, you should be able to:

1. **Data Loading and Preparation**: Import and preprocess data using Spark Structured APIs.
2. **Data Analysis**: Perform complex queries and transformations to address specific business questions.
3. **Insight Generation**: Derive actionable insights from the analyzed data.


# Dataset Generation Script

## Overview
This script generates two CSV files, `users.csv` and `posts.csv`, in the `input/` directory. These datasets are designed for social media analytics, allowing analysis of user engagement, sentiment trends, and hashtag popularity.

## Files Generated
### 1. `users.csv`
Contains details about users, including their age group, country, and verification status.

**Columns:**
- `UserID` (Integer): Unique identifier for each user.
- `Username` (String): Social media handle.
- `AgeGroup` (String): User's age category (`Teen`, `Adult`, `Senior`).
- `Country` (String): Country of the user.
- `Verified` (Boolean): Whether the user is verified (`True` or `False`).

### 2. `posts.csv`
Contains details of user posts, including engagement metrics and sentiment scores.

**Columns:**
- `PostID` (Integer): Unique identifier for each post.
- `UserID` (Integer): ID linking the post to a user in `users.csv`.
- `Content` (String): The text content of the post.
- `Timestamp` (Datetime): When the post was made.
- `Likes` (Integer): Number of likes on the post.
- `Retweets` (Integer): Number of retweets/shares.
- `Hashtags` (String): Comma-separated hashtags used in the post.
- `SentimentScore` (Float): Sentiment analysis score (-1 to 1), where positive values indicate positive sentiment, and negative values indicate negative sentiment.

## Data Generation
- **User data:** 10 randomly generated users with varied age groups, countries, and verification statuses.
- **Post data:** 100 randomly generated posts, each associated with a user. Each post includes engagement metrics, hashtags, and sentiment scores.
- **Hashtags and content:** Randomly selected from predefined lists to simulate real-world diversity in social media posts.
- **Engagement metrics:** Likes and retweets are assigned random values to represent varying levels of popularity.
- **Sentiment scores:** Random float values between -1 and 1 are assigned to posts to analyze sentiment trends.

## Usage
1. Run the script to generate the datasets:
   ```bash
   python generate_dataset.py
   ```
2. The generated CSV files will be stored in the `input/` directory.
3. Use these datasets for data analysis tasks such as:
   - Identifying trending hashtags
   - Measuring engagement by age group
   - Exploring sentiment impact on user interactions
   - Finding top influencers based on engagement

## Output Example
### Sample `users.csv`
| UserID | Username     | AgeGroup | Country | Verified |
|--------|------------|----------|---------|----------|
| 1      | @techie42  | Adult    | US      | True     |
| 2      | @critic99  | Senior   | UK      | False    |
| 3      | @daily_vibes | Teen   | India   | False    |

### Sample `posts.csv`
| PostID | UserID | Content                     | Timestamp           | Likes | Retweets | Hashtags       | SentimentScore |
|--------|--------|----------------------------|---------------------|-------|----------|---------------|---------------|
| 101    | 1      | Loving the new update!     | 2023-10-05 14:20:00 | 120   | 45       | #tech,#AI     | 0.8           |
| 102    | 2      | This app keeps crashing.  | 2023-10-05 15:00:00 | 5     | 1        | #fail         | -0.7          |
| 103    | 3      | Just another day...        | 2023-10-05 16:30:00 | 15    | 3        | #mood         | 0.0           |

## Notes
- Ensure that at least 100 records are generated for meaningful analysis.
- The dataset structure is designed for easy integration with Apache Spark-based analysis workflows.



## **Assignment Tasks**

You are required to complete the following three analysis tasks using Spark Structured APIs. Ensure that your analysis is well-documented, with clear explanations and any relevant visualizations or summaries.

### **1. Hashtag Trends **

**Objective:**

Identify trending hashtags by analyzing their frequency of use across all posts.

**Tasks:**

- **Extract Hashtags**: Split the `Hashtags` column and flatten it into individual hashtag entries.
- **Count Frequency**: Count how often each hashtag appears.
- **Find Top Hashtags**: Identify the top 10 most frequently used hashtags.


**Expected Outcome:**  
A ranked list of the most-used hashtags and their frequencies.

**Example Output:**

| Hashtag     | Count |
|-------------|-------|
| #tech       | 120   |
| #mood       | 98    |
| #design     | 85    |

---

### **2. Engagement by Age Group**

**Objective:**  
Understand how users from different age groups engage with content based on likes and retweets.

**Tasks:**

- **Join Datasets**: Combine `posts.csv` and `users.csv` using `UserID`.
- **Group by AgeGroup**: Calculate average likes and retweets for each age group.
- **Rank Groups**: Sort the results to highlight the most engaged age group.

**Expected Outcome:**  
A summary of user engagement behavior categorized by age group.

**Example Output:**

| Age Group | Avg Likes | Avg Retweets |
|-----------|-----------|--------------|
| Adult     | 67.3      | 25.2         |
| Teen      | 22.0      | 5.6          |
| Senior    | 9.2       | 1.3          |

---

### **3. Sentiment vs Engagement**

**Objective:**  
Evaluate how sentiment (positive, neutral, or negative) influences post engagement.

**Tasks:**

- **Categorize Posts**: Group posts into Positive (`>0.3`), Neutral (`-0.3 to 0.3`), and Negative (`< -0.3`) sentiment groups.
- **Analyze Engagement**: Calculate average likes and retweets per sentiment category.

**Expected Outcome:**  
Insights into whether happier or angrier posts get more attention.

**Example Output:**

| Sentiment | Avg Likes | Avg Retweets |
|-----------|-----------|--------------|
| Positive  | 85.6      | 32.3         |
| Neutral   | 27.1      | 10.4         |
| Negative  | 13.6      | 4.7          |

---

### **4. Top Verified Users by Reach**

**Objective:**  
Find the most influential verified users based on their post reach (likes + retweets).

**Tasks:**

- **Filter Verified Users**: Use `Verified = True` from `users.csv`.
- **Calculate Reach**: Sum likes and retweets for each user.
- **Rank Users**: Return top 5 verified users with highest total reach.

**Expected Outcome:**  
A leaderboard of verified users based on audience engagement.

**Example Output:**

| Username       | Total Reach |
|----------------|-------------|
| @techie42      | 1650        |
| @designer_dan  | 1320        |

---

## **Grading Criteria**

| Task                        | Marks |
|-----------------------------|-------|
| Hashtag Trend Analysis      | 1     |
| Engagement by Age Group     | 1     |
| Sentiment vs Engagement     | 1     |
| Top Verified Users by Reach | 1     |
| **Total**                   | **1** |

---

## 📬 Submission Checklist

- [✅] PySpark scripts in the `src/` directory  
- [✅] Output files in the `outputs/` directory  
- [✅] Datasets in the `input/` directory  
- [✅] Completed `README.md`  
- [✅] Commit everything to GitHub Classroom  
- [✅] Submit your GitHub repo link on canvas

---


