import pandas as pd
from pandas import DataFrame
import sys, os, datetime

#Read in data
dataPath = os.getcwd()+'/Data/vehicle_collisions.csv'
df = pd.read_csv(dataPath)

#Fill NaN data in 'BOROUGH' and create list of boroughs
df['BOROUGH'].fillna('UNRECORDED',inplace=True)
bos = df['BOROUGH'].unique()

#Create dataFrame of vehicle count in collisions for each borough
holder = []
for each in bos:
    boro = df[df['BOROUGH'] == each] #pull borough specific data
    veh = boro.loc[:,'VEHICLE 1 TYPE':'VEHICLE 5 TYPE'] #pull only vehicle-type data
    veh['NUM'] = veh.count(axis=1) #count number of non-empty cells in each row, gives num vehicles in collision
    vals = veh['NUM'].value_counts() #get count for each unique NUM
    #append information to holder list
    holder.append((each, vals[1], vals[2], vals[3], (vals[4]+vals[5])))

#create dataFrame from holder list
collisions = DataFrame(holder, columns=('BOROUGH',
                                        'ONE_VEHICLE_INVOLVED',
                                        'TWO_VEHICLES_INVOLVED',
                                        'THREE_VEHICLES_INVOLVED',
                                        'MORE_VEHICLES_INVOLVED')).sort_values(by='BOROUGH').reset_index(drop=True)
print(collisions.head())

#write to csv file
collisions.to_csv('Q1_Part_2.csv',index=False,header=True)
