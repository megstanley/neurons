# neurons
Python-based analysis of multiple neuron (larval zebrafish) time-series data. 

This is currently **very much** a work in progress. 

### data_cleaning###
Module to do initial cleaning of data. So far that includes removing data that contains low signal, indicating it is an 
artifact, with find_low_baseline and removing those points that are edge of pixel array artifacts with find_edges.

### preprocessing ###
Here, working on removing the redundancy between different z planes of the data: cells are represented in multiple planes, and 
time-series belonging to the same cell must be found. Appropriate averaging or discarding of low signal to be included. The goal
is to produce a combined data set of all time-series for all unique, non-artifact cells in the data set, with corresponding 
location coordinates. 

### analysis ###
Here, following first the proposed analysis of calcium signals from Nature Protocols 6:1 2011. Once clean calcium signals
are identified and isolated, we can start to look for clusters of related cells on the basis of the timing and characteristics of their time-series. 
