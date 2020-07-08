import sys
import tweepy
from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
import requests
from lxml import html

def create_tweet():
    response = requests.get('https://www.worldometers.info/coronavirus/')
    doc = html.fromstring(response.content)
    total, deaths, recovered = doc.xpath('//div[@class="maincounter-number"]/span/text()')

    #your tweet will be seen as below so add your hashtags
    tweet = f'''Coronavirus automated WorldWide Latest Updates
Total cases: {total}
Recovered: {recovered}
Deaths: {deaths}
Source: https://www.worldometers.info/coronavirus/
Stay Safe
#covid19 #Programming #100DaysOfCode #Python #CodeNewbie
'''
    return tweet

if __name__ == '__main__':
    auth = tweepy.OAuthHandler('Consumer_key','Consumer_secret')
auth.set_access_token('Access_token','Access_token_secret')
    # Create API object
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print('Authentication Successful')
except:
    print('Error while authenticating API')
    sys.exit(1)

tweet = create_tweet()
api.update_status(status =(tweet))
print('Tweet successful')
