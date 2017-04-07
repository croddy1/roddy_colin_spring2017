import pandas as pd
from pandas import DataFrame
import sys, os, string

#Read in data
dataPath = os.getcwd()+'/Data/movies_awards.csv'
df = pd.read_csv(dataPath)

#Count the number of wins for a movie
def countWins(s):
    new = s.replace('.','')
    zoo = new.lower().split(' ')
    wins = 0
    
    if 'win' in zoo:
        wins += 1
    
    if 'wins' in zoo:
        w = zoo[zoo.index('wins')-1]
        wins += int(w)
    
    if 'won' in zoo:
        w = zoo[zoo.index('won')+1]
        if w.isdigit():
            wins += int(w)

    return wins

#Count the number of nominations for a movie
def countNoms(s):
    new = s.replace('.','')
    zoo = new.lower().split(' ')
    noms = 0
    if 'nominated' in zoo:
        n = zoo[zoo.index('nominated')+2]
        if n.isdigit():
            noms += int(n)

    if 'nominations' in zoo:
        n = zoo[zoo.index('nominations')-1]
        if n.isdigit():
            noms += int(n)

    if 'nomination' in zoo:
        noms += 1
    
    return noms

#prime
#Count Primetime Emmy nominations
def primeNoms(s):
    new = s.replace('.','')
    zoo = new.lower().split(' ')
    noms = 0
    if 'nominated' in zoo and 'primetime' in zoo:
        n = zoo[zoo.index('primetime')-1]
        if n.isdigit():
            noms += int(n)
    return noms
#Count Primetime Emmy wins
def primeWins(s):
    new = s.replace('.','')
    zoo = new.lower().split(' ')
    wins = 0
    if 'won' in zoo and 'primetime' in zoo:
        n = zoo[zoo.index('primetime')-1]
        if n.isdigit():
            wins += int(n)
    return wins

#oscar
#Count Oscar nominations
def oscarNoms(s):
    new = s.replace('.','')
    zoo = new.lower().split(' ')
    noms = 0
    if 'nominated' in zoo and 'oscar' in zoo:
        n = zoo[zoo.index('oscar')-1]
        if n.isdigit():
            noms += int(n)
    if 'nominated' in zoo and 'oscars' in zoo:
        n = zoo[zoo.index('oscars')-1]
        if n.isdigit():
            noms += int(n)
    return noms
#Count Oscar wins
def oscarWins(s):
    new = s.replace('.','')
    zoo = new.lower().split(' ')
    wins = 0
    if 'won' in zoo and 'oscar' in zoo:
        n = zoo[zoo.index('oscar')-1]
        if n.isdigit():
            wins += int(n)
    if 'won' in zoo and 'oscars' in zoo:
        n = zoo[zoo.index('oscars')-1]
        if n.isdigit():
            wins += int(n)
    return wins

#golden
#Count Golden Globe nominatiosn
def goldenNoms(s):
    new = s.replace('.','')
    zoo = new.lower().split(' ')
    noms = 0
    if 'nominated' in zoo and 'golden' in zoo:
        n = zoo[zoo.index('golden')-1]
        if n.isdigit():
            noms += int(n)
    return noms
#Count Golden Globe wins
def goldenWins(s):
    new = s.replace('.','')
    zoo = new.lower().split(' ')
    wins = 0
    if 'won' in zoo and 'golden' in zoo:
        n = zoo[zoo.index('golden')-1]
        if n.isdigit():
            wins += int(n)
    return wins

#bafta
#Count BAFTA Movie Award nominations
def baftaNoms(s):
    new = s.replace('.','')
    zoo = new.lower().split(' ')
    noms = 0
    if 'nominated' in zoo and 'bafta' in zoo:
        n = zoo[zoo.index('bafta')-1]
        if n.isdigit():
            noms += int(n)
    return noms
#Count BAFTA Movie Award wins
def baftaWins(s):
    new = s.replace('.','')
    zoo = new.lower().split(' ')
    wins = 0
    if 'won' in zoo and 'bafta' in zoo:
        n = zoo[zoo.index('bafta')-1]
        if n.isdigit():
            wins += int(n)
    return wins

#create new columns using count functions defined above
df['Total Nominations'] = df['Awards'].apply(lambda x: countNoms(x) if isinstance(x,str) else 0)
df['Total Wins'] = df['Awards'].apply(lambda x: countWins(x) if isinstance(x,str) else 0)
df['Primetime Emmy Nominations'] = df['Awards'].apply(lambda x: primeNoms(x) if isinstance(x,str) else 0)
df['Oscar Nominations'] = df['Awards'].apply(lambda x: oscarNoms(x) if isinstance(x,str) else 0)
df['Golden Glob Nominations'] = df['Awards'].apply(lambda x: goldenNoms(x) if isinstance(x,str) else 0)
df['BAFTA Nominations'] = df['Awards'].apply(lambda x: baftaNoms(x) if isinstance(x,str) else 0)
df['Primetime Emmy Wins'] = df['Awards'].apply(lambda x: primeWins(x) if isinstance(x,str) else 0)
df['Oscar Wins'] = df['Awards'].apply(lambda x: oscarWins(x) if isinstance(x,str) else 0)
df['Golden Glob Wins'] = df['Awards'].apply(lambda x: goldenWins(x) if isinstance(x,str) else 0)
df['BAFTA Wins'] = df['Awards'].apply(lambda x: baftaWins(x) if isinstance(x,str) else 0)

print(df.head())

#write to csv file
df.to_csv('Q4_Part_1.csv',index=False,header=True)
