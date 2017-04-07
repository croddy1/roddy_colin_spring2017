import pandas as pd
from pandas import DataFrame
import sys, os

#Read in data
dataPath = os.getcwd()+'/Data/cricket_matches.csv'
df = pd.read_csv(dataPath)

#Create dataFrame of only home winners
winners = df[df['home'] == df['winner']]

#Create dataFrame of home winners innings 1 data
win1 = winners[['home'] + ['innings1'] + ['innings1_runs']]
win1.columns = ['home','innings1','Score']
#remove any data where home winner didn't win inning 1
win1 = win1[win1['innings1'] == win1['home']]

#Create dataFrame of home winners innings 2 data
win2 = winners[['home'] + ['innings2'] + ['innings2_runs']]
win2.columns = ['home','innings2','Score']
#remove any data where home winner didn't win inning 2
win2 = win2[win2['innings2'] == win2['home']]

#Append innings 1 and 2 data together to create dataFrame of only home winner scores
homeWinners = win1.append(win2)

#Take mean of each home winning team score
output = homeWinners.groupby('home').mean()
print(output.head())

#write to csv file
output.to_csv('Q3_Part_1.csv',index=True,header=True)
