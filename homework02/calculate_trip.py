# robot starts at latitude / longitude {16.0, 82.0}
# robot visits the five sites in the order of the list index
# max robot speed is 10 km/hr
# Mars is a sphere (radius = 3389.5 km) and use the great-circle
# distance algorithm to calculate distance between points
# Stony meteorites = 1 hour
# iron meteorites = 2 hours
# stony-iron meteorites = 3 hours

import json
import math
from typing import List

with open('meteoriteSites.json','r') as f:
    site_data = json.load(f)

robotStartLat = 16.0    #deg
robotStartLon = 82.0    # deg
robotSpeed = 10 # km/hr
mars_radius = 3389.5    # km
sampleTimes = {'stony':1, 'iron':2, 'stony-iron':3}
elapsedTime = 0

def calc_gcd(latitude_1: float, longitude_1: float, latitude_2: float, longitude_2: float) -> float:
    lat1, lon1, lat2, lon2 = map( math.radians, [latitude_1, longitude_1, latitude_2, longitude_2] )
    d_sigma = math.acos( math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(abs(lon1-lon2)))
    return ( mars_radius * d_sigma )

def count_classes(a_list_of_dicts: List[dict], a_key_string: str):
    classes_observed = {}
    for item in a_list_of_dicts:
        if item[a_key_string] in classes_observed:
            classes_observed[item[a_key_string]] += 1
        else:
            classes_observed[item[a_key_string]] = 1
    return(classes_observed)

num_of_classes = count_classes(site_data['sites'], 'site_id')

for i in range(len(num_of_classes)):
    latitude_2 = site_data['sites'][i]['latitude']
    longitude_2 = site_data['sites'][i]['longitude']

    dist = calc_gcd(robotStartLat, robotStartLon, latitude_2, longitude_2)
    travelTime = round(float(dist/robotSpeed),2)
    elapsedTime += travelTime

    meteoriteComp = site_data['sites'][i]['composition']
    sampleTime = int(sampleTimes[meteoriteComp])

    elapsedTime += sampleTime

    print('leg = ', i+1, ', time to travel = ', travelTime, ', time to sample = ', sampleTime,'hr',sep = '')

print('===============================')
print('number of legs = ', i+1, ', total time elapsed = ', elapsedTime, ' hr', sep = '')
