'''from looking at the plot of coordinates from adjacent z stacks, there is
a constant offset that appears -- the coordinates for all found blobs
need to be corrected. First, the drift must be found'''
# Path hack.
import sys, os
sys.path.insert(0, os.path.abspath('..'))
import numpy as np

def find_drift():


def drift_correct():


'''TO DO:now we compare the coordinates in this and the previous slice,
and output an average time-series for the two'''
