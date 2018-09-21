'''Initial pass of setting up a processing and analysis pipeline'''

import numpy as np
import matplotlib.pyplot as plt
from data_cleaning.data_cleaning import low_baseline
from deltaF import baseline

data = np.load('/Users/Megan/data_analysis/Aug02_2018_B3/B3_TS/Extracted/rg_B3_TS_ZP_1.npz')
new_data = []
new_data, deletedcells = low_baseline(data['data'],150)
(times, cells) = new_data.shape
print(deletedcells)
timepoints = range(times)
f0 = baseline(new_data, 3, 5)


fig, ax = plt.subplots(2, sharex='col', figsize = (100,5))
ax[0].plot(timepoints, new_data[:,1])
ax[1].plot(timepoints, f0[:,1])

plt.xlabel('Time (s)')
plt.ylabel('Signal')
plt.show()
