import webController.services.credentials as credentials
import textAnalyser.textParser as parser
import time
from twython import Twython
from twython import TwythonStreamer
import json
import time


class MyStreamer(TwythonStreamer):
    writer = parser.parseWriter()
    tweetCounter = 0
    count=0
    def on_success(self, data):
        if 'text' in data:
            if (self.tweetCounter < 300):
                self.writer.addTweet(str(data['text']),str(data['created_at']),str(data['favorite_count']),str(data['retweet_count']))

                self.tweetCounter += 1
                self.count+=1
                print("TWEETS:  "+ str(self.count))
            else:
                self.writer.newBlock(str(data['text']),str(data['created_at']),str(data['favorite_count']),str(data['retweet_count']))
                self.tweetCounter = 0

    def on_error(self, status_code, data):
        print(status_code)
        if(str(status_code) == "420"):
            print("waiting 15 mins for rate limiting")
            time.sleep(30)
        else:
            getTwitterStream("en")



        # Want to stop trying to get data because of the error?
        # Uncomment the next line!
        # self.disconnect()


def getTwitterData(searchTerm):
    python_tweets = MyStreamer(credentials.twitterCredentials.consumerKey, credentials.twitterCredentials.consumerSecret,credentials.twitterCredentials.accessToken,credentials.twitterCredentials.accessTokenSecret)

    tweets = python_tweets.statuses.filter(q=searchTerm, result_type='popular')
    output = json.dumps(tweets)
    return output

def getTwitterStream(lang):
    python_tweets = MyStreamer(credentials.twitterCredentials.consumerKey, credentials.twitterCredentials.consumerSecret,credentials.twitterCredentials.accessToken,credentials.twitterCredentials.accessTokenSecret)

    tweets = python_tweets.statuses.filter( language = 'en',track='disaster')
    print(tweets)
    output = json.dumps(tweets)
    return output