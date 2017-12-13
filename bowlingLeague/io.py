import pandas as pd
import glob


def getLeagueNames():
    files = glob.glob('./data/leagues/*.csv')
    names = [i.split('/')[-1].split('.csv')]
    return names
