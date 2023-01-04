# libraries
import matplotlib.pyplot as plt
import numpy as np
 
# data 
#   I hardcoded this in because I was on a deadline which obviously isn't 
#   optimal but it works for graph generation 
years    = ['2001', '2010', '2021']
negative = np.array([16.4, 11.6, 6.4])
neutral = np.array([75.2, 79.9, 87.8])
positive  = np.array([8.4, 8.5, 5.8])
 
# plot bars 
plt.bar(years, positive, color='#76b800')
plt.bar(years, neutral, bottom=positive, color='#35b4d7')
plt.bar(years, negative, bottom=positive+neutral, color='#e01f2d')
plt.xlabel("Years")
plt.ylabel("Percentage")
plt.show()