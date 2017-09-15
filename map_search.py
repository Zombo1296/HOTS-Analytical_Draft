import sys,json
from pprint import pprint

with open('hero_data.json') as data_file:    
    heroDict = json.load(data_file)

def searchMap(tDict, tMap):
    heroList = []
    for key in tDict:
        for v in tDict[key]['maps']:
            if tMap in v:
                heroList.append(key)
    return heroList

mapsShorten = {'hm':'Haunted Mines','h':'Hanamura','ts':'Tomb of the Spider Queen','gt':'Garden of Terror',
               'bh':'Braxis Holdout','td':'Towers of Doom','is':'Infernal Shrines','st':'Sky Temple',
               'be':'Battlefield of Eternity','bb':'Blackhearts Bay','ds':'Dragon Shire',
               'ch':'Cursed Hollow','wj':'Warhead Junction'}

token = mapsShorten[sys.argv[1]]

heroInfo = searchMap(heroDict, token)

pprint(heroInfo)