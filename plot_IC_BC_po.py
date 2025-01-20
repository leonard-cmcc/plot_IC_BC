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

# IC plots
def plot_ic(variable,timevariable,variablename,pathnamefig):  # define the function plot_ic for initial conditions with entry variable timevariable ariablename pathnamefig
        if variablename == 'saltin':    # check if variablename is equal to string saltin
                variablelegend = 'salinity [psu]' # legend of salinity [psu]
                ylim1 = 30   # 1st y axis at 32
                ylim2 = 40  # 2nd y axis at 40
        elif variablename == 'tempin': # check if variablename is equal to string tempin
                variablelegend = 'temperature [C]' # legend of temperature
                ylim1 = 6 # 1st y axis at 0
                ylim2 = 30 # 2nd y axis at 40
        elif variablename == 'uin': # check if variablename is equal to string uvin
                variablelegend = 'u-velocity [m/s]'  # legend of  u velocity
                ylim1 = -0.3  # 1st y axis at -0.3
                ylim2 = 0.3  # 2nd y axis at 0.3
        elif variablename == 'vin':  # check if variablename is equal to string vin
                variablelegend = 'v-velocity [m/s]'  # legend of v velocity
                ylim1 = -0.3
                ylim2 = 0.3
        elif variablename == 'uvin':  # check if variablename is equal to string vin
                variablelegend = 'uv-velocity [m/s]'  # legend of v velocity
                ylim1 = -0.3
                ylim2 = 0.3

        #indd = [0,1000,10000,20000,30000,40000,46423]
        indd = [0,39590,42151,40582,42000] # create a list of 5 points

        fig = pl.figure(figsize=(12,16))  # figure size
        ax = fig.add_subplot(611) # 1st plot
        ax2 = fig.add_subplot(612) # 2nd
        ax3 = fig.add_subplot(613) # 3rd
        ax4 = fig.add_subplot(614) # 4th
        ax5 = fig.add_subplot(615) # 5th
        ax6 = fig.add_subplot(616) # 6th  
                      
        ax.set_title('INPUT FILE = ' + variablename + '.dat (Level =0, 1.02 m)',fontsize=18,weight='bold')  # set title for the first plot 
        ax.plot(timevariable,variable[:,indd[0],0],'o', color='blue', label='P1(First node)') # create a scatter plot on the axis in Matplotlib
        ax.plot(timevariable,variable[:,indd[1],0],'o', color='cyan', label='P2(39590 nodes)')
        ax.plot(timevariable,variable[:,indd[2],0],'o', color='black', label='P3(42151 nodes)')  
        ax.plot(timevariable,variable[:,indd[3],0],'o', color='red', label='P4(40582 nodes)')
        ax.plot(timevariable,variable[:,indd[4],0],'o', color='blueviolet', label='P5(42000 nodes)')

        ax.set_ylabel(variablelegend, fontsize=16)
        ax.set_ylim([ylim1,ylim2])
        ax.legend()
        ax.tick_params(axis='both', labelsize=14)
        ax.grid()

        ax2.set_title('INPUT FILE = ' + variablename + '.dat (Level =10, 10.5 m)',fontsize=18,weight='bold') # set title for the 2nd plot 
        #ax2.plot(timevariable,variable[:,indd[0],10],'o', color='blue', label='P1')
        ax2.plot(timevariable,variable[:,indd[1],10],'o', color='cyan', label='P2')
        ax2.plot(timevariable,variable[:,indd[2],10],'o', color='black', label='P3')
        ax2.plot(timevariable,variable[:,indd[3],10],'o', color='red', label='P4')
        ax2.plot(timevariable,variable[:,indd[4],10],'o', color='blueviolet', label='P5')

        ax2.set_ylabel(variablelegend, fontsize=16)
        ax2.set_ylim([ylim1,ylim2])
        ax2.grid()
        ax2.tick_params(axis='both', labelsize=14)

        ax3.set_title('INPUT FILE = ' + variablename + '.dat (Level =14, 22.5 m)',fontsize=18,weight='bold') # set title for the 3rd plot
        #ax3.plot(timevariable,variable[:,indd[0],14],'o', color='blue', label='P1')
        ax3.plot(timevariable,variable[:,indd[1],14],'o', color='cyan', label='P2')
        ax3.plot(timevariable,variable[:,indd[2],14],'o', color='black', label='P3')
        ax3.plot(timevariable,variable[:,indd[3],14],'o', color='red', label='P4')
        #ax3.plot(timevariable,variable[:,indd[4],14],'o', color='blueviolet', label='P5')

        ax3.set_ylabel(variablelegend, fontsize=16)
        ax3.set_ylim([ylim1,ylim2])
        ax3.grid()
        ax3.tick_params(axis='both', labelsize=14)

        ax4.set_title('INPUT FILE = ' + variablename + '.dat (Level =17, 32 m)',fontsize=18,weight='bold') # set title for the 4th plot 
        #ax4.plot(timevariable,variable[:,indd[0],17],'o', color='blue', label='P1')
        ax4.plot(timevariable,variable[:,indd[1],17],'o', color='cyan', label='P2')
        ax4.plot(timevariable,variable[:,indd[2],17],'o', color='black', label='P3')
        #ax4.plot(timevariable,variable[:,indd[3],17],'o', color='red', label='P4')
        #ax4.plot(timevariable,variable[:,indd[4],17],'o', color='blueviolet', label='P5')

        ax4.set_ylabel(variablelegend, fontsize=16)
        ax4.set_ylim([ylim1,ylim2])
        ax4.grid()
        ax4.tick_params(axis='both', labelsize=14)

        ax5.set_title('INPUT FILE = ' + variablename + '.dat (Level =19, 38.5 m)',fontsize=18,weight='bold') # set title for the 5th plot
        #ax5.plot(timevariable,variable[:,indd[0],19],'o', color='blue', label='P1')
        ax5.plot(timevariable,variable[:,indd[1],19],'o', color='cyan', label='P2')
        #ax5.plot(timevariable,variable[:,indd[2],19],'o', color='black', label='P3')
        #ax5.plot(timevariable,variable[:,indd[3],19],'o', color='red', label='P4')
        #ax5.plot(timevariable,variable[:,indd[4],19],'o', color='blueviolet', label='P5')

        ax5.set_ylabel(variablelegend, fontsize=16)
        ax5.set_ylim([ylim1,ylim2])
        ax5.grid()
        ax5.tick_params(axis='both', labelsize=14)

        ax6.set_title('INPUT FILE = ' + variablename + '.dat (Level =20, 40 m)',fontsize=18,weight='bold') # set title for the 6th plot
        #ax6.plot(timevariable,variable[:,indd[0],20],'o', color='blue', label='P1')
        ax6.plot(timevariable,variable[:,indd[1],20],'o', color='cyan', label='P2')
        #ax6.plot(timevariable,variable[:,indd[2],20],'o', color='black', label='P3')
        #ax6.plot(timevariable,variable[:,indd[3],20],'o', color='red', label='P4')
        #ax6.plot(timevariable,variable[:,indd[4],20],'o', color='blueviolet', label='P5')

        ax6.set_ylabel(variablelegend, fontsize=16)
        ax6.set_ylim([ylim1,ylim2])
        ax6.grid()
        ax6.tick_params(axis='both', labelsize=14)

        pl.tight_layout() # adjusts the parameters of the subplots to give specified padding and avoid overlapping elements
        pl.savefig(pathnamefig+'plot_input_' + variablename + '.png', dpi=300, facecolor='w', edgecolor='w',
                orientation='portrait', transparent=False, bbox_inches='tight', pad_inches=0.1)  # save different plot
        pl.close()  # close plot mode

