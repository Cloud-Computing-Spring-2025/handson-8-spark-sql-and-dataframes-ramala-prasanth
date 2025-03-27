from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, col, desc

# Initialize Spark Session
spark = SparkSession.builder.appName("HashtagTrends").getOrCreate()

# Load posts data
posts_df = spark.read.option("header", True).csv("/workspaces/handson-8-spark-sql-and-dataframes-ramala-prasanth/input/posts.csv")

# Split the Hashtags column into individual hashtags
hashtags_df = posts_df.withColumn("Hashtag", explode(split(col("Hashtags"), ",")))

# Count the frequency of each hashtag
hashtag_counts = hashtags_df.groupBy("Hashtag").count().orderBy(desc("count"))

# Get the top 10 hashtags
top_hashtags = hashtag_counts.limit(10)

# Show the result
top_hashtags.show()

# Save result
top_hashtags.coalesce(1).write.mode("overwrite").csv("/workspaces/handson-8-spark-sql-and-dataframes-ramala-prasanth/outputs/hashtag_trends.csv", header=True)

# Stop Spark Session
spark.stop()