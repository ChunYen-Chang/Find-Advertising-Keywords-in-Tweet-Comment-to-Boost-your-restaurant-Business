# import packages which are needed
from pyspark.sql import SparkSession
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from textblob import TextBlob


# define a function
def convert_to_dataframe(rdd):
    print('here it goes')
    if not rdd.isEmpty():
        df = spark.createDataFrame(rdd, ['text', 'polarity', 'subjectivity'])
        df.write.format('jdbc').options(url="jdbc:mysql://ec2-18-236-88-41.us-west-2.compute.amazonaws.com:3306/restaurant",driver="com.mysql.jdbc.Driver",dbtable="streaming",user="remote",password="remotepw").mode('append').save()
    return rdd


# create a SparkSession and StreamingContext
spark = SparkSession \
.builder \
.config("spark.jars.packages", "org.apache.spark:spark-streaming-kafka-0-8_2.11:2.2.0") \
.getOrCreate()
ssc = StreamingContext(spark.sparkContext, 10)


# receive data from Kafka cluster
directKafkaStream = KafkaUtils.createDirectStream(ssc, ['restaurant'], {"metadata.broker.list": '54.213.235.62:9092'})


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
