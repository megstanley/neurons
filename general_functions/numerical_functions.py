'''A few functions that get used to process the data here and there
(aim is to allow for easy changing of method used to process signals)
Lots of ideas borrowed from scipy cookbook and documentation'''

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
from scipy.ndimage import gaussian_filter1d

def sg_lowpass(data, t_win, polydegree = 2):
    '''Low pass filtering the signal using Savitsky-Golay method'''
    filt = savgol_filter(data, t_win, polydegree, axis = 1)
    return filt

def gaussian_lpf(data, t_win= 3):
    '''Low pass smoothing filter using convolution with Gaussian:
    a weighted moving average.
    data is input unsmoothed data. t_win is some characteristic feature
    time of the data (determine by testing).'''
    sig_filt = gaussian_filter1d(data, t_win, axis = 0)

    return sig_filt

'''Test functions'''
def main_sgfilter_test(data):
    filt = sg_lowpass(data, 9, 3)
    times, cells = data.shape
    timepoints = range(times)
    plt.plot(timepoints, data[:,2])
    plt.plot(timepoints, filt[:,2])
    plt.xlabel('Time (s)')
    plt.ylabel('Signal')
    plt.show()

def main_gaussianlpf_test(data):
    sig_filt = gaussian_lpf(data, 3)
    times, cells = data.shape
    timepoints = range(times)
    plt.plot(timepoints, data[:,2])
    plt.plot(timepoints, sig_filt[:,2])
    plt.xlabel('Time (s)')
    plt.ylabel('Signal')
    plt.show()

if __name__ == "__main__":
    data = np.load('/Users/Megan/data_analysis/Aug02_2018_B3/B3_TS/Extracted/rg_B3_TS_ZP_1.npz')
    #main_sgfilter_test(data['data'])
    main_gaussianlpf_test(data['data'])
