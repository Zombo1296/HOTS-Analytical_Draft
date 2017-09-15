import sys,json
from pprint import pprint

with open('hero_data.json') as data_file:    
    heroDict = json.load(data_file)

cList = heroDict[sys.argv[1]]['cBy']

pprint(cList)