'''Importing z stack data that is separate, and joining together those which
are part of the same cell, by virtue of being within a threshold distance in x
and y in adjacent stacks'''

import numpy as np
import glob

data_root_path = '/Users/Megan/data_analysis/Aug02_2018_B3/'

def join_z_stacks(directory, flag = 'ZP_'):
    '''takes in all the data files in a directory, and joins them in to
    one array of all cells found in the full brain map.'''

    datalist = glob.glob(directory+ '*TS/Extracted/*' + flag + '*.npz')
    #return datalist
    #find the z value associated with each file from the file name
    z_values = []
    for datafile in datalist:
        i = datafile.find(flag)
        #tempdata = data = np.load(datafile)
        print(datafile + ' ' +str(i))


def testing_join_z_stacks(directory):
    print(join_z_stacks(directory))

if __name__ == '__main__':
    testing_join_z_stacks(data_root_path)
