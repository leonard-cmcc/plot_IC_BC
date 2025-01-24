# plot IC BC 
The script plot_IC_BC_po.py is useful to plot the initial, boundary conditions and atmospheric .dat files from shyfem pre-processing while plot_boundn_BC_po.py plot the water level. In the meantime, plot_runoff_BC.py and temp_river_flow.py alow to visualise the river runoff and the river flow temperature respectively. As described in each script you have to edit each block of the code according to your .dat file



## Setting up the environment
To use the scripts of this repository you need to install some packages meanwhile you to create a conda environment and install the dependences as following example:

```
$conda create --name env_plot
```


Activate the environment with 

```
$conda activate env_plot
```

## install the needed dependencies


```
import matplotlib
matplotlib.use('Agg')
import matplotlib.dates as mdates
import pandas as pd
import numpy as np
import pdb # import the python debugger
from datetime import datetime, timedelta
from matplotlib import pylab as pl 
import traceback
import subprocess
import matplotlib.pyplot as plt
#from fem_tools import *
import sys, os
import re
from netCDF4 import Dataset

```

## Plot the initial, boundary conditions and the atmospheric fields for the surface 
Edit the output and figure path in plot_IC_BC_po.py according to your directory as well as each block of variable in the script. When it done, you can run the script:


```
$python plot_IC_BC_po.py
```


### plot the water level 
Edit the output and the figure path before run the script as following:


```
$python plot_boundn_BC_po.py
```

### plot the river runoff
Update the file path and the figure path and run the code


```
$python plot_runoff_BC.py
```

### plot the river flow temperature


```
$python temp_river_flow.py
```

### plot shyfem partitioning
To run the script provide the path of shyfem netcdf unstructured output and the path of partitioning file

```
$python show_part3.py .../output.nc .../part_elems144
```
