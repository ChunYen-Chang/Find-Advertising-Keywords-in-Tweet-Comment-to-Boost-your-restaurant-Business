# import packages
import datetime
import tweepy
from kafka import KafkaProducer


# open the file which contains the account informaiton about accessing to Tweet API 
with open('tweet_api.txt') as file:
    text = file.read()
    lines = (text.split('\n'))
    consumer_api_key = lines[0].split(' = ')[1]
    consumer_api_secret_key = lines[1].split(' = ')[1]
    access_token = lines[2].split(' = ')[1]
    access_token_secret = lines[3].split(' = ')[1]

    
# set up an instance for access to Tweet API
auth = tweepy.OAuthHandler(consumer_api_key, consumer_api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# instantiate a Kafka producer
producer = KafkaProducer(bootstrap_servers=['<your kafka broker IP address>:<your kafka broker port, default is 9092>'])


# define a class for receiving the streaming data from Tweet API
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        if 'RT @' not in status.text:
            tweet_item = {
                'id_str': status.id_str,
                'text': status.text,
                'received_at': datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S"),
            }
            
			tweet_content = tweet_item['id_str'] + '|||||' + tweet_item['text'] + '|||||' + tweet_item['received_at']
			
            # send data to Kafka broker
            producer.send('restaurant', tweet_content.encode('utf-8'))


if __name__ == '__main__':
	# start to receive data from tweet and send to Kafka cluster
	stream_listener = MyStreamListener()
	stream = tweepy.Stream(auth=api.auth, listener=stream_listener)

	# filter the Tweet text, only exteact the text which contains two key words--"restaurant" 
	stream.filter(languages=['en'], track=['restaurant'])