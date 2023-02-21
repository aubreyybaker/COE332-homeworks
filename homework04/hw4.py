import requests
import xmltodict
from flask import Flask
import math

app = Flask(__name__)

def getData():
    """
    Retrieves the data from the NASA URL as an XML and returns it as a dictionary.

    Args:
        N/A

    Returns:
        Data (dict): Positional and velocity data for the International Space Station (ISS)
    """
    url='https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml'
    response = requests.get(url)
    data = xmltodict.parse(response.text)
    #data = xmltodict.parse(response.text, attr_prefix='', cdata_key='')
    return data

def getEpochInfo(epoch,data):
    """
    Retrieves the position and velocity data of a certain epoch from the NASA ISS trajectory data.

    Args:
        epoch (str): A moment in time used as a reference point for some time-varying astronomical quantity -- positional and velocity data for the ISS
        data (dict): IMPORTANT - must be retrieved using getData function. Positional and velocity data for the International Space Station (ISS)

    Returns:
        StateVec (dict): Returns position in the X, Y, Z directions as a dictionary
    """
    for epoch in data['ndm']['oem']['body']['segment']['data']['stateVector']:
        X = epoch['X']
        Y = epoch['Y']
        Z = epoch['Z']
        X_dot = epoch['X_DOT']
        Y_dot = epoch['Y_DOT']
        Z_dot = epoch['Z_DOT']

        #speed = {'Speed': {'#text': math.sqrt((x_dot**2)+(y_dot**2)+(z_dot**2)), '@units': 'km/s'}}
        stateVec = {'StateVector': {'X':X, 'Y':Y, 'Z':Z, 'X_DOT':X_dot, 'Y_DOT':Y_dot, 'Z_DOT':Z_dot}}
    return stateVec

@app.route('/', methods=['GET'])
def showData():
    """
    Displays all of the data in the data set from the NASA ISS trajectory data

    Args:
        N/A
    Returns:
        getData (dict): Returns all data within the data set from the NASA ISS trajectory data as a list of dictionaries
    """
    return getData()

@app.route('/epochs', methods=['GET'])
def showEpochs():
    """
    Retrieves all of the epochs in the data set from the NASA ISS trajectory data

    Args:
        N/A
    Returns:
        epochs (list): Returns all epochs within the data set from the NASA ISS trajectory data as a list
    """    
    data = getData()
    epochs = []
    for x in data['ndm']['oem']['body']['segment']['data']['stateVector']:
        epochs.append(x['EPOCH'])
    return epochs

@app.route('/epochs/<epoch>', methods=['GET'])
def showStateVectors(epoch):
    """
    Retrieves the position and velocity data of a certain epoch from the NASA ISS trajectory data by using the getEpochInfo function.

    Args:
        epoch (str): A moment in time used as a reference point for some time-varying astronomical quantity -- positional and velocity data for the ISS
    Returns:
        StateVec (dict): Returns position in the X, Y, Z directions as a dictionary
    """
    data = getData()
    stateVec = getEpochInfo(epoch,data)
    return stateVec

@app.route('/epochs/<epoch>/speed', methods=['GET'])
def showSpeed(epoch):
    """
    Calculates the speed of the ISS at a given epoch with a x, y, and z velocity. 

    Args:
        epoch (str): A moment in time used as a reference point for some time-varying astronomical quantity -- positional and velocity data for the ISS
    Returns:
        speed (float): Returns the speed of the ISS from Cartesian velocity vectors
    """
    data = getData()
    stateVec = getEpochInfo(epoch,data)
    x_dot = float(stateVec['StateVector']['X_DOT']['#text'])
    y_dot = float(stateVec['StateVector']['Y_DOT']['#text'])
    z_dot = float(stateVec['StateVector']['Z_DOT']['#text'])
    speed = {'Speed': {'#text': math.sqrt((x_dot**2)+(y_dot**2)+(z_dot**2)), '@units': 'km/s'}}
    return speed
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')