def plot_bc(variable,timevariable,variablename,pathnamefig):  # define the function plot_bc for bc entry variable timevariable ariablename pathnamefig (same as plot_ic)
        if variablename == 'saltn':      #sal variable
                variablelegend = 'salinity [psu]' #sal legend
                ylim1 = 30
                ylim2 = 40
        elif variablename == 'tempn':
                variablelegend = 'temperature [C]'
                ylim1 = 6
                ylim2 = 30
                yticks_interval = 1  # Customize temperature tick interval
        elif variablename == 'U3d':
                variablelegend = 'u-velocity [m/s]'
                ylim1 = -0.3
                ylim2 = 0.3

        elif variablename == 'V3d':
                variablelegend = 'v-velocity [m/s]'
                ylim1 = -0.3
                ylim2 = 0.3
                yticks_interval = 0.1  # Customize temperature tick interval

        elif variablename == 'UV3d':
                variablelegend = 'uv-velocity [m/s]'
                ylim1 = -0.3
                ylim2 = 0.3
                yticks_interval = 0.1  # Customize temperature tick interval

        #indb = [0,20,40,60,80,100,111]
        indb = [0,20,40,60,90]  # create a list of 5 nodes
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
                ax.set_title('BC FILE = ' + variablename + '.dat (Level =0, 1.02 m)',fontsize=18,weight='bold') # set title of the 1st plot
        ax.plot(timevariable,variable[0,indb[0],:],'.-', color='blue', label='P1(First node, 2.7506 m)')
        ax.plot(timevariable,variable[0,indb[1],:],'.-', color='cyan', label='P2(20 nodes, 13.009 m)')
        ax.plot(timevariable,variable[0,indb[2],:],'.-', color='black', label='P3(40 nodes, 36.2845 m)')
        ax.plot(timevariable,variable[0,indb[3],:],'.-', color='red', label='P4(60 nodes, 40.5206 m)')
        ax.plot(timevariable,variable[0,indb[4],:],'.-', color='blueviolet', label='P5(90 nodes, 28.8236 m)')

        ax.set_ylabel(variablelegend, fontsize=16)
        #ax.set_ylim([ylim1,ylim2])
        ax.set_ylim([ylim1,ylim2])
        ax.legend()
        ax.tick_params(axis='both', labelsize=14)
        ax.grid()   # add grid

        if (variablename == 'U3d') | (variablename == 'V3d'):
                ax2.set_title('BC FILE = uv3d.dat (Level = 10)',fontsize=18,weight='bold')
        else:
                ax2.set_title('BC FILE = ' + variablename + '.dat (Level =10, 10.5 m)',fontsize=18,weight='bold')
        #ax2.plot(timevariable,variable[10,indb[0],:],'o', color='blue', linewidth=1, label='P1(First node, 2.7506 m)')
        ax2.plot(timevariable,variable[10,indb[1],:],'.-', color='cyan', label='P2(20 nodes, 13.009 m)')
        ax2.plot(timevariable,variable[10,indb[2],:],'.-', color='black', label='P3(40 nodes, 36.2845 m)')
        ax2.plot(timevariable,variable[10,indb[3],:],'.-', color='red', label='P4(60 nodes, 40.5206 m)')
        ax2.plot(timevariable,variable[10,indb[4],:],'.-', color='blueviolet', label='P5(90 nodes, 28.8236 m)')

        ax2.set_ylabel(variablelegend, fontsize=16)
        ax2.set_ylim([ylim1,ylim2])
        ax2.grid()
        ax2.tick_params(axis='both', labelsize=14)

        if (variablename == 'U3d') | (variablename == 'V3d'):
                ax3.set_title('INPUT FILE = uv3d.dat (nlevel = 14)',fontsize=18,weight='bold')
        else:
                ax3.set_title('INPUT FILE = ' + variablename + '.dat (Level =14, 22.5 m)',fontsize=18,weight='bold')
        #ax3.plot(timevariable,variable[14,indb[0],:],'o', color='blue', linewidth=1, label='P1(First node, 2.7506 m)')
        #ax3.plot(timevariable,variable[14,indb[1],:],'o', color='cyan', linewidth=1, label='P2(20 nodes, 13.009 m)')
        ax3.plot(timevariable,variable[14,indb[2],:],'.-', color='black', label='P3(40 nodes, 36.2845 m)')
        ax3.plot(timevariable,variable[14,indb[3],:],'.-', color='red', label='P4(60 nodes, 40.5206 m)')
        ax3.plot(timevariable,variable[14,indb[4],:],'.-', color='blueviolet', label='P5(90 nodes, 28.8236 m)')

        ax3.set_ylabel(variablelegend, fontsize=16)
        ax3.set_ylim([ylim1,ylim2])
        ax3.grid()
        ax3.tick_params(axis='both', labelsize=14)

        if (variablename == 'U3d') | (variablename == 'V3d'):
        
                ax4.set_title('BC FILE = uv3d.dat (Level = 17)',fontsize=18,weight='bold')
        else:
                ax4.set_title('BC FILE = ' + variablename + '.dat (Level =17, 32 m)',fontsize=18,weight='bold')
        #ax4.plot(timevariable,variable[17,indb[0],:],'o', color='blue', linewidth=1, label='P1(First node, 2.7506 m)')
        #ax4.plot(timevariable,variable[17,indb[1],:],'o', color='cyan', linewidth=1, label='P2(20 nodes, 13.009 m)')
        ax4.plot(timevariable,variable[17,indb[2],:],'.-', color='black', label='P3(40 nodes, 36.2845 m)')
        ax4.plot(timevariable,variable[17,indb[3],:],'.-', color='red', label='P4(60 nodes, 40.5206 m)')
        ax4.plot(timevariable,variable[17,indb[4],:],'.-', color='blueviolet', label='P5(90 nodes, 28.8236 m)')

        ax4.set_ylabel(variablelegend, fontsize=16)
        ax4.set_ylim([ylim1,ylim2])
        ax4.grid()
        ax4.tick_params(axis='both', labelsize=14)

        if (variablename == 'U3d') | (variablename == 'V3d'):
                ax5.set_title('BC FILE = uv3d.dat (Level = 19)',fontsize=18,weight='bold')
        else:
                ax5.set_title('BC FILE = ' + variablename + '.dat (Level =19, 38.5 m)',fontsize=18,weight='bold')
        #ax5.plot(timevariable,variable[19,indb[0],:],'o', color='blue', linewidth=1, label='P1(First node, 2.7506 m)')
        #ax5.plot(timevariable,variable[19,indb[1],:],'o', color='cyan', linewidth=1, label='P2(20 nodes, 13.009 m)')
        #ax5.plot(timevariable,variable[19,indb[2],:],'o', color='black', linewidth=1, label='P3(40 nodes, 36.2845 m)')
        ax5.plot(timevariable,variable[19,indb[3],:],'.-', color='red', label='P4(60 nodes, 40.5206 m)')
        #ax5.plot(timevariable,variable[19,indb[4],:],'o', color='blueviolet', linewidth=1, label='P5(90 nodes, 28.8236 m)')

        ax5.set_ylabel(variablelegend, fontsize=16)
        ax5.set_ylim([ylim1,ylim2])
        ax5.grid()
        ax5.tick_params(axis='both', labelsize=14)

        if (variablename == 'U3d') | (variablename == 'V3d'):
                ax6.set_title('BC FILE = uv3d.dat (Level = 20)',fontsize=18,weight='bold')
        else:
        
              ax6.set_title('BC FILE = ' + variablename + '.dat (Level =20, 40 m)',fontsize=18,weight='bold')
        #ax6.plot(timevariable,variable[20,indb[0],:],'o', color='blue', linewidth=1, label='P1(First node, 2.7506 m)')
        #ax6.plot(timevariable,variable[20,indb[1],:],'o', color='cyan', linewidth=1, label='P2(20 nodes, 13.009 m)')
        #ax6.plot(timevariable,variable[20,indb[2],:],'o', color='black', linewidth=1, label='P3(40 nodes, 36.2845 m)')
        ax6.plot(timevariable,variable[20,indb[3],:],'.-', color='red', label='P4(60 nodes, 40.5206 m)')
        #ax6.plot(timevariable,variable[20,indb[4],:],'o', color='blueviolet', linewidth=1, label='P5(90 nodes, 28.8236 m)')

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
    
    print("MAIN --- BC init...")
    
    #tc file
    timetc = np.array([]); lonstc = np.array([]); latstc = np.array([]) # create a empty NumPy array time lon lat for tc
    solarrad = np.array([]) # empty NumPy array for solar radiat store in solarrad
    airtemp = np.array([]) # empty NumPy array for airtemp store in airtemp
    dewptemp = np.array([]) # empty NumPy array for dewpoint store in dewpoint
    cloud = np.array([]) # empty NumPy array for cloud store in cloud
    #wp file
    timewp = np.array([]); lonswp = np.array([]); latswp = np.array([]) # create a empty NumPy array time lon lat for wp
    windu = np.array([])  # empty NumPy array for wind store in windu
    windv = np.array([]) # empty NumPy array for wind store in windv
    pressatm = np.array([]) # empty NumPy array for atms pressure and store in pressatm
    
    timesaltn = np.array([]) # create a empty NumPy array time lon lat for saltinity bc
    timetempn = np.array([]) # create a empty NumPy array time lon lat for temp bc
    timeuv3d = np.array([])      # create a empty NumPy array time lon lat for uv bc
    timeboundn = np.array([]) # create a empty NumPy array time lon lat for bound bc
    
    
    ########
    ## IC ## --- NOTE : this part is also for BC
    ########
    
    print("MAIN --- IC init...")
    
    #saltin file
    nk= 48 # number of chunks
    npp= 42517  # Number of points
    nl= 22      # Number of Levels
    timesaltin = ["" for x in range(nk+1)] #   creates a list called timesaltin contains nk + 1 empty strings
    saltin = np.zeros([nk+1,npp,nl]) #saltin array with dimension [Nchunks,Npoints,Nlevels]
    saltinN1 = np.zeros([nk+1,npp]) # create an empty NumPy array with shape nk + 1 rows and npp columns store in saltinN1
    saltinN2 = np.zeros([nk+1,npp]) # create an empty NumPy array with shape nk + 1 rows and npp columns store in saltinN2
    #tempin file
    timetempin = ["" for x in range(nk+1)]
    tempin = np.zeros([nk+1,npp,nl]) #tempin array with dimension [Nchunks,Npoints,Nlevels]
    tempinN1 = np.zeros([nk+1,npp])
    tempinN2 = np.zeros([nk+1,npp])
    
    #boundin file
    timeboundin = ["" for x in range(nk+1)]
    boundin = np.zeros([nk+1,npp]) #boundin arraywith dimension [Nchunks,Npoints]
    boundinN1 = np.zeros([nk+1,npp])
    boundinN2 = np.zeros([nk+1,npp])
    
    #uin file
    timeUin = ["" for x in range(nk+1)]
    Uin = np.zeros([nk+1,npp,nl]) #Uin matrix with dimension [Nchunks,Npoints,Nlevels]
    UinN1 = np.zeros([nk+1,npp])
    UinN2 = np.zeros([nk+1,npp])
    ##vin file
    timeVin = ["" for x in range(nk+1)]
    Vin = np.zeros([nk+1,npp,nl]) #Vin array with dimension [Nchunks,Npoints,Nlevels]
    VinN1 = np.zeros([nk+1,npp])
    VinN2 = np.zeros([nk+1,npp])
    #uvin file
    timeUVin = ["" for x in range(nk+1)]
    UVin = np.zeros([nk+1,2,npp,nl]) #Vin array with dimension [Nchunks,U/V,Npoints,Nlevels]
    UVinN1 = np.zeros([2,nk+1,npp])
    UVinN2 = np.zeros([2,nk+1,npp])
    
    
        
        ######################################################################################
        #
        # 1. BOUNDARY CONDITIONS
        #
        ######################################################################################
 
    chunk_start_times = [] ### F
    for c in range(1,nk + 1):   #number of chunks
   
        print(f"MAIN --- BC --- iteration {c}")
        
        ## --------------- ##
        ## open tc_* files ##
        ## --------------- ##
        f_tc = open(pathname + 'tc_' + str(c) + '.dat') # open all the tc_dd..dat file
        content = f_tc.readlines()  # read each line of tc open and store in content
    
        # read the content of the file opened with while loop
        count1tc=0   # initialize the content
        count2tc=count1tc+75  # number of lines between the first block(solar radiation,air temperature,dew point temperature,cloud cover) and the next one

        chunkc_added = False ###
        while count2tc <= len(content):   # while loop for count2tc small or eqaual to content
                
                tmp = content[count1tc:count2tc] # gather all the count1tc and count2tc and store as tmp
                date = datetime.strptime(tmp[1:2][0][:-1], '%Y%m%d %H%M%S') # extract a date in a substring from tmp. [0] stand to extract the 1st sublist and -1 to remove the last character from the 
                
                
                ############
                if not chunkc_added: ### 
                        chunk_start_times.append(date) ### 
                        chunkc_added = True ### 
                else:
                        chunk_start_times.append(None) ### 
                ###################
                
                
                N1 = int(tmp[2][0:2]) # extract index=2 stand for number of rows
                N2 = int(tmp[2][3:5]) # extract index=2 of tmp for number of column
                lon1 = np.round(float(tmp[2][6:10]),2)  # extract a longitude from the string located at index 2 convert substring to a float
                lat1 = np.round(float(tmp[2][25:29]),2) # extract a latitude from the string located at index 2 convert substring to a float
                dx = np.round(float(tmp[2][29:35]),2) # extract dx from the string located at index 2 convert substring to a float
                dy = np.round(float(tmp[2][49:55]),2) # extract dy from the string located at index 2 convert substring to a float
                lons1 = np.arange(lon1, lon1+(dx*N1), dx)[0:-1] # arange a NumPy array of long within a specified range. lon1 + (dx * N1) calculates the upper bound of the range, dx=distance between consecutive value and slice operation [0:-1] removes the last element from the generated array. N1 an integer representing the number of steps
                lats1 = np.arange(lat1, lat1+(dy*N2), dy) #  same as lons1
    
                try:   # block in case it fails
                        lonstc = np.dstack((lonstc, lons1)) # np.dstack() is a function that stacks arrays and takes a tuple of arrays (lonstc, lons1) and combines them along a new third axis store as 
                        latstc = np.dstack((latstc, lats1)) # np.dstack() is a function that stacks arrays and takes a tuple of arrays (latstc, lats1) and combines them along a new third axis store 
                except:
                        lonstc = lons1.copy()
                        latstc = lats1.copy()
    
                timetc = np.append(timetc, date)
                # Ensure timetc is a numpy array of datetime objects if it's not already
                #timetc = np.array(timetc, dtype='datetime64[s]')

                if tmp[3].startswith('solar'):  # start line of solar radiation
                        solarradtmp = tmp[4:21] # select solar radiation lines in tmp (tc.dat)
                        solarrad1 = np.array(np.zeros([N1,N2]))
                        for i in range(0,len(solarradtmp)):
                                res = np.array([float(idx) for idx in solarradtmp[i][0:-1].split(' ')])
                                solarrad1[:,i] = res
    
                        try:
                                solarrad = np.dstack((solarrad, solarrad1))
                        except:
                                solarrad = solarrad1.copy()

                if tmp[21].startswith('air'): # start line of air temp
                         airtemptmp = tmp[22:39] # select air temp from tmp(tc.dat) 
                         airtemp1 = np.array(np.zeros([N1,N2]))
                         for i in range(0,len(airtemptmp)):
                                res = np.array([float(idx) for idx in airtemptmp[i][0:-1].split(' ')])  
                                airtemp1[:,i] = res
                         try:
                       
                               airtemp = np.dstack((airtemp, airtemp1))  # join a sequence of array (airtemp1) along the 3rd axis of airtemp
                         except:
                                airtemp = airtemp1.copy()  # copy of airtemp

                if tmp[39].startswith('dew'): # start line of dew temp
                        dewptemptmp = tmp[40:57] # select dew temp from tmp(tc.dat) 
                        dewptemp1 = np.array(np.zeros([N1,N2]))
                        for i in range(0,len(dewptemptmp)):
                                res = np.array([float(idx) for idx in dewptemptmp[i][0:-1].split(' ')])
                                dewptemp1[:,i] = res
                        try:
                                dewptemp = np.dstack((dewptemp, dewptemp1))
                        except:
                                dewptemp = dewptemp1.copy()
                               
                if tmp[57].startswith('cloud'): # start line of cloud cover
                        cloudtmp = tmp[58:75] # select cloud from tmp
                        cloud1 = np.array(np.zeros([N1,N2]))
                        for i in range(0,len(cloudtmp)):
                                res = np.array([float(idx) for idx in cloudtmp[i][0:-1].split(' ')])
                                cloud1[:,i] = res
                        try:
                                cloud = np.dstack((cloud, cloud1))
                        except:
                                cloud = cloud1.copy()

                
                count1tc=count1tc+75
                count2tc=count1tc+75
    
    
   
        ## --------------- ##
        ## open wp_* files ##
        ## --------------- ##
        f_wp = open(pathname + 'wp_' + str(c) + '.dat')
        content = f_wp.readlines()
    
         # read the content of the file opened
        count1wp=0
        count2wp=count1wp+57  # number of lines between the first block(wind velocity in x , wind velocity in y,pressure (atmospheric) and the next one
        while count2wp <= len(content):
                 tmp = content[count1wp:count2wp]
                 date = datetime.strptime(tmp[1:2][0][:-1], '%Y%m%d %H%M%S')
    
                 if len(tmp) >= 3:  # Ensure tmp has enough lines
    
                         N1 = int(tmp[2][0:2]) #total number of grid nodes
                         N2 = int(tmp[2][3:5]) # extract a specific substring(3rd, 4th) from the string located at index 2
                         lon1 = np.round(float(tmp[2][6:10]),2)  # extract a specific substring from the string located at index 2 convert substring to a float, and then round it to two decimal places
                         lat1 = np.round(float(tmp[2][25:29]),2) # extract a specific substring from the string located at index 2 convert substring to a float, and then round it to two decimal places
                         dx = np.round(float(tmp[2][29:35]),2) # extract a specific substring from the string located at index 2 convert substring to a float, and then round it to two decimal places
                         dy = np.round(float(tmp[2][49:55]),2) # extract a specific substring from the string located at index 2 convert substring to a float, and then round it to two decimal places
                         lons1 = np.arange(lon1, lon1+(dx*N1), dx)[0:-1] # arange a NumPy array of lon (evenly spaced values) within a specified range. lon1 + (dx * N1) calculates the upper bound of  
                         lats1 = np.arange(lat1, lat1+(dy*N2), dy) #  same as lons1
    
                 try:
                         lonswp = np.dstack((lons, lons1))
                         latswp = np.dstack((lats, lats1))
                 except:
                         lonswp = lons1.copy()
                         latswp = lats1.copy()
    
                 timewp = np.append(timewp, date)
                 if tmp[3].startswith('wind velocity in x'):
                         windutmp = tmp[4:21]
                         windu1 = np.array(np.zeros([N1,N2]))
                         for i in range(0,len(windutmp)):
                                 res = np.array([float(idx) for idx in windutmp[i][0:-1].split(' ')])
                                 windu1[:,i] = res
                         try:
                                 windu = np.dstack((windu, windu1))
                         except:
                                 windu = windu1.copy()
    
                 if tmp[21].startswith('wind velocity in y'):
                         windvtmp = tmp[22:39]
                         windv1 = np.array(np.zeros([N1,N2]))
                         for i in range(0,len(windvtmp)):
                                 res = np.array([float(idx) for idx in windvtmp[i][0:-1].split(' ')])
                                 windv1[:,i] = res
                         try:
                                 windv = np.dstack((windv, windv1))
                         except:
                                 windv = windv1.copy()
    
                 if tmp[39].startswith('pressure (atmospheric)'):
                         pressatmtmp = tmp[40:57]
                         pressatm1 = np.array(np.zeros([N1,N2]))
                         for i in range(0,len(pressatmtmp)):
                                 res = np.array([float(idx) for idx in pressatmtmp[i][0:-1].split(' ')])
                                 pressatm1[:,i] = res
                         try:
                                 pressatm = np.dstack((pressatm, pressatm1))
                         except:
                                 pressatm = pressatm1.copy()
    
                 count1wp=count1wp+57
                 count2wp=count1wp+57
    
    
         ## -------------------- ##
         ## open *saltn_1* files ##
         ## -------------------- ##
        f_saltn = open(pathname + 'saltn_1_' + str(c) + '.dat')
        content = f_saltn.readlines()
    
         # read the content of the file opened
        count1saltn=0
        count2saltn=count1saltn+104
    
        while count2saltn <= len(content):
                 tmp = content[count1saltn:count2saltn]
                 N = int(tmp[0][11:14]) #total number of grid nodes
                 Nz = int(tmp[0][15:17]) #total number of vertical levels
                 date = datetime.strptime(tmp[1:2][0][:-1], '%Y%m%d %H%M%S')
                 levels_saltn = tmp[2].split(' '); levels_saltn[-1] = levels_saltn[-1][0:-1]
                 levels_saltn = np.array(levels_saltn).astype(float)
    
                 timesaltn = np.append(timesaltn, date)
    
                 if tmp[3].startswith(' salinity'):
                         saltntmp = tmp[4:]
                         saltn1 = np.array(np.zeros([Nz,N])) #[nlevels,npoints]
                         for i in range(0,len(saltntmp)):
                                 res = np.array([float(idx) for idx in saltntmp[i][0:-1].split(' ')])
                                 saltn1[:,i] = res[2:] #[nlevels,npoints]
                         try:
                                 saltn = np.dstack((saltn, saltn1))
                         except:
                                 saltn = saltn1.copy()
    
    
                 count1saltn=count1saltn+104
                 count2saltn=count1saltn+104
    
    
         ## -------------------- ##
         ## open *tempn_1* files ##
         ## -------------------- ##
        f_tempn = open(pathname + 'tempn_1_' + str(c) + '.dat')
        content = f_tempn.readlines()
   
         # read the content of the file opened
        count1tempn=0
        count2tempn=count1tempn+104
    
        while count2tempn <= len(content):
                 tmp = content[count1tempn:count2tempn]
                 N = int(tmp[0][11:14]) #total number of grid nodes
                 Nz = int(tmp[0][15:17]) #total number of vertical levels
                 date = datetime.strptime(tmp[1:2][0][:-1], '%Y%m%d %H%M%S')
                 levels_tempn = tmp[2].split(' '); levels_tempn[-1] = levels_tempn[-1][0:-1]
                 levels_tempn = np.array(levels_tempn).astype(float)
    
                 timetempn = np.append(timetempn, date)
    
                 if tmp[3].startswith(' temperature'):
                         tempntmp = tmp[4:]
                         tempn1 = np.array(np.zeros([Nz,N])) #[nlevels,npoints]
                         for i in range(0,len(tempntmp)):
                                 res = np.array([float(idx) for idx in tempntmp[i][0:-1].split(' ')])
                                 tempn1[:,i] = res[2:] #[nlevels,npoints]
                         try:
                                 tempn = np.dstack((tempn, tempn1)) #[nlevels,npoints,time]
                         except:
                                 tempn = tempn1.copy()
    
    
                 count1tempn=count1tempn+104
                 count2tempn=count1tempn+104
    
    
         ## -------------------- ##
         ## open *uv3d_1* files ##
         ## -------------------- ##
        f_uv3d = open(pathname + 'uv3d_1_' + str(c) + '.dat')
        content = f_uv3d.readlines()
    
         # read the content of the file opened
        count1uv3d=0
        count2uv3d=count1uv3d+205
    
        while count2uv3d <= len(content):
                 tmp = content[count1uv3d:count2uv3d]
                 N = int(tmp[0][11:14]) #total number of grid nodes
                 Nz = int(tmp[0][15:17]) #total number of vertical levels
                 date = datetime.strptime(tmp[1:2][0][:-1], '%Y%m%d %H%M%S')
                 levels_uv3d = tmp[2].split(' '); levels_uv3d[-1] = levels_uv3d[-1][0:-1]
                 levels_uv3d = np.array(levels_uv3d).astype(float)   
                 timeuv3d = np.append(timeuv3d, date)
    
                 if tmp[3].startswith(' u-velocity [m/s]'):
                         U3dtmp = tmp[4:104]
                         U3d1 = np.array(np.zeros([Nz,N])) #[nlevels,npoints]
                         for i in range(0,len(U3dtmp)):
                                 res = np.array([float(idx) for idx in U3dtmp[i][0:-1].split(' ')])
                                 U3d1[:,i] = res[2:] #[nlevels,npoints]
                         try:
                                 U3d = np.dstack((U3d, U3d1))
                         except:
                                 U3d = U3d1.copy()
                                
                 if tmp[104].startswith(' v-velocity [m/s]'):
                         V3dtmp = tmp[105:]
                         V3d1 = np.array(np.zeros([Nz,N])) #[nlevels,npoints]
                         for i in range(0,len(V3dtmp)):
                                 # Parse the string, filter out empty elements, and convert to floats
                                 res = np.array([float(idx) for idx in V3dtmp[i][0:-1].split(' ') if idx.strip()])
                                 V3d1[:,i] = res[2:] #[nlevels,npoints]
                         try:
                                 V3d = np.dstack((V3d, V3d1))
                         except:
                                 V3d = V3d1.copy()
    
                 count1uv3d=count1uv3d+205
                 count2uv3d=count1uv3d+205
               
   
    
 #############################
 ### 2. INITIAL CONDITIONS ###
 #############################
	
	       
 	## -------------------- ##
 	## open boundin_* files ##
 	## -------------------- ##
	
        chunk_start_in = [] ### F
    for c in range(1,nk + 1):   #number of chunks
	
         f_boundin = open(pathname + 'boundin_' + str(c) + '.dat')
         content = f_boundin.readlines()

 	# read the content of the file opened
         date_boundin = datetime.strptime(content[1:2][0][:-1], '%Y%m%d %H%M%S')
         timeboundin[c] = date_boundin
         N_boundin = int(content[0][11:16]) #total number of grid nodes
         Nz_boundin = int(content[0][17:18]) #total number of vertical levels
        
        
        
         chunkc_add_in = False ### 
         if not chunkc_add_in: ### 
                        chunk_start_in.append(date_boundin) ### 
                        chunkc_add_in = True ### 
         else:
                         chunk_start_in.append(None) ### 

        
         if content[2].startswith(' water level'):
                   tmp = content[3:] #each line for each point

                   for n in range(0,len(tmp)):
                        boundtmp = tmp[n][:-1]
                        boundin[c,n] = float(boundtmp)


 	## ------------------- ##
 	## open saltin_* files ##
 	## ------------------- ##
         f_saltin = open(pathname + 'saltin_' + str(c) + '.dat')
         content = f_saltin.readlines()

 	# read the content of the file opened
         date_saltin = datetime.strptime(content[1:2][0][:-1], '%Y%m%d %H%M%S')
         timesaltin[c] = content[1:2][0][:-1]
         N_saltin = int(content[0][11:16]) #total number of grid nodes
         Nz_saltin = int(content[0][17:19]) #total number of vertical levels
         levels_saltin = content[2].split(' '); levels_saltin[-1] = levels_saltin[-1][0:-1]
         levels_saltin = np.array(levels_saltin).astype(float)

         if content[3].startswith(' salinity'):
                 tmp = content[4:] #each line for each point
 
                 for n in range(0,len(tmp)):
                         salttmp = tmp[n].split(' '); salttmp[-1] = salttmp[-1][0:-1]
                         saltinN1[c,n] = float(salttmp[0])
                         saltinN2[c,n] = float(salttmp[1])
                        
                         salttmp = [x for x in salttmp if x.strip()]
                         salttmp = salttmp[2:]; salttmp = np.array(salttmp).astype(float)
                         saltin[c,n,:] = salttmp


 	## ------------------- ##
 	## open tempin_* files ##
 	## ------------------- ##
         f_tempin = open(pathname + 'tempin_' + str(c) + '.dat')
         content = f_tempin.readlines()

 	# read the content of the file opened
         date_tempin = datetime.strptime(content[1:2][0][:-1], '%Y%m%d %H%M%S')
         timetempin[c] = content[1:2][0][:-1]
         N_tempin = int(content[0][11:16]) #total number of grid nodes
         Nz_tempin = int(content[0][17:19]) #total number of vertical levels
         levels_tempin = content[2].split(' '); levels_tempin[-1] = levels_tempin[-1][0:-1]
         levels_tempin = np.array(levels_tempin).astype(float)

         if content[3].startswith(' temperature'):
                 tmp = content[4:] #each line for each point

                 for n in range(0,len(tmp)):
                         temptmp = tmp[n].split(' '); temptmp[-1] = temptmp[-1][0:-1]
                         tempinN1[c,n] = float(temptmp[0])
                         tempinN2[c,n] = float(temptmp[1])
                         temptmp = temptmp[2:]; temptmp = [x for x in temptmp if x.strip()]
                         temptmp = np.array(temptmp).astype(float) 
                         tempin[c,n,:] = temptmp


 	## ------------------ ##
 	## open uvin_* files  ##
 	## ------------------ ##
	
         print(f"MAIN --- UV --- iteration {c}")
        
         f_UVin = open(pathname + 'uvin_' + str(c) + '.dat')
         content = f_UVin.readlines()

 	# read the content of the file opened
         N_UVin = int(content[0][11:16]) #total number of grid nodes
         Nz_UVin = int(content[0][17:19]) #total number of vertical levels
         levels_UV = content[2].split(' '); levels_UV[-1] = levels_UV[-1][0:-1]
         levels_UV = np.array(levels_UV).astype(float)
                
         timeUVin[c] = content[1:2][0][:-1]
         if content[3].startswith(' u-velocity'):
                 tmp = content[4:42521] #each line for each point
                 for n in range(0,len(tmp)):
                         UVtmp = tmp[n].split(' '); UVtmp[-1] = UVtmp[-1][0:-1]
                         UVinN1[0,c,n] = float(UVtmp[0])
                         UVinN2[0,c,n] = float(UVtmp[1])
                         UVtmp = UVtmp[2:]; UVtmp = np.array(UVtmp).astype(float)
                         UVin[c,0,n,:] = UVtmp #Uin
                        
         if content[42521].startswith(' v-velocity'):
                  tmp = content[42522:] #each line for each point
                  for n in range(0,len(tmp)):
                         UVtmp = tmp[n].split(' '); UVtmp[-1] = UVtmp[-1][0:-1]
                         UVinN1[1,c,n] = float(UVtmp[0])
                         UVinN2[1,c,n] = float(UVtmp[1])
                         UVtmp = UVtmp[2:]; UVtmp = np.array(UVtmp).astype(float)
                         UVin[c,1,n,:] = UVtmp # extract the 2nd slice (Vin) 

         f_tc.close(); f_wp.close(); f_saltin.close(); f_tempin.close(); f_boundin.close(); f_UVin.close(); 


 ############################### I define here missing values below the bathymetry due to the extrapolation  ###############################################################

