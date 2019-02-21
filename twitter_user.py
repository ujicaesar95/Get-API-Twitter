# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the twitter library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '219318879-VO2z6J7qIK4hjKLAz9E68aKEeHDRoeJwIo1zdxMz'
ACCESS_SECRET = 'skadu9quTk94npgW6xKFxXH42YcbiWe3rKtgKMDNUmVA3'
CONSUMER_KEY = 'brLTTDqGomjHKRXFnu4JkjJID'
CONSUMER_SECRET = 'PdEklANwDdCuIVc3i6J1J0LEa1kvZqy5UvBgYGLOoKGGyHzjIl'

# Setup twitter to authenticate with Twitter credentials:

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

twitter = Twitter(auth=oauth)

# Create the api to connect to twitter with your creadentials

tweets = twitter.statuses.user_timeline(screen_name='Piquitha')

print(json.dumps(tweets, indent=4))

#---------------------------------------------------------------------------------------------------------------------
# wait_on_rate_limit= True;  will make the api to automatically wait for rate limits to replenish
# wait_on_rate_limit_notify= Ture;  will make the api  to print a notification when Tweepyis waiting for rate limits to replenish
#---------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------------------
# The following loop will print most recent statuses, including retweets, posted by the authenticating user and that user’s friends. 
# This is the equivalent of /timeline/home on the Web.
#---------------------------------------------------------------------------------------------------------------------

# for status in tweepy.Cursor(api.home_timeline).items(200):
# 	print(status._json)
	
#---------------------------------------------------------------------------------------------------------------------
# Twitter API development use pagination for Iterating through timelines, user lists, direct messages, etc. 
# To help make pagination easier and Tweepy has the Cursor object.
#---------------------------------------------------------------------------------------------------------------------