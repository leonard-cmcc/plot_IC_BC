#!/usr/bin/python3  # shabang to invoke python in a local system
# Loading of libraries
import matplotlib
matplotlib.use('Agg')
import matplotlib.dates as mdates
import pandas as pd
import numpy as np
import pdb # import the python debugger
from datetime import datetime, timedelta
from matplotlib import pylab as pl 
import traceback
import matplotlib.pyplot as plt

def plot_bc(variable,timevariable,variablename,pathnamefig):  # define the function plot_bc for bc entry variable timevariable ariablename pathnamefig (same as plot_ic)
        if variablename == 'saltn':
                variablelegend = 'salinity [psu]'
                ylim1 = 36
                ylim2 = 40
        elif variablename == 'tempn':
                variablelegend = 'temperature [C]'
                ylim1 = 8
                ylim2 = 16
        elif variablename == 'U3d':
                variablelegend = 'u-velocity [m/s]'
                ylim1 = -0.3
                ylim2 = 0.3

        elif variablename == 'V3d':
                variablelegend = 'v-velocity [m/s]'
                ylim1 = -0.3
                ylim2 = 0.3

        elif variablename == 'UV3d':
                variablelegend = 'uv-velocity [m/s]'
                ylim1 = -0.3
                ylim2 = 0.3

        #indb = [0,20,40,60,80,100,111]
        indb = [0,20,40,60,90]  # create a list of 5 integers points
        fig = pl.figure(figsize=(12,16)) # plot size
        ax = fig.add_subplot(611) # 1st plot
        ax2 = fig.add_subplot(612)
        ax3 = fig.add_subplot(613)
        ax4 = fig.add_subplot(614)
        ax5 = fig.add_subplot(615)
        ax6 = fig.add_subplot(616) # 6th  plot


        if (variablename == 'U3d') | (variablename == 'V3d'):  # check if variablename is equal to string U3d and V3d
                ax.set_title('BC FILE = uv3d.dat (Level = 0)',fontsize=18,weight='bold')  # set title
        else:
                ax.set_title('BC FILE = ' + variablename + '.dat (Level = 0)',fontsize=18,weight='bold') # set title of the 1st plot
        ax.plot(timevariable,variable[0,indb[0],:],'o', color='blue', linewidth=1.5, label='P1')
        ax.plot(timevariable,variable[0,indb[1],:],'o', color='cyan', linewidth=1.5, label='P2')
        ax.plot(timevariable,variable[0,indb[2],:],'o', color='black', linewidth=1.5, label='P3')
        ax.plot(timevariable,variable[0,indb[3],:],'o', color='skyblue', linewidth=1.5, label='P4')
        ax.plot(timevariable,variable[0,indb[4],:],'o', color='blueviolet', linewidth=1.5, label='P5')

        ax.set_ylabel(variablelegend, fontsize=16)
        ax.set_ylim([ylim1,ylim2])
        ax.legend()
        ax.tick_params(axis='both', labelsize=14)
        ax.grid()   # add grid

        if (variablename == 'U3d') | (variablename == 'V3d'):
                ax2.set_title('BC FILE = uv3d.dat (Level = 10)',fontsize=18,weight='bold')
        else:
                ax2.set_title('BC FILE = ' + variablename + '.dat (Level = 10)',fontsize=18,weight='bold')
        ax2.plot(timevariable,variable[10,indb[0],:],'o', color='blue', linewidth=1.5, label='P1')
        ax2.plot(timevariable,variable[10,indb[1],:],'o', color='cyan', linewidth=1.5, label='P2')
        ax2.plot(timevariable,variable[10,indb[2],:],'o', color='black', linewidth=1.5, label='P3')
        ax2.plot(timevariable,variable[10,indb[3],:],'o', color='skyblue', linewidth=1.5, label='P4')
        ax2.plot(timevariable,variable[10,indb[4],:],'o', color='blueviolet', linewidth=1.5, label='P5')

        ax2.set_ylabel(variablelegend, fontsize=16)
        ax2.set_ylim([ylim1,ylim2])
        ax2.grid()
        ax2.tick_params(axis='both', labelsize=14)

        if (variablename == 'U3d') | (variablename == 'V3d'):
                ax3.set_title('INPUT FILE = uv3d.dat (nlevel = 15)',fontsize=18,weight='bold')
        else:
                ax3.set_title('INPUT FILE = ' + variablename + '_1_?.dat (nlevel = 15)',fontsize=18,weight='bold')
        ax3.plot(timevariable,variable[15,indb[0],:],'o', color='blue', linewidth=1.5, label='P1')
        ax3.plot(timevariable,variable[15,indb[1],:],'o', color='cyan', linewidth=1.5, label='P2')
        ax3.plot(timevariable,variable[15,indb[2],:],'o', color='thistle', linewidth=1.5, label='P3')
        ax3.plot(timevariable,variable[15,indb[3],:],'o', color='skyblue', linewidth=1.5, label='P4')
        ax3.plot(timevariable,variable[15,indb[4],:],'o', color='blueviolet', linewidth=1.5, label='P5')

        ax3.set_ylabel(variablelegend, fontsize=16)
        ax3.set_ylim([ylim1,ylim2])
        ax3.grid()
        ax3.tick_params(axis='both', labelsize=14)

        if (variablename == 'U3d') | (variablename == 'V3d'):
        
                ax4.set_title('BC FILE = uv3d.dat (Level = 20)',fontsize=18,weight='bold')
        else:
                ax4.set_title('BC FILE = ' + variablename + '.dat (Level = 20)',fontsize=18,weight='bold')
        ax4.plot(timevariable,variable[20,indb[0],:],'o', color='blue', linewidth=1.5, label='P1')
        ax4.plot(timevariable,variable[20,indb[1],:],'o', color='cyan', linewidth=1.5, label='P2')
        ax4.plot(timevariable,variable[20,indb[2],:],'o', color='black', linewidth=1.5, label='P3')
        ax4.plot(timevariable,variable[20,indb[3],:],'o', color='skyblue', linewidth=1.5, label='P4')
        ax4.plot(timevariable,variable[20,indb[4],:],'o', color='blueviolet', linewidth=1.5, label='P5')

        ax4.set_ylabel(variablelegend, fontsize=16)
        ax4.set_ylim([ylim1,ylim2])
        ax4.grid()
        ax4.tick_params(axis='both', labelsize=14)

        if (variablename == 'U3d') | (variablename == 'V3d'):
                ax5.set_title('BC FILE = uv3d.dat (Level = 30)',fontsize=18,weight='bold')
        else:
                ax5.set_title('BC FILE = ' + variablename + '.dat (Level = 30)',fontsize=18,weight='bold')
        ax5.plot(timevariable,variable[30,indb[0],:],'o', color='blue', linewidth=1.5, label='P1')
        ax5.plot(timevariable,variable[30,indb[1],:],'o', color='cyan', linewidth=1.5, label='P2')
        ax5.plot(timevariable,variable[30,indb[2],:],'o', color='black', linewidth=1.5, label='P3')
        ax5.plot(timevariable,variable[30,indb[3],:],'o', color='skyblue', linewidth=1.5, label='P4')
        ax5.plot(timevariable,variable[30,indb[4],:],'o', color='blueviolet', linewidth=1.5, label='P5')

        ax5.set_ylabel(variablelegend, fontsize=16)
        ax5.set_ylim([ylim1,ylim2])
        ax5.grid()
        ax5.tick_params(axis='both', labelsize=14)

        if (variablename == 'U3d') | (variablename == 'V3d'):
                ax6.set_title('BC FILE = uv3d.dat (Level = 40)',fontsize=18,weight='bold')
        else:
        
              ax6.set_title('BC FILE = ' + variablename + '.dat (Level = 40)',fontsize=18,weight='bold')
        ax6.plot(timevariable,variable[40,indb[0],:],'o', color='blue', linewidth=1.5, label='P1')
        ax6.plot(timevariable,variable[40,indb[1],:],'o', color='cyan', linewidth=1.5, label='P2')
        ax6.plot(timevariable,variable[40,indb[2],:],'o', color='black', linewidth=1.5, label='P3')
        ax6.plot(timevariable,variable[40,indb[3],:],'o', color='skyblue', linewidth=1.5, label='P4')
        ax6.plot(timevariable,variable[40,indb[4],:],'o', color='blueviolet', linewidth=1.5, label='P5')

        ax6.set_ylabel(variablelegend, fontsize=16)
        ax6.set_ylim([ylim1,ylim2])
        ax6.grid()
        ax6.tick_params(axis='both', labelsize=14)

        pl.tight_layout()  # prevent the plot to ovarlap
        pl.savefig(pathnamefig+'plot_input_' + variablename + '.png', dpi=300, facecolor='w', edgecolor='w',
                orientation='portrait', transparent=False, bbox_inches='tight', pad_inches=0.1) # save figures
        pl.close()  # close plot
        
