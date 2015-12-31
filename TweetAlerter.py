import tweepy
import ctypes

CONSUMER_KEY = "key"
CONSUMER_SECRET = "key"
ACCESS_KEY = "key"
ACCESS_SECRET = "key"
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#if you want to hardcode it you can put the username as a string instead of input
twitterAccount = input("What twitter account are you gonna watch? ")
twitterAccountID = api.get_user(twitterAccount)
twitterAccountID = twitterAccountID.id

def message(text, Title, Type):
    MessageBox = ctypes.windll.user32.MessageBoxW
    MessageBox(None, text, Title, Type)

class streamListener(tweepy.StreamListener):
    def on_status(self, status):
        user = status.user.screen_name
        print(user + ":    " + status.text)
        print("http://www.twitter.com/{0}".format(user) + "\n")
        message('{0} tweeted: {1}.'.format(user, status.text), 'NEW TWEET', 0)

    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True
 
    def on_timeout(self):
        print('Timeout...')
        return True


if __name__ == '__main__':
    listener = streamListener()
 
    stream = tweepy.Stream(auth, listener)
    stream.filter(follow=[str(twitterAccountID)])

