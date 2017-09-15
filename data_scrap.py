import requests,bs4

res = requests.get('https://www.icy-veins.com/heroes/talent-calculator')
res.raise_for_status()
heroNameSoup = bs4.BeautifulSoup(res.text,"lxml")

divEle = heroNameSoup.select("div.heroes-portraits > a > img")
hNameList = []
for imgEle in divEle:
    heroNames = imgEle["id"]
    heroNames = heroNames[0:-9]
    hNameList.append(heroNames);

# print(hNameList)
allHeroDict = {}

for hNames in hNameList:
    heroDict = {hNames:{'maps':[],'cBy':[]}}

    res = requests.get('https://www.icy-veins.com/heroes/'+hNames+'-build-guide')
    res.raise_for_status()
    linkSoup = bs4.BeautifulSoup(res.text,"lxml")

    divEle = linkSoup.select("div.heroes_tldr_maps_stronger > span > img")
    mapsList = []
    for imgEle in divEle:
        maps = imgEle["alt"]
        mapsList.append(maps)

    divEle2 = linkSoup.select("div.heroes_tldr_matchups_hero_list > a > img")
    cHeroList = []
    for imgEle in divEle2:
        cHeroes = imgEle["data-heroes-tooltip"]
        cHeroes = cHeroes[5:]
        cHeroList.append(cHeroes)

    heroDict[hNames]['maps'] = mapsList
    heroDict[hNames]['cBy'] = cHeroList
    allHeroDict.update(heroDict)

print(allHeroDict)