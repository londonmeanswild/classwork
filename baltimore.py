#!/usr/bin/env python3
# (c) 2017 Landon A Marchant
""" Imports CSV of baseball statistics, and plots them. """


import csv
import matplotlib.pyplot as plt

games_above = []

with open('baltimore16.csv', 'r') as f:
    csvf = csv.reader(f)
    for row in csvf:

        #print(row)
        if row[0] == 'Gm#':
            continue
        #print(row[0])

        w, l = row[10].split('-') # returns a string 13, not integer thirteen
        wins = int(w)
        loss = int(l)
        games_above.append(wins-loss)  # or games_above.append(eval(row[10])) or: .append(w-l)
        
        
number_over_500 = len(games_above)

plt.title('The 2016 Baltimore Orioles Season')
plt.xlabel('Game number')
plt.ylabel('Games over .500') 
plt.plot(range(1,number_over_500+1), games_above, 'r-') # plot in red using lines. gamesAbove is y
plt.axis([1,number_over_500, 0, 50]) # range of data I want to see. 1,n = x range, 0,50 = y
plt.savefig('baltimore.pdf') 

plt.show('baseball.pdf')