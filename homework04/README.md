# ISS Trajectory Information

The purpose of this project is to query and return interesting information from the ISS data set provided by NASA. The project has the ability to retrieve all of the information within the Orbit Ephemeris Message dataset, **just** the ephochs, the state vector a specific epoch, and the speed of the identified epoch. At the altitude of the International Space Station (ISS), a sparse atmosphere still exists, which generates resistance that can gradually lead to errors in its anticipated trajectory. To mitigate this, orbital mechanics update the projected trajectory to get the most precise estimation possible. Maintaining accurate trajectory calculations is critical for establishing communication links, scheduling rendezvous with visiting spacecraft, and ensuring the ISS's path remains unobstructed by potential collisions.

## Retrieve Data

The user may view the website that the ISS trajectory data comes from using the link below:

```bash
https://spotthestation.nasa.gov/trajectory_data.cfm
```
The data can be downloaded in ``TXT`` or ``XML`` format. The saved data looks like the following: 

```bash
...
<data>
  <stateVector>
        <EPOCH>2023-048T12:00:00.000Z</EPOCH>
        <X units="km">-5097.51711371908</X>
        <Y units="km">1610.3574036042901</Y>
        <Z units="km">-4194.4848049601396</Z>
        <X_DOT units="km/s">-4.5815461024513304</X_DOT>
        <Y_DOT units="km/s">-4.8951801207083303</Y_DOT>
        <Z_DOT units="km/s">3.70067961081915</Z_DOT>
    </stateVector>
    <stateVector>
        <EPOCH>2023-048T12:04:00.000Z</EPOCH>
        <X units="km">-5998.4652356788401</X>
        <Y units="km">391.26194859011099</Y>
        <Z units="km">-3164.26047476555</Z>
        <X_DOT units="km/s">-2.8799691318087701</X_DOT>
        <Y_DOT units="km/s">-5.2020406581448801</Y_DOT>
        <Z_DOT units="km/s">4.8323394499086101</Z_DOT>
    </stateVector>
    ... etc
```
For this project, the data is downloaded in XML format.

## Installation

Install this project by cloning the repository, making the scripts executable, and adding them to
your PATH. For example:


```bash
git clone ssh://git@github.com:alb6443/COE332-homeworks.git <directory>
```

## Understanding the Scripts

This code has one script-- ``iss_tracker.py`` 

**``iss_tracker.py``**: This script is a Flask application that has four routes: ``/``, ``/epochs``, ``/epochs/<epoch>``, ``/epochs/<epoch>/speed``. In addition the Flask application utilizes two functions outside of the routes: ``getData`` and ``getEpochInfo``. The functions and routes are explained in further detail below:

## Functions
**``getData()``**: This function is designed to retrieve the data from the NASA URL as an XML and returns it as a list of dictionaries. All routes will require the use of this funtion.

**``getEpochInfo(epoch,data)``**: This function is designed to retrieve the position and velocity state vector of a certain epoch from the NASA ISS trajectory data. The input variable ``epoch`` must be in the format:
```
2023-063T11:23:00.000Z
```
The variable ``data`` can be created using ``getData()``. Once ``data`` is produced, the user will be able to see a key called ``EPOCH``-- this is the value that can be input into the function.

## Flask Application Routes

| **Route**                 | **What it returns**                                                       | Example Output                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|---------------------------|---------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ``/``                     | The entire data set                                                       | ``` ...{                 "EPOCH": "2023-063T09:43:00.000Z",                 "X": {                   "#text": "-3499.0919157778098",                   "@units": "km"                 },                 "X_DOT": {                   "#text": "-4.4852130542234603",                   "@units": "km/s"                 },                 "Y": {                   "#text": "5758.3645262524497",                   "@units": "km"                 },                 "Y_DOT": {                   "#text": "-1.8288811936459901",                   "@units": "km/s"                 },                 "Z": {                   "#text": "-880.78647118498498",                   "@units": "km"                 },                 "Z_DOT": {                   "#text": "5.9371088431915604",                   "@units": "km/s"                 }               },  ``` |
| ``/epochs``               | A list of all Epochs in the data set                                      | ``` ... "2023-063T11:31:00.000Z",   "2023-063T11:35:00.000Z",   "2023-063T11:39:00.000Z",   "2023-063T11:43:00.000Z",   "2023-063T11:47:00.000Z",   "2023-063T11:51:00.000Z",   "2023-063T11:55:00.000Z",   "2023-063T11:59:00.000Z",   "2023-063T12:00:00.000Z"... ```                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ``/epochs/<epoch>``       | State vectors for a specific Epoch from the data set                      | ``` {   "StateVector": {     "X": {       "#text": "2820.04422055639",       "@units": "km"     },     "X_DOT": {       "#text": "5.0375825820999403",       "@units": "km/s"     },     "Y": {       "#text": "-5957.89709645725",       "@units": "km"     },     "Y_DOT": {       "#text": "0.78494316057540003",       "@units": "km/s"     },     "Z": {       "#text": "1652.0698653803699",       "@units": "km"     },     "Z_DOT": {       "#text": "-5.7191913150960803",       "@units": "km/s"     }   } }  ```                                                                                                                                                                                                                                                                                                                                                    |
| ``/epochs/<epoch>/speed`` | Instantaneous speed for a specific Epoch in the data set (math required!) | ``` {   "Speed": {     "#text": 7.661757196327827,     "@units": "km/s"   } }  ```                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

