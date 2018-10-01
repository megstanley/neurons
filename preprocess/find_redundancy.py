'''function to find the redundancies of data in adjacent slices'''

import numpy as np

def find_redundancy(first, second, thresh = 0.1):
    '''compares the first and second sets of coordinates for identified blobs
    and identifies those that are redundant because they sit within threshold of each other
    Returns the indices in each array of those that sit within the threshold.'''
    x1 = first[:,0]
    x2 = second[:,0]
    y1 = first[:,1]
    y2 = second[:,1]
    #use meshgrid to compare every X and every Y value of one dataset to the
    #next dataset.
    XF, XS = np.meshgrid(x1, x2)
    YF, YS = np.meshgrid(y1, y2)
    displacements = np.sqrt((XF-XS)**2 + (YF-YS)**2)
    redundants = np.where(displacements <= thresh)
    #returning index arrays
    return redundants[0], redundants[1]