def replace_last_n_levels_of_nodes(arr, node_last_levels_mapping, missing_value=-999.0):
     """
     Replace the last N levels of specific nodes with missing values.

     Parameters:
         arr (np.ndarray): The array to modify (shape: [levels, nodes, time]).
         node_last_levels_mapping (dict): A dictionary mapping nodes to the number of last levels to replace.
                                          Keys are node indices (int), values are the number of last levels (int).
                                          Example: {0: 16, 10: 12}
         missing_value (float): The value to insert as missing data.
    
     Returns:
         np.ndarray: The modified array.
     """
     total_levels = arr.shape[0]  # Total number of levels in the array

     for node, num_last_levels in node_last_levels_mapping.items():
         levels_to_replace = range(total_levels - num_last_levels, total_levels)  # Last N levels
         for level in levels_to_replace:
             arr[level, node, :] = missing_value  # Replace across all time steps
     return arr

# ###############################################################################################################################################################################


# ####################################################################################################################################################################################

                       #######################################################################################
                       #                                                                                     #
                       #                     apply misssing values for values below the bathymetry           #
                       #                                                                                     #
                       #######################################################################################
 
saltin1 = saltin[1:,:,:]
tempin1 = tempin[1:,:,:]
Uin1 = UVin[1:,0,:,:]
Vin3 = UVin[1:,1,:,:]


 # Define the nodes and the number of last levels to replace in (saltn - tempn - U3d - V3d )
