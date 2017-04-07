import pandas as pd
from pandas import DataFrame
import sys, os

#Read in data
dataPath = os.getcwd()+'/Data/employee_compensation.csv'
df = pd.read_csv(dataPath)

#Create new dataFrame with only Orgranizational Grouop, Department, and total Compensation
col = ['Organization Group'] + ['Department'] + ['Total Compensation']
comp = df[col]
comp.head()

#Calculate mean of Total Compensation for each Department in Each organization
avg_compensation = comp.groupby(['Organization Group','Department']).mean().sort_values(by='Total Compensation', ascending=False).sort_index()

print(avg_compensation.head())

#write to csv file
avg_compensation.to_csv('Q2_Part_1.csv',index=False,header=True)
