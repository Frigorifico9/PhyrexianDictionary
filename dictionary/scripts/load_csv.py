from words.models import *
import sys
import pandas as pd

def run():
    inDF = pd.read_csv('import/phy_import.csv')
    inDF = inDF.dropna(axis=0, subset = 'Official')[['Official', 'Latin', 'IPA', 'Definition']]
    inDF = inDF.loc[inDF['Official'] != '--'] #remove line 3
    wordimport = [PhyrexianWord(phyrexian='phyrexianPlaceholder', official=obj.Official, latin = obj.Latin, ipa = obj.IPA, definition = obj.Definition) for obj in inDF.itertuples()]
    for i in wordimport:
        if PhyrexianWord.objects.filter(official=i.official).count() == 0: #check if entry exists
            i.save()