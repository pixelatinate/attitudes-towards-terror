import matplotlib.pyplot as plt
from nltk.tokenize import sent_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

with open('articles/2001.txt', 'r') as file:
    article01 = file.read().replace('\n', '')
    print(sia.polarity_scores(article01))

with open('articles/2010.txt', 'r') as file:
    article10 = file.read().replace('\n', '')
    print(sia.polarity_scores(article10))
    
with open('articles/2021.txt', 'r') as file:
    article21 = file.read().replace('\n', '')
    print(sia.polarity_scores(article21))

ss = sia.polarity_scores(article01)
labels = ['negative', 'neutral', 'positive']
plt.bar(neg, color='r')
plt.bar(neu, bottom=neg, color='b')
plt.bar(pos, bottom=neg+neu, color='g')

plt.show()