node_last_levels_mapping = {
     0: 16,  # Replace the last 16 levels of node 0
     20: 11, # Replace the last 11 levels of node 20
     40: 3,   # Replace the last 3 levels of node 40
     90: 5   # Replace the last 5 levels of node 90
}


## Apply the replacements
#saltn = replace_last_n_levels_of_nodes(saltn, node_last_levels_mapping, missing_value=-999.0)
#tempn = replace_last_n_levels_of_nodes(tempn, node_last_levels_mapping, missing_value=-999.0)
#U3d = replace_last_n_levels_of_nodes(U3d, node_last_levels_mapping, missing_value=-999.0)
#V3d = replace_last_n_levels_of_nodes(V3d, node_last_levels_mapping, missing_value=-999.0)



 ## Define the nodes and the number of last levels to replace in (saltin - tempin - Uin3 )
node_last_levels_mapping = {
     0: 16,  # Replace the last 16 levels of node 0
     39590: 1, # Replace the last 1 levels of node 20
     42151: 4,   # Replace the last 4 levels of node 40
     40582: 6,   # Replace the last 6 levels of node 90
     42000: 11 # Replace the last 11 levels of node 20

}


saltin2 = np.transpose(saltin1, (2, 1, 0)) # Transpose on level, node, time
tempin2 = np.transpose(tempin1, (2, 1, 0)) # Transpose on level, node, time
Uin2 = np.transpose(Uin1, (2, 1, 0)) # Transpose on level, node, time

