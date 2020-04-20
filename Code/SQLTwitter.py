import mysql.connector
from mysql.connector import Error
import tweepy
import json
from dateutil import parser
import subprocess

from config import consumer_key, consumer_secret, access_token, access_token_secret, db_password


def connect(created_at, username, tweet, location, followers_count, tweet_id):
    """
    connect to MySQL database and insert twitter data
    """
    try:
        con = mysql.connector.connect(host = 'localhost',
        database='Twitter', user='root', password = db_password,
        auth_plugin='mysql_native_password', charset = 'utf8')

        if con.is_connected():

            #Insert twitter data

            cursor = con.cursor()
          
            query = "INSERT INTO no_retweet (created_at, username, tweet, location, \
                    followers_count, tweet_id) \
                    VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (created_at, username, tweet, location, followers_count, tweet_id))

            con.commit()
            cursor.close()
            con.close()

    except Error as e:
        print(e)


    return

# Tweepy class to access Twitter API
class Streamlistener(tweepy.StreamListener):


    def on_connect(self):
        print("You are connected to the Twitter API")


    def on_error(self):
        if status_code != 200:
            print("error found")
        # returning false disconnects the stream
            return False

    def on_status(self, status):
        """
        Only reads in tweets that are not retweets.
        """
        if status.retweeted_status:
            return
    
    def on_data(self,data):
        """
        This method reads in tweet data as JSON
        and extracts the data we want.
        """

        try:
            raw_data = json.loads(data)

            if 'text' in raw_data:

                if 'extended_tweet' in raw_data:
                    # gets extended text if possible instead of cutting off tweet
                    tweet = raw_data['extended_tweet']['full_text']
                    created_at = raw_data['created_at']
                    username = raw_data['user']['screen_name']
                    location = raw_data['user']['location']
                    followers_count = raw_data['user']['followers_count']
                    tweet_id = raw_data['id']

                    connect(created_at, username, tweet, location, followers_count, tweet_id)
                    print("Tweet collected at: {} ".format(str(created_at)))

                else:
                    created_at = raw_data['created_at']
                    username = raw_data['user']['screen_name']
                    tweet = raw_data['text']
                    location = raw_data['user']['location']
                    followers_count = raw_data['user']['followers_count']
                    tweet_id = raw_data['id']
               
                    connect(created_at, username, tweet, location, followers_count, tweet_id)
                    print("Tweet collected at: {} ".format(str(created_at)))

        except Error as e:
            print(e)

if __name__ == '__main__':

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    listener = Streamlistener(api = api)
    stream = tweepy.Stream(auth, listener = listener)

    track = ['coronavirus', 'COVID-19', 'novel', 'unprecedented']

    # choose what we want to filter by
    stream.filter(track = track, languages = ['en'])
