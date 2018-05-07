import tweepy
from time import sleep
from random import randint

CONSUMER_KEY = '9RXWrjYJ4fY9vzGJuStKWJTDw'
CONSUMER_SECRET = 'oSrpOEYJ8HRAdCFmbEbmgsUFeSSLaamV206YvWgodbtlbcWSv8'
ACCESS_TOKEN = '992562987213914118-xSKB4iINLSKV9GxjLgNrA0JNq748kU2'
ACCESS_SECRET = 'n2uXfxTWFpq3vf0k9iNp1xZe9KBNaXn7PAhIGBO6DfE2C'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)
linenumbs = len(open('content.txt', 'r').readlines())
filename=open('content.txt', 'r')
lines = filename.readlines()
filename.close()

while True != False:
  try:
    randomline1 = lines[randint(0, linenumbs)]
    randomline2 = lines[randint(0, linenumbs)]
    tweet = randomline1[0:len(randomline1)/2] + randomline2[len(randomline1)/2:len(randomline2)]
    api.update_status(tweet)
    print("tweeting")
  except tweepy.TweepError , err:
    print(err)
  sleep(3600)
