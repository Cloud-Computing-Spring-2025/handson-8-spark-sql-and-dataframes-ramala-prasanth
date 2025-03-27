from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as _sum, desc

# Initialize Spark Session
spark = SparkSession.builder.appName("TopVerifiedUsers").getOrCreate()

# Load datasets
posts_df = spark.read.option("header", True).csv("/workspaces/handson-8-spark-sql-and-dataframes-ramala-prasanth/input/posts.csv", inferSchema=True)
users_df = spark.read.option("header", True).csv("/workspaces/handson-8-spark-sql-and-dataframes-ramala-prasanth/input/users.csv", inferSchema=True)

# Filter Verified Users
verified_users_df = users_df.filter(col("Verified") == True)

# Join datasets on UserID
verified_posts_df = posts_df.join(verified_users_df, "UserID")

# Calculate Total Reach (Likes + Retweets)
top_verified = (
    verified_posts_df.groupBy("Username")
    .agg(_sum(col("Likes") + col("Retweets")).alias("Total Reach"))
    .orderBy(desc("Total Reach"))
    .limit(5)
)

# Show the result
top_verified.show()

# Save result
top_verified.coalesce(1).write.mode("overwrite").csv("/workspaces/handson-8-spark-sql-and-dataframes-ramala-prasanth/outputs/top_verified_users.csv", header=True)

# Stop Spark Session
spark.stop()