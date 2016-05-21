"""
    This is used to alert the user of new tweets from a selected follower.
"""
import ctypes
import credentials
import tweepy

CONSUMER_KEY = credentials.CONSUMER_KEY
CONSUMER_SECRET = credentials.CONSUMER_SECRET
ACCESS_KEY = credentials.ACCESS_KEY
ACCESS_SECRET = credentials.ACCESS_SECRET
AUTH_KEY = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
AUTH_KEY.set_access_token(ACCESS_KEY, ACCESS_SECRET)
API = tweepy.API(AUTH_KEY)

TWITTER_ACCOUNT = input("What twitter account are you gonna watch? ")
TWITTER_ACCOUNT_ID = API.get_user(TWITTER_ACCOUNT)
TWITTER_ACCOUNT_ID = TWITTER_ACCOUNT_ID.id

def message(text, title, boxtype=0):
    """Used to popup a message to the user"""
    message_box = ctypes.windll.user32.MessageBoxW
    message_box(None, text, title, boxtype)

class StreamListener(tweepy.StreamListener):
    """Used to get new tweets as they are sent out."""
    def on_status(self, status):
        user = status.user.screen_name
        print(user + ":    " + status.text)
        print("http://www.twitter.com/{0} \n".format(user))
        message('{0} tweeted: {1}.'.format(user, status.text), 'NEW TWEET')

    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True

    def on_timeout(self):
        print('Timeout...')
        return True

if __name__ == '__main__':
    LISTENER = StreamListener()
    STREAM = tweepy.Stream(AUTH_KEY, LISTENER)
    STREAM.filter(follow=[str(TWITTER_ACCOUNT_ID)])
    