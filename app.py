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
    randomline1 = lines[randint(0, linenumbs)] #chooses a random line in content.txt
    randomline2 = lines[randint(0, linenumbs)] #chooses another random line in context.txt
    line1split = randomline1.split(" ") #splits randomline1 at each space, creates a list
    line2split = randomline2.split(" ") #splits randomline2 at each space, creates a list
    tweet = line1split[0:len(line1split)/2] + line2split[len(line1split)/2:len(line2split)]
    #tweet = the first half of the first line plus the second half of the second line, new list
    api.update_status(' '.join(tweet)) #contents of tweet are joined with a space
    print("tweeting")
  except tweepy.TweepError , err:
    print(err)
  sleep(3600)
