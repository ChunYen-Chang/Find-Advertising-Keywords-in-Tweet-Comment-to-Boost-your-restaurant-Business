<p align="center">
  <img width="1100" height="300" src="https://github.com/ChunYen-Chang/Personalized-restaurant-RESTfulAPI-Using-Kafka-and-Spark/blob/master/image/project_logo.jpg">
</p>
  
  
# Finding Keywords in Tweet Comment to Boost your restaurant Business-Using Kafka and Spark Streaming

#### *PROJECT BACKGROUND and DESCRIPTION*
Suppose that you are a manager of one restaurant and you are eager for finding a way to attract more customers, what will you do? I believe the 
first idea comes to your mind is posting advertisements on some online forums such as Facebook, Twitter, or Plurk. However, it is hard to find 
what kind of text content you sould put in your advertisement to catch people's eyes to make them have the motivation to go to your restaurant. 
If you are struggling with this issue, this project might be helpful for you. Generally speaking, this project will collect a lot of restaurant comments 
from Twitter, separate these comments into good comments and bad comments, and save these good and bad comments in a table in a database. 
After creating the table in a database, the restaurant manager can conduct much deeper analysis such as NLP to find what kind of word is frequently 
used in good comments and which word is usually used in bad comment. Then, when this restaurant manager tries to write down the restaurant advertisement 
content , he knows which word sould be used (the word coming from good comments) and which word should avoid to use (the word from bad comments).


#### *SYSTEM ARCHITECTURE*

<p align="center">
  <img width="700" height="800" src="https://github.com/ChunYen-Chang/Personalized-restaurant-RESTfulAPI-Using-Kafka-and-Spark/blob/master/image/system_architecture.jpeg">
</p>

In this project, we choose to play around with the Twitter Streaming data. In order to harness the streaming data from Twitter, this project decides to use the
combinaton of Kafka and Spark. Kafka is a message broker which can accommodate a great amount of data which comes in a short period of time and allow other system 
to extract data from it. Spark is an analytical engie for great amount of data. Thus, by combing these two, we can create a system which can accommodata the great 
amount streaming data and process this data in a real-time manner.  

OK, so let us walk throught the whole system. In the beginning, we create three AWS EC2 instances to receive the data from Twitter APIs and 
send all this data to Kafka cluster. After the Kafka cluster receives the data, it will store all data in one topic--"restaurant topic" 
and wait for other consumers to consume the data. Then, the AWS EMR cluster (Spark cluster) will send the message to the Kafka broker to 
ask the kafka cluster send the data stored in "restaurant topic". The Spark cluster receives the data, has data wrangling processes, conducts 
a basic sentiment analysis on the data(restaurant's comments), seperates data into two categories(good restaurant comments and bad restaurant 
commnets) based on the previous sentiment analysis, and store these two categories into a table in a database. After this, we create 
a RESTful API by using flask for users (which might be restaurant managers), users can use the HTTP request to interact with the server and get
the restaurant comments' data.  

Hmm, it is really simple. is it? Before we move to next sections, we want to answer some question as we know that you might have these questions.  
1. **WHY WE HAVE THREE EC2 INSTANCES:**  
The reason why we use three EC2 instances is that Twitter has a **restriction** on how many tweets one free account can receive at a certain period of time. 
To put it in simple, we cannot extract a lot of data in a certain period of time. To overcome this restriction, we set up three Twitter accounts and fetch 
the data at the same time. By doing this, we think it can help us to extract more data at a certain period of time.  

2. **WHY WE USE MySql:**  
Some people might have the concern. Since we collect the streaming data from Twitter, it is not a good idea to store the streaming data in MySql database 
because the MySql database may not have the ability to accommodata all data. However, according to our test, the Twitter post which contains restaurant 
comments is rare. It is possible we only get five comments in 10 mins time period. Under this situation, it is not necessart to consider the problem that 
MySql cannot accommodate the data.  

3. **WHY WE USE RESTful APIs:**  
The reason is simple. We don't want our end-users have the right to directly access to the database as the database safety concern. Thus, we 
decide to provide a RESTful API for them and only allow them to use that channel to extract data from the database.  

------------
#### SOFTWATE VERSION IN THIS PROJECT
1. **KafKa version:** kafka_2.11-2.3.0
2. **Spark version:** Spark 2.4.4
3. **Hadoop version:** Hadoop 2.8.5
4. **MySql version:** MySql 5.7
5. **Ubuntu version for EC2 instance:** Ubuntu Server 16.04 LTS (HVM)
7. **.jar file for Spark cluster:**  
    1. spark-streaming-kafka-0-8-assembly_2.11-2.2.0.jar.  
It can download from https://repo1.maven.org/maven2/org/apache/spark/spark-streaming-kafka-0-8-assembly_2.11/2.2.0/spark-streaming-kafka-0-8-assembly_2.11-2.2.0.jar
    2. mysql-connector-java-8.0.17.jar  
