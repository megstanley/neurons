'''Initial pass of setting up a processing and analysis pipeline.
This is incomplete, subject to modification as the pipeline grows'''

import numpy as np
import matplotlib.pyplot as plt
import data_cleaning.data_cleaning as dclean
import glob

directory = '/Users/Megan/data_analysis/Aug02_2018_B3/'

class test_pipeline(object):

    '''Process all the files in a folder:
    1. Load the file
    2. Perform data cleaning
    3. Save the cleaned data
    '''

    def __init__(self, directory, flag = 'ZP_'):
        self.folder = directory
        self.file_list = glob.glob(directory+ '*TS/Extracted/*' + flag + '*.npz')
        self.current_file = None

    def load_file(self, file_number):
        '''load the file at file_number from file_list'''
        self.current_file = file_number
        self.filename = self.file_list[file_number]
        self.data = np.load(self.filename)

    def save_file(self, outputpath):
        '''save the current file to another folder'''


    def run_cleaning(self, margin, threshold):
        '''this is currently incorrect'''

        i = 1
        for file in self.file_list:
            self.load_file(i)
            self.baseline_mask = dclean.find_low_baseline(self.data, threshold)
            self.edges_mask = dclean.find_edges(self.data, margin)
            self.newdata = dict({'data':[], 'xy':[]})
            self.newdata['xy'] = self.data['xy'][self.edges_mask[0],:]
            self.newdata['data'] = self.data['data'][:,self.edges_mask[0]]
            # self.newdata['xy'] = self.newdata['xy'][self.baseline_mask,:]
            # self.newdata['data'] = self.newdata['data'][:,self.baseline_mask]

            i += 1



def main():
    tp = test_pipeline(directory)

    tp.run_cleaning(10, 200)



if __name__ == "__main__":
    main()
