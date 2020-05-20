import time
import pandas as pd
import os
import logging

def extract_tranform():
    URL = 'http://winterolympicsmedals.com/medals.csv'
    data = pd.read_csv(URL)
    #  Tranform
    medal_by_country = pd.DataFrame({'count' : data.groupby( [ "NOC", "Medal"] ).size()}).reset_index()
    pairs_medals = data[data['Event'] == 'pairs']

    print(data)
    print(medal_by_country)
    print(pairs_medals)

def load():
    time.sleep(25) #  Very easy example.
    print("This would be a call: export to a data warehouse")
