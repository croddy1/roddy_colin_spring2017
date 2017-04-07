import pandas as pd
from pandas import DataFrame
import sys, os, datetime

#Read in data
dataPath = os.getcwd()+'/Data/vehicle_collisions.csv'
df = pd.read_csv(dataPath)

#Convert date colume to datetime format (this takes some time, ~1 min on my machine)
df['DATE'] = pd.to_datetime(df['DATE'])

#Create new dataframe with only entries from 2016
zoo16 = df[(df['DATE'] >= '2016-01-01') & (df['DATE'] <= '2016-12-31')]

#Create a new colum representing the month of the colision
zoo16['MONTH'] = zoo16['DATE'].apply(lambda x : x.strftime('%b'))

#Create a list of all unique months in the collisions dataFrame from 2016
mon = zoo16['MONTH'].unique()

#Create a dataFrame with Month, number of accidents in Manhattan, number of accidents in NYC, and percentage of accidents in Manhattan compared to all of NYC

data = {'MONTH':[],'MANHATTAN':[],'NYC':[],'PERCENTAGE':[]} #data holder
for each in mon:
    thisMonth = zoo16[zoo16['MONTH'] == each] #Create new dataFrame of only given month
    nyc = len(thisMonth) #count NYC collisions
    man = len(thisMonth[thisMonth['BOROUGH'] == 'MANHATTAN']) #count Manhattan collisions
    perc = man/nyc #calculate percentage
    
    #store data
    data['MONTH'].append(each)
    data['MANHATTAN'].append(man)
    data['NYC'].append(nyc)
    data['PERCENTAGE'].append(perc)

dframe = DataFrame(data, columns=['MONTH','MANHATTAN','NYC','PERCENTAGE'])
print(dframe.head())

#write to csv file
dframe.to_csv('Q1_Part_1.csv',index=False,header=True)
