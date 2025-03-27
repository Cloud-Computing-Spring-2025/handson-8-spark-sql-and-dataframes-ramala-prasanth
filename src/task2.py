from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, col, desc

# Initialize Spark Session
spark = SparkSession.builder.appName("EngagementByAgeGroup").getOrCreate()

# Load datasets
posts_df = spark.read.option("header", True).csv("/workspaces/handson-8-spark-sql-and-dataframes-ramala-prasanth/input/posts.csv", inferSchema=True)
users_df = spark.read.option("header", True).csv("/workspaces/handson-8-spark-sql-and-dataframes-ramala-prasanth/input/users.csv", inferSchema=True)

# Join datasets on UserID
joined_df = posts_df.join(users_df, "UserID")

# Calculate average likes and retweets per age group
engagement_df = (
    joined_df.groupBy("AgeGroup")
    .agg(avg("Likes").alias("Avg Likes"), avg("Retweets").alias("Avg Retweets"))
    .orderBy(desc("Avg Likes"))
)

# Show the result
engagement_df.show()

# Save result
engagement_df.coalesce(1).write.mode("overwrite").csv("/workspaces/handson-8-spark-sql-and-dataframes-ramala-prasanth/outputs/engagement_by_age.csv", header=True)

# Stop Spark Session
spark.stop()
