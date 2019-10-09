# import packages which are needed
from pyspark.sql import SparkSession
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from textblob import TextBlob


# define a function
def convert_to_dataframe(rdd):
    if not rdd.isEmpty():
        df = spark.createDataFrame(rdd, ['text', 'polarity', 'subjectivity'])
        df.write.format('jdbc').options(url="jdbc:mysql://<your mysql db IP>:<your mysql db port>/<db name>",driver="com.mysql.jdbc.Driver",dbtable="<db table name>",user="<db account>",password="<db password>").mode('append').save()
    return rdd


# create a SparkSession and StreamingContext
spark = SparkSession \
.builder \
.config("spark.jars.packages", "org.apache.spark:spark-streaming-kafka-0-8_2.11:2.2.0") \
.getOrCreate()
ssc = StreamingContext(spark.sparkContext, 10)


# receive data from Kafka cluster
directKafkaStream = KafkaUtils.createDirectStream(ssc, ['restaurant'], {"metadata.broker.list": '<your kafka cluster IP>:<your kafka cluster port>'})


# Data wrangling process by using RDD
lines = directKafkaStream.map(lambda x: x[1])
sentiment_analysis = lines.map(lambda x: (x, TextBlob(x)))
sentiment_analysis_result = sentiment_analysis.map(lambda x: (x[0].encode('utf-8'), x[1].sentiment.polarity, x[1].subjectivity))
sentiment_analysis_result.foreachRDD(lambda x: convert_to_dataframe(x))


# print the result on console
sentiment_analysis_result.pprint()


# start the streaming process
ssc.start()
ssc.awaitTermination()