saltin3 = replace_last_n_levels_of_nodes(saltin2, node_last_levels_mapping, missing_value=-999.0)
tempin3 = replace_last_n_levels_of_nodes(tempin2, node_last_levels_mapping, missing_value=-999.0)
Uin3 = replace_last_n_levels_of_nodes(Uin2, node_last_levels_mapping, missing_value=-999.0)

saltin3 = np.transpose(saltin3, (2, 1, 0)) # Transpose on level, node, time
tempin3 = np.transpose(tempin3, (2, 1, 0)) # Transpose on level, node, time
Uin3 = np.transpose(Uin3, (2, 1, 0)) # Transpose on level, node, time

### Define the nodes and the number of last levels to replace
#node_last_levels_mapping = {
#     42517: 16 # Replace the last 11 levels of node 20

#}
#Vin3 = replace_last_n_levels_of_nodes(Vin3, node_last_levels_mapping, missing_value=-999.0)

 ####################################################################################################################################################################################

     ######################################################################################
     #
     # 3. PRE-PLOTS
     #
     ######################################################################################
     
xticks_major = []
xticks_minor = []
chunk_start_times_labels = [] ### 
for d in range(len(chunk_start_times)): ### 
            if chunk_start_times[d]: ### 
                    chunk_start_times_labels.append(chunk_start_times[d].strftime("%Y-%m-%d")) ### 
                    xticks_major.append(d) ### 
            else: ### 
                    chunk_start_times_labels.append("") ### 
                    xticks_minor.append(d) ### 

   
