'''functions for some initial data cleaning to remove artifacts that have
been identified:
1. low_baseline -- if the lowest value in a measurement is below a threshold
    (typically 200) then the identified neuron is likely an artifact rather
    than a true neuron. It has possibly been found by mistake on the edge of
    image, and moves out of frame due to drifting, or is an inactive neuron with
    a background fluorescence'''
import matplotlib.pyplot as plt
import numpy as np

def low_baseline(raw_data, threshold):

    minima = np.amin(raw_data, axis = 0)
    times, cells = raw_data.shape
    threshold_pass = [i>threshold for i in minima]

    print(str(threshold_pass.count(True))+ ' out of ' + str(cells)+ ' time series above threshold.')

    new_data = raw_data[:, threshold_pass]
    deletedcells = np.nonzero(np.invert(threshold_pass))

    return new_data, deletedcells[0]

if __name__ == "__main__":
    '''bits and pieces for testing the functions'''
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
