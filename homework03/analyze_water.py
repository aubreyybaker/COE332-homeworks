#(1) the current water turbidity (taken as the average of the most recent five data points)
#(2) whether that turbidity is below a safe threshold
#(3) the minimum time required for turbidity to fall below the safe threshold (if it is 
# already below the safe threshold, the script would report “0 hours” or similar).

import requests
import json
from datetime import datetime
import math

def turbitityCalculation(I90: float, a0: float) -> float:
    """
    Calculates the turbitiy of a singular water sample. Returns the turbitiy value.

    Args:
        I90 (float): The 90 degree detector current for the specific water sample as a float.
        a0 (float): The calibration constant for the specific water sample as a float.

    Returns:
        T (float): turbidity in NTU unites (0-40) as a float
    """
    T = a0 * I90
    return T

def turbThreshold(T0: float,Ts: float) -> float:
    """
    Calculates the minimum time to return below a safe threshold. Returns the value as a float.

    Args:
        T0 (float): Current turbidity for the 5 most recent water samples as a float.
        Ts (float): Turbidity threshold for safe water as a float.

    Returns:
        b (float): hours elapsedin hours as a float
    """
    d = 0.02
    b = (math.log(Ts/T0))/(math.log(1-d))
    return b


def main():
    url = 'https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json'
    data = requests.get(url)
    turbData = data.json()
    #print(turbData)

    sorted_date = sorted(turbData['turbidity_data'], key=lambda x: datetime.strptime(x['datetime'], '%Y-%m-%d %H:%M'))
    turbSorted = json.dumps(sorted_date)
   
    turb = []
    for x in sorted_date[-5:]:
        detectCurr = x['detector_current']
        calibConst = x['calibration_constant']
        turb.append(turbitityCalculation(detectCurr, calibConst))
    
    Ts = 1.0
    T0 = round(sum(turb)/len(turb),4)
    print('Average turbidity based on most recent five measurements = ', T0, ' NTU')
    
    if (T0>Ts):
        print('Warning: Turbidity is above threshold for safe use')
        b = round(turbThreshold(T0,Ts),4)
        print('Minimum time required to return below a safe threshold = ', b, ' hours')

    else:
        print('Info: Turbidity is below threshold for safe use')
        print('Minimum time required to return below a safe threshold = 0 hours')

    

if __name__ == '__main__':
    main()


