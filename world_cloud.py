#!/usr/bin/python3.7

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

with open ("alice_in_wonderland.txt") as f:
    text = f.read()

worldcloud = WordCloud(width=1920, height=1200)
worldcloud.generate(text)

STOPWORDS.add('said')
STOPWORDS.add('Illustration')

plt.imshow(worldcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