print("MAIN --- PrePlots")
    
    ## 1. BOUNDARY CONDITIONS    

indx = [0,3,7,9] #point index to plot
indy = [0,5,10,12] #point index to plot

    #################################     tc file   ################################
    
#tc file
fig = pl.figure(figsize=(12,14))
ax = fig.add_subplot(411)
ax2 = fig.add_subplot(412)
ax3 = fig.add_subplot(413)
ax4 = fig.add_subplot(414)

ax.set_title('INPUT FILE = tc.dat',fontsize=18,weight='bold')
ax.plot(timetc,solarrad[indx[0],indy[0],:],'.-', color='red', linewidth=1.5, label='P1(0,0)')
ax.plot(timetc,solarrad[indx[2],indy[2],:],'.-', color='blue', linewidth=1.5, label='P2(7,10)')
ax.plot(timetc,solarrad[indx[3],indy[3],:],'.-', color='gold', linewidth=1.5, label='P3(9,12)')
ax.set_ylabel('solar radiaiton [W/m**2]', fontsize=16)
ax.set_ylim([0,35])
ax.legend()
ax.tick_params(axis='both', labelsize=14)
ax.grid()

ax2.plot(timetc,airtemp[indx[0],indy[0],:],'.-', color='red', linewidth=1.5, label='P1')
ax2.plot(timetc,airtemp[indx[2],indy[2],:],'.-', color='blue', linewidth=1.5, label='P2')
ax2.plot(timetc,airtemp[indx[3],indy[3],:],'.-', color='gold', linewidth=1.5, label='P3')
ax2.set_ylabel('air temperature [C]', fontsize=16)
ax2.set_ylim([0,35])
ax2.grid()
ax2.tick_params(axis='both', labelsize=14)

