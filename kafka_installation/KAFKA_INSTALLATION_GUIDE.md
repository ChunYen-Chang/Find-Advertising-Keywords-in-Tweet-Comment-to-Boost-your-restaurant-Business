# How to configure a Kafka cluster (with 3 brokers) in Amazon EC2 instances
This documentation shows how to build a Kafka cluster with three beokers in Amazon EC2 instances and it can be seperated into three parts. The detail of each part is listed below.
1. **PART ONE :** Amazon EC2 instance configuration
2. **PART TWO :** Install Apache Zookeeper
3. **PART THREE :** Install Apache Kafka
4. **PART FOUR :** Quick testing
-----
#### *PART ONE - Amazon EC2 instance configuration*
**Step1:** Launch three Amazon EC2 instance.
<p align="center">
  <img width="800" height="450" src="https://github.com/ChunYen-Chang/Personalized-restaurant-RESTfulAPI-Using-Kafka-and-Spark/blob/master/image/kaf_install_1.png">
</p>  
  
**Step2:** Configure the EC2 security group setting so that the zookeeper and Kafka program in each EC2 instance can communicate with each other. (In this part, please access to the security group inbound rule setting, open port 2888, port 3888, port 2181, port 9202. And, for each port, assign the IP address which has the right to access to the instance) 
<p align="center">
  <img width="800" height="450" src="https://github.com/ChunYen-Chang/Personalized-restaurant-RESTfulAPI-Using-Kafka-and-Spark/blob/master/image/kaf_install_1_1.png">
</p>  
  
-----
#### *PART TWO - Install Apache Zookeeper*
**Step1:** Access to your Amazon EC2 instance
<p align="center">
  <img width="800" height="450" src="https://github.com/ChunYen-Chang/Personalized-restaurant-RESTfulAPI-Using-Kafka-and-Spark/blob/master/image/kaf_install_2.png">
</p>  

**Step2:** Run apt-get update command
<p align="center">
  <img width="800" height="450" src="https://github.com/ChunYen-Chang/Personalized-restaurant-RESTfulAPI-Using-Kafka-and-Spark/blob/master/image/kaf_install_3.png">
</p>  

**Step3:** Get Kafka installation relating files from internet
<p align="center">
  <img width="800" height="450" src="https://github.com/ChunYen-Chang/Personalized-restaurant-RESTfulAPI-Using-Kafka-and-Spark/blob/master/image/kaf_install_4.png">
</p>  

**Step4:** Unzip the Kafka installation files
<p align="center">
  <img width="800" height="450" src="https://github.com/ChunYen-Chang/Personalized-restaurant-RESTfulAPI-Using-Kafka-and-Spark/blob/master/image/kaf_install_5.png">
</p>  

**Step5:** Create a directory at path--"/var/lib/zookeeper" 
<p align="center">
  <img width="800" height="450" src="https://github.com/ChunYen-Chang/Personalized-restaurant-RESTfulAPI-Using-Kafka-and-Spark/blob/master/image/kaf_install_6.png">
</p>  

**Step6:** Create a file which is called myid(at /var/lib/zookeeper). After creating this file, use vi command to write some information in this file. If this Amazon instance is node 1 in Zookeeper cluster, write 1 in this file. If this Amazon instance is node 2 in Zookeeper cluster, write 2 in this file. If this Amazon instance is node 3 in Zookeeper cluster, write 3 in this file.
<p align="center">
  <img width="800" height="450" src="https://github.com/ChunYen-Chang/Personalized-restaurant-RESTfulAPI-Using-Kafka-and-Spark/blob/master/image/kaf_install_7.png">
</p>  

**Step7:** Configure zookeeper.properties file. Please make sure you modify this file at each EC2 instance  
<p align="center">
  <img width="800" height="350" src="https://github.com/ChunYen-Chang/Personalized-restaurant-RESTfulAPI-Using-Kafka-and-Spark/blob/master/image/kaf_install_8.png">
</p>  

```
----------------------------------------------- 
# The setting for node 1
    dataDir=/var/lib/zookeeper  
    clientPort=2181  
    maxClientCnxns=0  
    initLimit=5  
    syncLimit=2  
    tickTime=2000
    
    # server ip list
    server.1=0.0.0.0:2888:3888  
    server.2=<Ip of second server>:2888:3888  
    server.3=<ip of third server>:2888:3888  
-----------------------------------------------    
# The setting for node 2
    dataDir=/var/lib/zookeeper  
    clientPort=2181  
    maxClientCnxns=0  
    initLimit=5  
    syncLimit=2  
    tickTime=2000
    
    # server ip list
    server.1=<ip of first server>:3888
    server.2=0.0.0.0:2888:3888
    server.3=<ip of third server>:2888:3888  
-----------------------------------------------      
# The setting for node 3
    dataDir=/var/lib/zookeeper  
    clientPort=2181  
    maxClientCnxns=0  
    initLimit=5  
    syncLimit=2  
    tickTime=2000
    
    # server ip list
    server.1=<ip of first server>:3888
    server.2=<ip of second server>:3888
    server.3=0.0.0.0:2888:3888
----------------------------------------------- 
```  

