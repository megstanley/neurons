'''functions for some initial data cleaning to remove artifacts that have
been identified'''
import matplotlib.pyplot as plt
import numpy as np

def low_baseline(raw_data, threshold):
    '''removes time-series with low baselines, as these are artifacts'''
    minima = np.amin(raw_data, axis = 0)
    times, cells = raw_data.shape
    threshold_pass = [i>threshold for i in minima]

    print(str(threshold_pass.count(True))+ ' out of ' + str(cells)+ ' time series above threshold.')

    new_data = raw_data[:, threshold_pass]
    deletedcells = np.nonzero(np.invert(threshold_pass))

    return new_data, deletedcells[0]

def remove_edges(data, margin):
    '''chops off time-series corresponding to points on the extreme edges,
    as these are artifacts.'''
    coords = data['xy']
    mask = [coords[:,0]]

if __name__ == "__main__":
    '''bits and pieces for testing the functions
    TO DO: clean this up and put in testing functions'''

    data = np.load('/Users/Megan/data_analysis/Aug02_2018_B3/B3_TS/Extracted/rg_B3_TS_ZP_1.npz')
    new_data = []
    new_data, deletedcells = low_baseline(data['data'],150)
    (times, cells) = new_data.shape
    print(deletedcells)
    timepoints = range(times)
    fig, ax = plt.subplots(20, sharex='col', figsize = (100,5))
    for i in range(20):
        ax[i].plot(timepoints, data['data'][:,i])
    fig.subplots_adjust(hspace=0)

    for axis in ax:
        axis.label_outer()
    plt.show()
