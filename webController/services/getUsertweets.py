import tweepy
import webController.services.credentials as credentials
import textAnalyser.textParser as parser

# Consumer keys and access tokens, used for OAuth
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(credentials.twitterCredentials.consumerKey, credentials.twitterCredentials.consumerSecret)
auth.set_access_token(credentials.twitterCredentials.accessToken, credentials.twitterCredentials.accessTokenSecret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)
writer = parser.parseWriter()


for status in tweepy.Cursor(api.user_timeline, screen_name='@BoulderOEM').items():
    writer.addTweet(str(status._json['text']), str(status._json['created_at']), str(status._json['favorite_count']), str(status._json['retweet_count']))
    print(str(status._json['text']))