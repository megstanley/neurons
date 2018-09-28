'''Creating a module to calculate deltaF/F for the time-series data that
has been extracted from image files. This is based on a
calculation described in Nature Protocols 6:1 2011. '''
import matplotlib.pyplot as plt
import numpy as np
from general_functions.numerical_functions import gaussian_lpf
from scipy.signal import fftconvolve

'''to do: add the exp filter function'''

def baseline(raw_data, t1, t2):
    '''Finds the time-dependent baseline of F, F0. For each
    time series this is an array of the same length as the series.
    First, smooth F with moving average of length t1. Baseline for timepoint t
    is the minimum of smoothed F in a window length t2 before to time t'''

    f0 = np.zeros_like(raw_data)
    (times, cells) = f0.shape
    '''t1 window moving average'''
    #the first smoothing window is set to the mean of the window
    f0[:t1, :] = np.mean(raw_data[:t1,:], axis = 0)
    for index in range(t1, times - t1):
        f0[index, :] = np.mean(raw_data[index-t1:index+t1,:], axis = 0)
    f0[times-t1:,:] = np.mean(raw_data[times-t1:,:], axis = 0)

    '''assigning t2 minimum to timepoints'''
    f0[:t2, :] = np.amin(f0[:t2, :], axis = 0)
    for index2 in range(t2, times - t2):
        f0[index2, :] = np.amin(f0[index2-t2:index2+t2,:], axis = 0)
    f0[times-t2:,:] = np.mean(f0[times-t2:,:], axis = 0)

    return f0

def simple_baseline(raw_data, twin):
    '''a more simple but 'good enough' baseline'''
    f0 = np.zeros_like(raw_data)
    (times, cells) = f0.shape

    f0[:twin, :] = np.amin(raw_data[:twin, :], axis = 0)
    for index2 in range(twin, times - twin):
        f0[index2, :] = np.amin(raw_data[index2-twin:index2+twin,:], axis = 0)
    f0[times-twin:,:] = np.mean(raw_data[times-twin:,:], axis = 0)

    return f0

def deltaFF(raw_data, feature_time, simplebase = False, smooth = True):
    '''calculates the relative change in fluorescence above baseline,
    divided by fluorescence signal. Fluorescence signal can be smoothed.
    feature_time is the typical timescale of a feature in the data '''

    if smooth == True:
        FT = gaussian_lpf(raw_data, feature_time)
    else:
        FT = raw_data

    if simplebase == True:
        F0 = simple_baseline(FT, feature_time)+1e-008
    else:
        F0 = baseline(FT, feature_time, feature_time*3)+1e-008

    relF = (FT - F0)/F0

    return relF, F0, FT

def expFilt(data, t0, window):
    '''function to perform the optional exponentially weighted moving average
    step -- t0 is decay constant of exponential. window is the length of the
    filter window.'''
    #make the exponential array with which to convolve

    sig_filt = fftconvolve()


'''Some testing functions here'''

def main_testingRel_F():
    data = np.load('/Users/Megan/data_analysis/Aug02_2018_B3/B3_TS/Extracted/rg_B3_TS_ZP_1.npz')
    relF, F0, FT = deltaFF(data['data'], 3)
    times, cells = relF.shape
    timepoints = range(times)
    plt.plot(timepoints, deltaFF[:,2], 'r')
    # plt.plot(timepoints, F0[:,2], 'g')
    # plt.plot(timepoints, FT[:,2], 'b')
    plt.xlabel('Time (s)')
    plt.show()

def main_testingbaseline():
    data = np.load('/Users/Megan/data_analysis/Aug02_2018_B3/B3_TS/Extracted/rg_B3_TS_ZP_1.npz')
    feature_time = 21
    times, cells = data['data'].shape
    timepoints = range(times)
    F0_simple = simple_baseline(data['data'], feature_time)
    F0 = baseline(data['data'], feature_time, feature_time*3)
    plt.plot(timepoints, data['data'][:,2], 'r')
    plt.plot(timepoints, F0[:,2], 'g')
    plt.plot(timepoints, F0_simple[:,2], 'b')
    plt.xlabel('Time (s)')
    plt.show()

if __name__ == "__main__":
    #main_testingRel_F()
    main_testingbaseline()