<p align="center">
  <img width="800" height="350" src="https://github.com/ChunYen-Chang/Personalized-restaurant-RESTfulAPI-Using-Kafka-and-Spark/blob/master/image/kaf_install_9.png">
</p> 

**Step8:** Run Zookeeper at each EC2 instance 
<p align="center">
  <img width="800" height="350" src="https://github.com/ChunYen-Chang/Personalized-restaurant-RESTfulAPI-Using-Kafka-and-Spark/blob/master/image/kaf_install_10.png">
</p>  

**Step9:** Check whether you successfully start the zookeeper cluster or not
<p align="center">
  <img width="800" height="350" src="https://github.com/ChunYen-Chang/Personalized-restaurant-RESTfulAPI-Using-Kafka-and-Spark/blob/master/image/kaf_install_11.png">
</p>  

-----
#### *PART THREE - Install Apache Kafka*
**Step1:** Configure Kafka server.properties file. Please make sure you modify this file at each EC2 instance  
<p align="center">
  <img width="800" height="350" src="https://github.com/ChunYen-Chang/Personalized-restaurant-RESTfulAPI-Using-Kafka-and-Spark/blob/master/image/kaf_install_12.png">
</p>  

```  
----------------------------------------------- 
# The setting for node 1
    broker.id=10
    log.dirs=/tmp/kafka-logs
    zookeeper.connect=<Ip of first server>:2181,<Ip of second server>:2181,<Ip of third server>:2181
    zookeeper.connection.timeout.ms=6000
-----------------------------------------------    
# The setting for node 2
    broker.id=20
    log.dirs=/tmp/kafka-logs
    zookeeper.connect=<Ip of first server>:2181,<Ip of second server>:2181,<Ip of third server>:2181
    zookeeper.connection.timeout.ms=6000
-----------------------------------------------      
# The setting for node 3
    broker.id=30
    log.dirs=/tmp/kafka-logs
    zookeeper.connect=<Ip of first server>:2181,<Ip of second server>:2181,<Ip of third server>:2181
    zookeeper.connection.timeout.ms=6000
----------------------------------------------- 
```  

<p align="center">
  <img width="800" height="350" src="https://github.com/ChunYen-Chang/Personalized-restaurant-RESTfulAPI-Using-Kafka-and-Spark/blob/master/image/kaf_install_13.png">
</p>  

**Step2:** Run Kafka at each EC2 instance  

<p align="center">
  <img width="800" height="350" src="https://github.com/ChunYen-Chang/Personalized-restaurant-RESTfulAPI-Using-Kafka-and-Spark/blob/master/image/kaf_install_15.png">
</p>  

**Step3:** Check whether you successfully start the Kafka cluster or not  
<p align="center">
  <img width="800" height="350" src="https://github.com/ChunYen-Chang/Personalized-restaurant-RESTfulAPI-Using-Kafka-and-Spark/blob/master/image/kaf_install_16.png">
</p>  

#### *PART FOUR - Quick testing*  

**Step1:** Create a topic "test" in this Kafka cluster  
<p align="center">
  <img width="800" height="350" src="https://github.com/ChunYen-Chang/Personalized-restaurant-RESTfulAPI-Using-Kafka-and-Spark/blob/master/image/kaf_install_17.png">
</p>  

**Step2:** Create a message producer for sending message to this "test" topic  
<p align="center">
  <img width="800" height="350" src="https://github.com/ChunYen-Chang/Personalized-restaurant-RESTfulAPI-Using-Kafka-and-Spark/blob/master/image/kaf_install_18.png">
</p>  

**Step3:** Create a consumer for receiving message from this "test" topic
<p align="center">
  <img width="800" height="350" src="https://github.com/ChunYen-Chang/Personalized-restaurant-RESTfulAPI-Using-Kafka-and-Spark/blob/master/image/kaf_install_20.png">
</p>  

**Step4:** Use producer to send a message to the topic  
<p align="center">
  <img width="800" height="350" src="https://github.com/ChunYen-Chang/Personalized-restaurant-RESTfulAPI-Using-Kafka-and-Spark/blob/master/image/kaf_install_19.png">
</p>  

**Step5:** Use consumer to receive a message to receive the message
<p align="center">
  <img width="800" height="350" src="https://github.com/ChunYen-Chang/Personalized-restaurant-RESTfulAPI-Using-Kafka-and-Spark/blob/master/image/kaf_install_21.png">
</p>  

**Step6:** Congratulations. You already had a Kafka cluster which works properly, enjoy it!