ax3.plot(timetc,dewptemp[indx[0],indy[0],:],'.-', color='red', linewidth=1.5, label='P1')
ax3.plot(timetc,dewptemp[indx[2],indy[2],:],'.-', color='blue', linewidth=1.5, label='P2')
ax3.plot(timetc,dewptemp[indx[3],indy[3],:],'.-', color='gold', linewidth=1.5, label='P3')
ax3.set_ylabel('dew point temperature [C]', fontsize=16)
ax3.set_ylim([-5,25])
ax3.grid()
ax3.tick_params(axis='both', labelsize=14)

ax4.plot(timetc,cloud[indx[0],indy[0],:],'.', color='red', linewidth=1.5, label='P1')
ax4.plot(timetc,cloud[indx[2],indy[2],:],'.', color='blue', linewidth=1.5, label='P2')
ax4.plot(timetc,cloud[indx[3],indy[3],:],'.', color='gold', linewidth=1.5, label='P3')



#######################################
#x_ticks = list(range(len(chunk_start_times_labels))) ### 
#ax4.set_xticks(x_ticks) ### 
#ax4.set_xticklabels(chunk_start_times_labels, rotation=45) ### F
#ax4.tick_params(axis='both', labelsize=14) ### 
#ax4.set_xticks(xticks_major, minor=False) ### 
#ax4.set_xticks(xticks_minor, minor=True) ### 
#######################################


ax4.set_ylabel('cloud cover [0-1]', fontsize=16)
ax4.set_ylim([0,1])
ax4.grid()
ax4.tick_params(axis='both', labelsize=14)
pl.tight_layout()

pl.tight_layout()
print(f"{pathnamefig}plot_input_tcfile.png")
pl.savefig(pathnamefig + 'plot_input_tcfile.png', format='png', dpi=300, facecolor='w', edgecolor='w',
          orientation='portrait', transparent=False, bbox_inches='tight', pad_inches=0.1)
pl.close()
    
#pdb.set_trace()
    
  
    ############################################################                      wp file       #######################################################
#wp file
fig = pl.figure(figsize=(12,14))
ax = fig.add_subplot(411)
ax2 = fig.add_subplot(412)
ax3 = fig.add_subplot(413)
ax4 = fig.add_subplot(414)