######################################################################################
#
# MAIN
#
######################################################################################

if __name__ == "__main__":

    print("MAIN --- Starting...")
        
    # change here when needed!
    pathname = '.../output/48chunks/'  # input path
    pathnamefig = '.../figures/48_chunks/' # fig path

    #saltin file
    nk= 48 # number of chunks
    npp= 42517  # Number of points
    nl= 22      # Number of Levels   
    
        
        ######################################################################################
        #
        # 1. BOUNDARY CONDITIONS
        #
        ######################################################################################

# Initialize empty arrays for time and data
timeboundn = np.array([], dtype='datetime64[s]')
boundn = None

# Loop over each chunk file
for c in range(1, nk + 1):   # nk is the number of chunks
    print(f"MAIN --- BC --- iteration {c}")
    
    # Open the file
    with open(pathname + 'boundn_1_' + str(c) + '.dat') as f_boundn:
        content = f_boundn.readlines()
    
    # Initialize counters
    count1boundn = 0
    count2boundn = count1boundn + 103  # Number of lines per data block
    
    # Process each block within the file
    while count2boundn <= len(content):
        # Extract the block content
        tmp = content[count1boundn:count2boundn]
        
        # Extract the date and convert it to datetime format
        date_str = tmp[1].strip()  # Extract date string from the second line
        date = datetime.strptime(date_str, '%Y%m%d %H%M%S')
        timeboundn = np.append(timeboundn, date)
        
        # Extract data values if block contains "water level"
        if tmp[2].startswith(' water level'):
            N = int(tmp[0][11:14])  # Total number of grid nodes
            boundntmp = tmp[3:]  # Get all lines containing data values
            
            # Initialize a temporary array for this block’s data
            boundn1 = np.zeros(N)
            for n in range(N):
                boundn1[n] = float(boundntmp[n].strip())
                
            # Stack data along the time dimension
            if boundn is None:
                boundn = boundn1[np.newaxis, :]  # First time, set initial shape
            else:
                boundn = np.vstack((boundn, boundn1[np.newaxis, :]))

        # Update counters to move to the next block
        count1boundn += 103
        count2boundn = count1boundn + 103

