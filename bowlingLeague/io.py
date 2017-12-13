import pandas as pd
import glob


def getLeagueNames():
    files = glob.glob('./data/leagues/*.json')
    names = [i.replace('\\', '/').split('/')[-1].split('.json')[0]
             for i in files]
    return names
