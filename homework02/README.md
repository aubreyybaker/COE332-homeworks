# Mars Rover Exploring Meteorite Landings

The purpose of this project is to produce 5 meteorite landing sites on Mars and calculate the amount of time it will take a mars rover to explore each site, sample the area, and the total elapsed time after all meteorite sites have been explored. Mars rovers are critical to better understand the planet's geology, climate and potential habitability and advance our knowledge of the origins and evolution of the solar system.


## Installation

Install this project by cloning the repository, making the scripts executable, and adding them to
your PATH. For example:


```bash
git clone ssh://git@github.com:alb6443/COE332-homeworks.git <directory>
```

## Understanding the Scripts

This code has two scripts: ``generate_sites.py`` and ``calculate_trip.py``

**``generate_sites.py``**: **RUN THIS FILE FIRST!** Produces 5 random meteorite landing sites between 16.0 - 18.0 degrees North and longitudes between 82.0 - 84.0 degrees East. Each landing site has a randomly chosen composition of any of the following: stony, iron, and stony-iron. All of the meteorite landing data is then saved to a JSON file titled ``meteoriteSites.json`` in the same directrory as ``generate_sites.py`` and ``calculate_trip.py``. For example, the data structure will look like:

```bash
 {
      "sites": [
        {
          "site_id": 1,
          "latitude": 17.93705170143149,
          "longitude": 83.36448444826725,
          "composition": "stony"
        },
        {
          "site_id": 2,
          "latitude": 16.714833623042153,
          "longitude": 82.84554246756586,
          "composition": "iron"
        },
    ... etc
```

**``calculate_trip``**: **WILL NOT RUN UNLESS ``generate_sites.py`` HAS BEEN EXECUTED!** Calculates the time required to visit and take samples from the five sites produced in ``meteoriteSites.json`` in order. The robot travels at a speed of 10 km/hr. The time it takes to travel is found by using the great-circle distance algorithm. The rover will spend ``1 hour`` sampling stony meteorites, ``2 hours`` sampling iron meteorites, and ``3 hours`` to sampling stony-iron meteorites. Each leg of the trip is described and a summary of the whole trip will look similar to:

```bash
leg = 1, time to travel = 11.75 hr, time to sample = 1 hr
leg = 2, time to travel = 3.43 hr, time to sample = 2 hr
leg = 3, time to travel = 4.53 hr, time to sample = 1 hr
leg = 4, time to travel = 6.04 hr, time to sample = 2 hr
leg = 5, time to travel = 10.43 hr, time to sample = 3 hr
===============================
number of legs = 5, total time elapsed = 45.17 hr
```
