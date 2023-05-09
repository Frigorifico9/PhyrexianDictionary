from words.models import *
import sys
import pandas as pd

def run():
    inDF = pd.read_csv('import/phy_import.csv')
    inDF = inDF.dropna(axis=0, subset = 'Official')
    print(inDF)
