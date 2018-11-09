# neurons
Python-based analysis of multiple neuron (larval zebrafish) time-series data. 

This is currently **very much** a work in progress. 

## Packages: 

### data_cleaning
Module to do initial cleaning of data, *data_cleaning.py*. So far that includes removing data that contains low signal, indicating it is an artifact, with find_low_baseline and removing those points that are edge of pixel array artifacts with find_edges. Making a preprocessing and data_cleaning test pipeline in *testingpipeline.py* (this is very much a self-teaching exercise as well :) )

### preprocessing 
Here, working on removing the redundancy between different z planes of the data: cells are represented in multiple planes, and 
time-series belonging to the same cell must be found. Appropriate averaging or discarding of low signal to be included. The goal is to produce a combined data set of all time-series for all unique, non-artifact cells in the data set, with corresponding location coordinates. This is the *join_z_stacks.py* module. 

### analysis 
Here, following first the proposed analysis of calcium signals from **Nature Protocols 6:1 2011**, in *deltaF.py*. Once clean calcium signals are identified and isolated, we can start to look for clusters of related cells on the basis of the timing and characteristics of their time-series, and see if we can spot anything interesting. 


Note: this work had been put on the backburner for the moment. Possibly best to look at the Granger causality using the connectivipy package. 
