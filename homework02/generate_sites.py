# need random number between 10-18 degrees North
# and longitudes between 82.0 - 84.0 degrees East in decimal notation
# random ["stony", "iron", "stony-iron"]

import random
import json

landSite = {} #dict
landSite['sites'] = []

def createLandingSite(numSites, landSite):
    compList = ["stony", "iron", "stony-iron"]
    northDeg = round(float(random.uniform(16.0,18.0)),1)
    eastDeg = round(float(random.uniform(82.0,84.0)),1)
    meteoriteComp = random.choice(compList)
    landSite['sites'].append( {'site_id': numSites, 'latitude':northDeg, 'longitude':eastDeg, 'composition':meteoriteComp})
    return landSite

for numSites in range(5):
    data = createLandingSite(numSites+1, landSite)

print(data)
with open('sites.json', 'w') as out:
    json.dump(data, out, indent=2)