# Sort time and boundn arrays by the time array
sorted_indices = np.argsort(timeboundn) # returns an array of indices that would arrange timeboundn in ascending order
timeboundn = timeboundn[sorted_indices]
boundn = boundn[sorted_indices]  # Sort `boundn` along the same order as `timeboundn`
# `timeboundn` and `boundn` are now sorted by date in chronological order

                
####################################################################################################################################################
indb = [0,20,40,60,90]  # create a list of 5 integers nodes
fig = pl.figure(figsize=(12,8))
ax = fig.add_subplot(111)
print('boundn=',boundn.shape)

ax.set_title('INPUT FILE = boundn.dat (nlevel = 0)',fontsize=18,weight='bold')
ax.plot(timeboundn,boundn[:,indb[0]],'-', color='blue', linewidth=1,label='P1(First node)')
ax.plot(timeboundn,boundn[:,indb[1]],'-', color='cyan', linewidth=1,label='P2(20 nodes)')
ax.plot(timeboundn,boundn[:,indb[2]],'-', linewidth=1, color='black', label='P3(40 nodes)')
ax.plot(timeboundn,boundn[:,indb[3]],'-',linewidth=1, color='blueviolet', label='P4(60 nodes)')
ax.plot(timeboundn,boundn[:,indb[4]],'-',linewidth=1, color='green', label='P5(90 nodes)')
ax.set_ylim([-1.2,0.6])
ax.axhline(0, color='black', linestyle='-', linewidth=1)  # Black dashed horizontal line at y=0
#pl.title("PO ESTUARY (WATER LEVEL)")
pl.xlabel("Time")
pl.ylabel("Water Level (m)")

# Display the legend
ax.legend()
pl.grid(True)
pl.savefig(pathnamefig+'plot_input_boundn', dpi=300, facecolor='w', edgecolor='w',
      orientation='portrait', transparent=False, bbox_inches='tight', pad_inches=0.1)
pl.close()