ax.set_title('INPUT FILE = wp.dat',fontsize=18,weight='bold')
ax.plot(timetc,windu[indx[0],indy[0],:],'.-', color='black', linewidth=1.5, label='P1(0,0)')
ax.plot(timetc,windu[indx[2],indy[2],:],'.-', color='blue', linewidth=1.5, label='P2(7,10)')
ax.plot(timetc,windu[indx[3],indy[3],:],'.-', color='aquamarine', linewidth=1.5, label='P3(9,12)')
ax.set_ylabel('wind velocity in x [m/s]', fontsize=16)
ax.set_ylim([-15,15])
ax.grid()
ax.legend()
ax.tick_params(axis='both', labelsize=14)

ax2.plot(timetc,windv[indx[0],indy[0],:],'.-', color='black', linewidth=1.5, label='P1')
ax2.plot(timetc,windv[indx[2],indy[2],:],'.-', color='blue', linewidth=1.5, label='P2')
ax2.plot(timetc,windv[indx[3],indy[3],:],'.-', color='aquamarine', linewidth=1.5, label='P3')
ax2.set_ylabel('wind velocity in v [m/s]', fontsize=16)
ax2.set_ylim([-15,15])
ax2.legend()
ax2.grid()
ax2.tick_params(axis='both', labelsize=14)

ax3.plot(timetc,np.sqrt(windu[indx[0],indy[0],:]**2 + windv[indx[0],indy[0],:]**2),'.-', color='black', linewidth=1.5, label='P1')
ax3.plot(timetc,np.sqrt(windu[indx[2],indy[2],:]**2 + windv[indx[2],indy[2],:]**2),'.-', color='blue', linewidth=1.5, label='P2')
ax3.plot(timetc,np.sqrt(windu[indx[3],indy[3],:]**2 + windv[indx[3],indy[3],:]**2),'.-', color='aquamarine', linewidth=1.5, label='P3')
ax3.set_ylabel('Horizontal velocity [m/s]', fontsize=16)
ax3.set_ylim([0,17.5])
ax3.legend()
ax3.grid()
ax3.tick_params(axis='both', labelsize=14)

ax4.plot(timetc,pressatm[indx[0],indy[0],:],'.-', color='black', linewidth=1.5, label='P1(0,0)')
ax4.plot(timetc,pressatm[indx[2],indy[2],:],'.-', color='blue', linewidth=1.5, label='P2(7,10)')
ax4.plot(timetc,pressatm[indx[3],indy[3],:],'.-', color='aquamarine', linewidth=1.5, label='P3(9,12)')
ax4.set_ylabel('atmospheric pressure [Pa]', fontsize=16)
ax4.set_ylim([98000,106000])
ax4.legend()
ax4.grid()
ax4.tick_params(axis='both', labelsize=14)

pl.tight_layout()
pl.savefig(pathnamefig+'plot_input_wpfile.png', dpi=500, facecolor='w', edgecolor='w',
      orientation='portrait', transparent=False, bbox_inches='tight', pad_inches=0.2)
pl.close()

 
    
##########################################################           BC PLOTS   #####################################################
    


                  #################################    saltn and tempn    ################################
                  
plot_bc(saltn,timesaltn,'saltn',pathnamefig)
plot_bc(tempn,timetempn,'tempn',pathnamefig)


UV3d=np.sqrt(U3d**2 + V3d**2)
plot_bc(U3d,timeuv3d,'U3d',pathnamefig)
plot_bc(V3d,timeuv3d,'V3d',pathnamefig)
plot_bc(UV3d,timeuv3d,'UV3d',pathnamefig)
print('tempn=',tempn.shape)
print('timetempn=',len(timetempn))
print('U3d=',U3d.shape)
print('V3d=',V3d.shape)
print('UV3d=',UV3d.shape)


###################################################################     boundin         ########################################################

boundin = boundin[1:,:]
timesaltin3 = timesaltin[1:]
#timetempin = timetempin[1:]
timeboundin = timeboundin[1:]
#timeVin = timeVin[1:]
#timeUin = timeUin[1:]
timeUVin3 = timeUVin[1:]

for t in range(0,len(timesaltin3)): 
         
               try:
               
                   timesaltin3[t] = datetime.strptime(timesaltin3[t], '%Y%m%d %H%M%S')
                   timetempin[t] = datetime.strptime(timetempin[t], '%Y%m%d %H%M%S')
                   timeboundin[t] = datetime.strptime(timeboundin[t], '%Y%m%d %H%M%S')
##                   timeUin[t] = datetime.strptime(timeUin[t], '%Y%m%d %H%M%S')
##                   timeVin[t] = datetime.strptime(timeVin[t], '%Y%m%d %H%M%S')
##                   timeUVin3[t] = datetime.strptime(timeUVin3[t], '%Y%m%d %H%M%S')
                   
               except:
         
                  pass


# IC PLOTS
#boundin

#indd = [0,10000,20000,30000,42000] # create a list of 7 integers points
indd = [0,39590,42151,40582,42000] # create a list of 5 points

fig = pl.figure(figsize=(12,8))
ax = fig.add_subplot(111)

ax.set_title('INPUT FILE = boundin.dat (nlevel = 0)',fontsize=18,weight='bold')
ax.plot(timeboundin,boundin[:,indd[0]],'.-', color='blue', linewidth=2, label='P1(First node)')
ax.plot(timeboundin,boundin[:,indd[1]],'.-', color='cyan',linewidth=2, label='P2(39590 nodes)')
ax.plot(timeboundin,boundin[:,indd[2]],'.-', color='black',linewidth=2, label='P3(42151 nodes)')
ax.plot(timeboundin,boundin[:,indd[3]],'.-', color='blueviolet',linewidth=2, label='P4(40582 nodes)')
ax.plot(timeboundin,boundin[:,indd[4]],'.-', color='red',linewidth=2, label='P5(42000 nodes)')

ax.set_ylabel('water level [m]', fontsize=16)
ax.set_ylim([-0.8,0])
ax.legend()
ax.tick_params(axis='both', labelsize=14)
ax.grid()
pl.tight_layout()
pl.savefig(pathnamefig+'plot_input_boundin.png', dpi=300, facecolor='w', edgecolor='w',
        orientation='portrait', transparent=False, bbox_inches='tight', pad_inches=0.1)
pl.close()

############################################################################################################

UVin3= np.sqrt(Uin3**2 + Vin3**2)

print('saltin=',saltin.shape)
print('saltin[1:,:,:]=',saltin3.shape)
print('timesaltin3=',len(timesaltin3))

plot_ic(saltin3,timesaltin3,'saltin',pathnamefig)
plot_ic(tempin3,timesaltin3,'tempin',pathnamefig)
plot_ic(Uin3,timesaltin3,'uin',pathnamefig)
plot_ic(Vin3,timesaltin3,'vin',pathnamefig)
plot_ic(UVin3,timesaltin3,'uvin',pathnamefig)




