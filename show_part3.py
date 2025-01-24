import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import subprocess
import matplotlib.pyplot as plt
#from fem_tools import *
import sys, os
import re
from netCDF4 import Dataset

ZOOM=False

if len(sys.argv) < 3:
	print ('Error: Missing argument')
	print ('Please provide path of shyfem netcdf unstructured output ')
	print ('and path of partitioning file')
	sys.exit(1)		

shyfem_coord_path 	= sys.argv[1]
part_path 		= sys.argv[2]

# Extract the number after 'elems' using regex
match = re.search(r'elems(\d+)', part_path)
# Check if the pattern is found, and extract the number
if match:
    number_of_parts = match.group(1)
    print(f"Number of parts: {number_of_parts}")
else:
    print("No matching pattern found.")


def load_shyfem_coords(path):
        nc      = Dataset(path)
        lons    = nc.variables['longitude'][:]
        lats    = nc.variables['latitude'][:]
        elems   = nc.variables['element_index'][:]-1
        #elems   = nc.variables['element'][:]-1
        levels  = nc.variables['level'][:]
        time    = nc.variables['time'][:]
        nc.close()

        return (lons,lats,elems,levels,time)

def load_shyfem_variable(path,varname):
        nc      = Dataset(path)
        var     = nc.variables[varname][:]
        nc.close()

        return var

def read_partition(part_path):
	# read all lines apart from last
	data = np.genfromtxt(part_path,skip_header=1,skip_footer=1)
	# read last line in file
	line = subprocess.check_output(['tail', '-1', part_path])
	line = np.asarray([int(i) for i in line.split()])
	nr,nc = data.shape 
	data = data.reshape(nr*nc)
	# concatenate last line
	data = np.concatenate((data,line))
	return data

lons,lats,elems,depth,time = load_shyfem_coords(shyfem_coord_path)

## read partition file
mpi_proc = read_partition(part_path)

mpi_proc        -= 1

nkn	= len(lons)
nel	= elems.shape[0]

nel_part	= len(mpi_proc)


if (nel != nel_part):
	print ('ERROR')	
	print ('Number of elements in shyfem grid does not match the')
	print ('number elements in partitioning file')
	sys.exit(1)


## this is to view process number at mouse 
x_centroid = np.mean(lons[elems],axis=1)
y_centroid = np.mean(lats[elems],axis=1)

glob_node	= np.arange(nkn)+1
glob_ele	= np.arange(nel)+1

def fmt(x, y):
        dist = np.sqrt((x-x_centroid)**2+(y-y_centroid)**2)
        dist2 = np.sqrt((x-lons)**2+(y-lats)**2)	
        idx = np.argmin(dist)
        z = mpi_proc[idx]
        e = glob_ele[idx]	
        idx2	= np.argmin(dist2)		
        n	= glob_node[idx2]	
        return 'x={x:.7f}  y={y:.7f} PROC={z:.1f} ele={e:6d} node={n:6d}'.format(x=x, y=y, z=z, e=e, n=n)

## make plot
plt.figure(figsize=(12,8))
cf = plt.tripcolor(lons,lats,elems,mpi_proc,cmap='jet')
plt.triplot(lons,lats,elems,color='k',linewidth=0.2)
cb = plt.colorbar(cf)
cb.set_label('MPI Process',fontsize=15)
plt.gca().format_coord = fmt

plt.title('Partition: ' + os.path.basename(part_path))

outfile=f'./{number_of_parts}_partition.png'

if ZOOM:
    outfile=f'./{number_of_parts}_partition_zoom.png'
    #plt.xlim(12.2,12.4)
    #plt.ylim(41.6,41.9)
    #plt.ylim(41.68,41.85)
    #plt.xlim(12.13,12.30)
    #plt.ylim(41.70,41.80)
    #plt.xlim(12.10,12.30)
    #plt.ylim(41.725,41.775)
    #plt.xlim(12.20,12.25)
    plt.ylim(44.10,45.4)
    plt.xlim(11.46,13.18)

else:
    pass
    #plt.ylim(41.20,42.10) #JK
    #plt.xlim(11.60,12.70) #JK
    #plt.ylim(41.20,41.70) #JK
    #plt.xlim(15.8,16.6) #JK
    plt.ylim(44.20,45.4) #LW
    plt.xlim(11.5,13.2) #LW

    outfile=f'./{number_of_parts}_partition.png' #JK

plt.savefig(outfile, dpi=300, bbox_inches='tight')
plt.show()


