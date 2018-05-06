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

filename=open('content.txt', 'r')
read_some_text = filename.readlines()
length_read_some_text = len(open('content.txt', 'r').readlines())
filename.close()

#for i in range(0,3):
  #random_tweet = random_line + random_tweet
  #add all three lines together in one tweet, separated by new line?? not quite there
while True != False:
  try:
    random_line = read_some_text[randint(0,length_read_some_text)]
    api.update_status(random_line)
    print("tweeting")
  except tweepy.TweepError , err:
    print(err)
  sleep(212000)
