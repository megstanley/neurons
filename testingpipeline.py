'''Initial pass of setting up a processing and analysis pipeline.
This is incomplete, subject to modification as the pipeline grows'''

import numpy as np
import matplotlib.pyplot as plt
import data_cleaning.data_cleaning as dclean
import glob

directory = '/Users/Megan/data_analysis/Aug02_2018_B3/'

class test_cleaning_pipeline(object):

    '''Process all the files in a folder:
    1. Load the file
    2. Perform data cleaning
    3. Save the cleaned data
    '''

    def __init__(self, directory, flag = 'ZP_'):
        self.folder = directory
        self.file_list = glob.glob(directory+ '*TS/Extracted/*' + flag + '*.npz')
        self.current_file = None

    def load_file(self, filename):
        '''load the file'''
        self.filename = filename
        self.data = np.load(self.filename)

    def save_file(self, outputpath):
        '''save the cleaned data to another folder'''
        np.savez(outputpath, self.cleandata)

    def run_cleaning(self, margin, threshold):
        '''find edge and low baseline time-series'''
        self.total_baseline_mask = dclean.find_low_baseline(self.data, threshold)
        self.total_edges_mask = dclean.find_edges(self.data, margin)
        self.cleandata = dict({'data':[], 'xy':[]})
        self.cleandata['xy'] = self.data['xy'][self.total_edges_mask[0],:]
        self.cleandata['data'] = self.data['data'][:,self.total_edges_mask[0]]

        #need to recalculate the baseline mask now the edges have been removed
        self.update_baseline_mask = dclean.find_low_baseline(self.cleandata, threshold)
        self.cleandata['xy'] = self.cleandata['xy'][self.update_baseline_mask,:]
        self.cleandata['data'] = self.cleandata['data'][:,self.update_baseline_mask]

def main():
    tp = test_cleaning_pipeline(directory)

    for file in tp.file_list:
        #file = tp.file_list[0]
        tp.load_file(file)
        tp.run_cleaning(10, 200)
        ident = tp.filename.find('/Extracted/')
        ind_name = tp.filename[ident+11:]
        outputpath = outputpath = directory + 'B3_TS/Cleaned/' + ind_name
        tp.save_file(outputpath)


if __name__ == "__main__":
    main()