It can download from https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-8.0.17.zip
------------
#### FILES IN THE REPOSITORY
- **image folder**: It contains images which are used in this repository  

- **Amazon_EMR_setting_instruction folder**: This folder has two files. EMR_CONFIGURATION_GUIDE.md is the documentation which tells you how to build an EMR 
cluster for this project. emr_other_packages.sh is the file which you will need when you build an EMR cluster for this project. You can check the EMR_CONFIGURATION_GUIDE.md 
to understand how to use emr_other_packages.sh  

- **kafka_installation folder**: This folder contains one file--KAFKA_INSTALLATION_GUIDE.md. This file details how to launch AWS EC2 instances and how to configure a Kafka 
cluster in these EC2 instances.  

- **code/streaming_part folder**: This folder has all programing code in streaming part. It has three files. streaming_from_twitter_to_kafka.py is about 
how to transfer data from Twitter to Kafka cluster. streaming_from_kafka_to_sprak_to_mysql.py relates to the code of how to move 
streaming data from Kafka cluster to Spark cluster, conduct data wrangling in Spark, and save data in MySql database. tweet_api.txt is the file 
including the account information of accessing to Twitter API. You can check this photo to see the which part these codes is corresponding to.  
<p align="center">
  <img width="700" height="600" src="https://github.com/ChunYen-Chang/Personalized-restaurant-RESTfulAPI-Using-Kafka-and-Spark/blob/master/image/system_architecture_upper.jpg">
</p>  

- **code/flaskserver_part folder**: This folder collects all code relating to RESTful APIs. It includes two files. model.py is about creating 
table in MySql database. server.py is about building a RESTful API in AWS EC2 instance. Again, please check the below photo to see which system 
architecture part is corresponding to.  
<p align="center">
  <img width="700" height="600" src="https://github.com/ChunYen-Chang/Personalized-restaurant-RESTfulAPI-Using-Kafka-and-Spark/blob/master/image/system_architecture_lower.jpg">
</p>  

- **README.md**: It includes the project background, project description, system architecture, and the information about how to run the project.  

------------
#### HOW TO RUN THE PROJECT
In order to run this project, you need to finish five steps. The first step is launching AWS EC2 instances. The second step is creating 
a kafka cluster based on the AWS EC2 instances you created in the first step. The Third step is building an AWS EMR cluster. The fourth 
step is build a RESTful API on the AWS EC2 instances you created in the first step. The fifth step is creating three TweetInf extraction 
server.

**STEP ONE: lAUNCH AWS EC2 INSTANCES**  
1. launch three AWS EC2 instances for the Kafka cluster.  
2. launch three AWS EC2 instances for the TweetInf extraction servers.  
3. launch one AWS EC2 instance for the RESTful API.  
   
**PART TWO: CREATE A KAFKA CLUSTER**  
1. For this part, please check the instruction documentation in *kafka_installation folder*  
2. After you have a Kafka cluster and make sure this Kafka cluster can work properly, please type `kafka_2.12-2.3.0/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 2 --partitions 3 --topic restaurant` 
to create a restaurant topic in the Kafka cluster.

**PART THREE: BUILD A EMR CLUSTER**  
1. For this part, please check the instruction documentation in *Amazon_EMR_setting_instruction folder*  
2. After creating the AWS EMR cluster, please access to the master node in this cluster.
3. Copy **streaming folder** to this EC2 instance  
4. Type `spark-submit --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.2.0 --jars /usr/lib/spark/jars/spark-streaming-kafka-0-8-assembly_2.11-2.2.0.jar,/home/hadoop/mysql-connector-java-8.0.17.jar streaming_from_kafka_to_sprak_to_mysql.py` in your terminal to start the process of extracting data from Kafka custer 
, have data wrangling process, and store result in a MySql database.


**PART FOUR: BUILD A RESTful API**  
1. Access to the EC2 instance.  
2. Install the MySql database
3. Copy the code in "code/flaskserver_part folder"  
4. Type `sudo python3 server.py` in your terminal to start the Falsk Web server  


**PART FIFTH: BUILD TWEETING EXTRACTION SERVER**  
1. Access to the EC2 instance.  
2. Copy the code in "code/streaming_part folder"  
3. Type `sudo python3 streaming_from_twitter_to_kafka.py` in your terminal to start the process of extracting data from Twitter API 

**FINAL**
Congraduation! You already finish all the necessary steps to operate this project. If you check your AWS EC2 dashboard, you may have 
the similiar result as in the below picture. Then, you can play with the streaming data with by using Kafka and Spark streaming. Enjoy it!  
<p align="center">
  <img width="1000" height="600" src="https://github.com/ChunYen-Chang/Personalized-restaurant-RESTfulAPI-Using-Kafka-and-Spark/blob/master/image/AWS_EC2_instance.png">
</p>
