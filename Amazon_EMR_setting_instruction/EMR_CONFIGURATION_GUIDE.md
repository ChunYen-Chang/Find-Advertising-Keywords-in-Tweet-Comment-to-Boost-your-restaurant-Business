# How to configure an AWS EMR spark cluster for this project
This documentation shows how to build an AWS EMR spark cluster. It can be seperated into three parts. The detail of each part is listed below.
1. **PART ONE :** Upload **emr_other_packages.sh** in you Amazon S3 bucket. 
2. **PART TWO :** Build an AWS EMR spark cluster
3. **PART THREE :** Download .jar file in the Spark master node
-----
#### *PART ONE - Upload **emr_other_packages.sh** in you Amazon S3 bucket*
**Step1:** Upload **emr_other_packages.sh** in you Amazon S3 bucket  
This .sh file is a bash script which helps you to install all necessary python packages for this project in all your Spark cluster nodes.
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Personalized-restaurant-RESTfulAPI-Using-Kafka-and-Spark/blob/master/image/EMR_ser_00.png">
</p>  
  
-----
#### *PART TWO - Build an AWS EMR spark cluster*
**Step1:** Click **Create cluster**
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Personalized-restaurant-RESTfulAPI-Using-Kafka-and-Spark/blob/master/image/EMR_ser_01.png">
</p>  

**Step2:** Click **Go to advanced options**
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Personalized-restaurant-RESTfulAPI-Using-Kafka-and-Spark/blob/master/image/EMR_ser_02.png">
</p>  

**Step3:** Choose softwares you want to install in your Spark cluster
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Personalized-restaurant-RESTfulAPI-Using-Kafka-and-Spark/blob/master/image/EMR_ser_03.png">
</p>  

**Step4:** Choose Hardware setting for your Spark cluster, in this project, we use default setting
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Personalized-restaurant-RESTfulAPI-Using-Kafka-and-Spark/blob/master/image/EMR_ser_04.png">
</p>  

**Step5:** Click **Bootstrap Actions**
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Personalized-restaurant-RESTfulAPI-Using-Kafka-and-Spark/blob/master/image/EMR_ser_05.png">
</p>  

**Step6:** Click **Custom action**
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Personalized-restaurant-RESTfulAPI-Using-Kafka-and-Spark/blob/master/image/EMR_ser_06.png">
</p>  

**Step7:** In Script location, type the emr_other_packages.sh file path. 
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Personalized-restaurant-RESTfulAPI-Using-Kafka-and-Spark/blob/master/image/EMR_ser_07.png">
</p>  

**Step8:** Click **Next**
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Personalized-restaurant-RESTfulAPI-Using-Kafka-and-Spark/blob/master/image/EMR_ser_08.png">
</p>  

**Step9:** Click **EC2 key pair** and choose the AWS key. Then, Click **Create cluster**
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Personalized-restaurant-RESTfulAPI-Using-Kafka-and-Spark/blob/master/image/EMR_ser_09.png">
</p>  

#### *PART THREE - Download .jar file in the Spark master node*  

**Step1:** Download **spark-streaming-kafka-0-8-assembly_2.11-2.2.0.jar** file in the Spark master node  
This file --**spark-streaming-kafka-0-8-assembly_2.11-2.2.0.jar**-- is important, this project needs this one for connecting AWS EMR cluster with Kafka Cluster.
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Personalized-restaurant-RESTfulAPI-Using-Kafka-and-Spark/blob/master/image/EMR_ser_10.png">
</p>  

**Step2:** Copy this file to **/usr/lib/spark/jars**
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Personalized-restaurant-RESTfulAPI-Using-Kafka-and-Spark/blob/master/image/EMR_ser_11.png">
</p>  

**Step6:** Congratulations. All the necessary steps for this project are finished.