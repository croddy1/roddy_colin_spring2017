import pandas as pd
from pandas import DataFrame
import sys, os

#Read in data
dataPath = os.getcwd()+'/Data/employee_compensation.csv'
df = pd.read_csv(dataPath)

#Filter data by calendar year
df = df[df['Year Type'] == 'Calendar']

#Create new dataFrame of only Job Family, Employee Identifier, and all Compensation data
cols = ['Job Family'] + list(df.loc[:,'Employee Identifier':'Total Compensation'])
sals = df[cols]

#Averaging all Employee Compensation data over the years
avg_sals = sals.groupby('Employee Identifier').mean()

#People whos overtime is greater than 5% of their salary
greater = avg_sals[avg_sals['Overtime'] > (avg_sals['Salaries']*0.05)]

#DataFrame of only Employee Identifier and Job Family
zoo = ['Employee Identifier'] + ['Job Family']
job = df[zoo]

#Drop all duplicate copies of Employee Identifier
jobs = job.drop_duplicates('Employee Identifier').set_index('Employee Identifier')

#Merge Job Family into Average Compensation
fin_sal = pd.merge(greater, jobs, left_index=True, right_index=True)

#Calculate percent of Compensation that come from Benefits
fin_sal['Percentage Ben/Comp'] = (fin_sal['Total Benefits']/fin_sal['Total Compensation'])*100

#Keep only Job Family, Total Benefits, Total Compensation, and Percentage data
coo = list(fin_sal.loc[:,'Total Benefits':'Percentage Ben/Comp'])
final = fin_sal[coo]

#Average the compensation data by Job Family
holder = final.groupby('Job Family').mean()
print(holder.head())

#write to csv file
holder.to_csv('Q2_Part_2.csv',index=True,header=True)
