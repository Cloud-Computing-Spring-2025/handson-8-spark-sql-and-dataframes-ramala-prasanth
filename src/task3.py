from pyspark.sql import SparkSession
from pyspark.sql.functions import when, avg, col, desc

# Initialize Spark Session
spark = SparkSession.builder.appName("SentimentVsEngagement").getOrCreate()

# Load posts data
posts_df = spark.read.option("header", True).csv("/workspaces/handson-8-spark-sql-and-dataframes-ramala-prasanth/input/posts.csv", inferSchema=True)

# Categorize Sentiment
posts_df = posts_df.withColumn(
    "Sentiment",
    when(col("SentimentScore") > 0.3, "Positive")
    .when((col("SentimentScore") >= -0.3) & (col("SentimentScore") <= 0.3), "Neutral")
    .otherwise("Negative")
)

# Calculate average likes and retweets per sentiment group
sentiment_stats = (
    posts_df.groupBy("Sentiment")
    .agg(avg("Likes").alias("Avg Likes"), avg("Retweets").alias("Avg Retweets"))
    .orderBy(desc("Avg Likes"))
)

# Show the result
sentiment_stats.show()

# Save result
sentiment_stats.coalesce(1).write.mode("overwrite").csv("/workspaces/handson-8-spark-sql-and-dataframes-ramala-prasanth/outputs/sentiment_engagement.csv", header=True)

# Stop Spark Session
spark.stop()