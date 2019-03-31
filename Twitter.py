from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import tweepy
from keytwitter import *

text = ''
auth = tweepy.OAuthHandler(key, secret)
api = tweepy.API(auth)

tweeds = api.user_timeline(screen_name='realDonaldTrump', count=100, include_rts = False, tweet_mode = 'extended')
for tweed in tweeds:
    text = text +' '+ tweed.full_text

worldcloud = WordCloud(width=1920, height=1200)
STOPWORDS.update('https','co')
worldcloud.generate(text)
plt.imshow(worldcloud)
plt.axis('off')
plt.show()




