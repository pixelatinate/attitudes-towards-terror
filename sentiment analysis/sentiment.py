# libraries
import numpy as np
from itertools import chain
import matplotlib.pyplot as plt
from nltk.tokenize import sent_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer

# initialize variables
sia = SentimentIntensityAnalyzer()
years = np.array(["2001", "2010", "2021"])

# read files and organize in a way that a graph can be generated straightaway
#   I did not succeed at this because again, I was on a deadline lol
with open('articles/2001.txt', 'r') as file:
    article01 = file.read().replace('\n', '')
    newrow = sia.polarity_scores(article01)
    result = newrow.items()
    list01 = chain(list(result))
    list01 = list(chain.from_iterable(list01))
    del list01[0]
    del list01[1]
    del list01[2]
    del list01[3]

with open('articles/2010.txt', 'r') as file:
    article10 = file.read().replace('\n', '')
    newrow = sia.polarity_scores(article10)
    result = newrow.items()
    list10 = chain(list(result))
    list10 = list(chain.from_iterable(list10))
    del list10[0]
    del list10[1]
    del list10[2]
    del list10[3]
    
with open('articles/2021.txt', 'r') as file:
    article21 = file.read().replace('\n', '')
    newrow = sia.polarity_scores(article21)
    result = newrow.items()
    list21 = chain(list(result))
    list21 = list(chain.from_iterable(list21))
    del list21[0]
    del list21[1]
    del list21[2]
    del list21[3]

del list01[3]
array01 = np.array(list01)
print(array01)

del list10[3]
array10 = np.array(list10)
print(array10)

del list21[3]
array21 = np.array(list21)
print(array21)

years  = ['2001', '2010', '2021'] 
plt.bar(years, array01, color='r')
plt.bar(years, array10, bottom=array01, color='b')
plt.bar(years, array21, bottom=array01+array10, color='g')
plt.show()