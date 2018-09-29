'''Importing z stack data that is separate, and joining together those which
are part of the same cell, by virtue of being within a threshold distance in x
and y in adjacent stacks'''

# Path hack.
import sys, os
sys.path.insert(0, os.path.abspath('..'))
import numpy as np
import glob
import matplotlib.pyplot as plt
#from neurons.general_functions.plotting_functions import threed_points_plot

data_root_path = '/Users/Megan/data_analysis/Aug02_2018_B3/'

def z_coordinate(file):
    '''internal sorting and coordinate returning function'''
    i = file.find('ZP_') + 3
    j = file.find('.npz')
    z_coord = int(file[i:j]) * 4 #multiply by 4 microns
    return z_coord

def remove_redundancy(first, second, thresh = 3.0):
    '''compares the first and second sets of coordinates for identified blobs
    and identifies those that are redundant because they sit within thresh of each other'''
    x1 = first[:,0]
    x2 = second[:,0]
    XF, XS = np.meshgrid(x1, x2)
    plt.plot(XF, XS, marker='.', color='k', linestyle='none')
    plt.show()
    print(XF)
    print(XS)
    # for i in range(len(XF[1])):
    #     print(str(XF[1][i]) + ', '+ str(XS[i][1]))


def findall_coords(directory, flag = 'ZP_'):
    '''takes all the datafiles and spits out an array of the coordinates
    of all of the blobs that were extracted: aim to plot locations and identify
    how much redundancy in the data'''
    datalist = glob.glob(directory+ '*TS/Extracted/*' + flag + '*.npz')
    datalist = sorted(datalist, key = z_coordinate) #sort the files by coordinate
    i = 1
    xyzarray = np.empty((0, 4))
    for datafile in datalist:
        tempdata = np.load(datafile)
        z_coord = z_coordinate(datafile)
        xyzarray_temp = np.insert(tempdata['xy'], 2, z_coord, axis=1)
        xyzarray = np.append(xyzarray, xyzarray_temp, axis=0)
    #print(xyzarray.shape)
    return xyzarray


def join_z_stacks(directory, flag = 'ZP_'):
    '''takes in all the data files in a directory, and joins them in to
    one array of all cells found in the full brain map.'''

    datalist = glob.glob(directory+ '*TS/Extracted/*' + flag + '*.npz')
    datalist = sorted(datalist, key = z_coordinate) #sort the files by coordinate

    z_values = []
    data = dict({'values':[], 'coords':[]})
    for datafile in datalist:
        tempdata = np.load(datafile)
        #look at all coordinates in this file and compare with those in previous,
        #if coords are within threshold, take larger magnitude of time-series and
        #remove the other
        if datafile == datalist[0]:
            first = tempdata['xy']
            #print(tempdata['xy'])
        elif datafile == datalist[-1]:
            second = tempdata['xy']
            remove_redundancy(first, second)
            first = tempdata['xy']
            #print(tempdata['xy'])
                #r2 = (tempdata[i,0])**2 + (tempdata[i,1])**2

        #print(datafile + ' ' + str(z_values))


def testing_join_z_stacks(directory):
    print(join_z_stacks(directory))

def testing_findall_coords(directory):
    total_array = findall_coords(directory)
    filepath = data_root_path + 'B3_TS/all_coords/xyzarray'
    np.savez(filepath, total_array)
    threed_points_plot(total_array)

def testing_remove_redundancy():
    first = np.array([[0, 0],[1,1],[2,2],[3,3],[4,4]])
    second = first
    remove_redundancy(first, second)

if __name__ == '__main__':
    #testing_join_z_stacks(data_root_path)
    #testing_findall_coords(data_root_path)
    testing_remove_redundancy()
