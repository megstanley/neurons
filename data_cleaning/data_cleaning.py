'''functions for some initial data cleaning to remove artifacts that have
been identified'''
import matplotlib.pyplot as plt
import numpy as np

data_root_path = '/Users/Megan/data_analysis/Aug02_2018_B3/'

def find_low_baseline(raw_data, threshold):
    '''find time-series with low baselines, as these are artifacts'''
    minima = np.amin(raw_data, axis = 0)
    threshold_pass = [i>threshold for i in minima]

    #print(str(threshold_pass.count(True))+ ' out of ' + str(cells)+ ' time series above threshold.')
    # new_data = raw_data[:, threshold_pass]
    # deletedcells = np.nonzero(np.invert(threshold_pass))
    #return new_data, deletedcells[0]

    return threshold_pass

def find_edges(data, margin, range_x = 693, range_y = 790):
    '''Identifies time-series corresponding to points on the extreme edges,
    as these are artifacts.'''

    small_x = margin
    large_x = range_x - margin
    small_y = margin
    large_y = range_y - margin
    mask = [(data['xy'][:,0]<=large_x)&(data['xy'][:,0]>=small_x)&(data['xy'][:,1]<=large_y)&(data['xy'][:,1]>=small_y)]

    return mask

def test_find_edges():
    newdata = dict({'data':[], 'xy':[]})
    data = np.load('/Users/Megan/data_analysis/Aug02_2018_B3/B3_TS/Extracted/rg_B3_TS_ZP_20.npz')
    mask = find_edges(data, 15)
    print(mask)
    newdata['xy'] = data['xy'][mask[0],:]
    newdata['data'] = data['data'][:,mask[0]]
    print(newdata['xy'].shape)
    filepath = data_root_path + 'B3_TS/rg_B3_TS_ZP_20_removed_edges15.npz'
    np.savez(filepath, newdata['xy'])

if __name__ == "__main__":
    test_find_edges()

    # data = np.load('/Users/Megan/data_analysis/Aug02_2018_B3/B3_TS/Extracted/rg_B3_TS_ZP_1.npz')
    # new_data = []
    # new_data, deletedcells = low_baseline(data['data'],150)
    # (times, cells) = new_data.shape
    # print(deletedcells)
    # timepoints = range(times)
    # fig, ax = plt.subplots(20, sharex='col', figsize = (100,5))
    # for i in range(20):
    #     ax[i].plot(timepoints, data['data'][:,i])
    # fig.subplots_adjust(hspace=0)
    #
    # for axis in ax:
    #     axis.label_outer()
    # plt.show()
