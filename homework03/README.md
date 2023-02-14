# Mars Water Sample Analysis

The purpose of this project is to read the water quality information and calculate the current water turbidity, whether or not the threshold is below a safe threshold, and the minimum time required for turbidity to fall below the safe threshold. Water on Mars is important because it is a key ingredient for life as we know it, and its presence on the planet could support the possibility of past or present microbial life. Additionally, water can be used as a resource for human exploration and potential future colonization of the planet. 

## Retrieve Data

The user may access the raw water sample turbidity data from the link below:

```bash
https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json
```
Each dictionary in the list has the same set of keys. A sample of the data looks like:

```bash
{
  "turbidity_data": [
    {
      "datetime": "2023-02-01 00:00",
      "sample_volume": 1.19,
      "calibration_constant": 1.022,
      "detector_current": 1.137,
      "analyzed_by": "C. Milligan"
    },
    {
      "datetime": "2023-02-01 01:00",
      "sample_volume": 1.15,
      "calibration_constant": 0.975,
      "detector_current": 1.141,
      "analyzed_by": "C. Milligan"
    },
    ... etc
```

## Installation

Install this project by cloning the repository, making the scripts executable, and adding them to
your PATH. For example:


```bash
git clone ssh://git@github.com:alb6443/COE332-homeworks.git <directory>
```

## Understanding the Scripts

This code has two scripts: ``analyze_water.py`` and ``test_analyze_water.py``

**``analyze_water.py``**: Determines whether or not the 5 most recent water sample average turbidity is safe or a hazard. The script calculates turbidity in NTU units (0-40). In addition, it calculates the minimum number of hours required to fall below the safe threshold turbidity of 1.0 NTU. When the script is run, a summary of the whole trip will look similar to:

.. code-block:: text

   Average turbidity based on most recent five measurements = 1.1992 NTU
   Warning: Turbidity is above threshold for safe use
   Minimum time required to return below a safe threshold = 8.99 hours

.. code-block:: text

   Average turbidity based on most recent five measurements = 0.9852 NTU
   Info: Turbidity is below threshold for safe use
   Minimum time required to return below a safe threshold = 0 hoursum time required to return below a safe threshold = 0 hours
```

**``test_analyze_water.py``**: This script is designed to test the ``turbitityCalculation`` and ``turbThreshold`` functions within  ``analyze_water.py``. This demonstrates that the functions work as they are expected to. The script asserts the functions by passing hand-crafted data that results in an already-known answer for both functions. 

Before calling pytest, ensure that ``pytest`` is installed. 
```bash
pip3 install --user pytest # installs pytest
pytest --version # check the installation
```
Call the ``pytest`` executable in your top directory, it will find the test functions in the test script, run the functions, and  print some informative output:

```bash
==================================== test session starts ====================================
platform linux -- Python 3.6.8, pytest-7.0.0, pluggy-1.0.0
rootdir: /home/wallen/coe-332/code-organization
collected 1 item

test_ml_data_analysis.py .                                                            [100%]

===================================== 1 passed in 0.01s =====================================
```
