'''some generally useful set ups for plotting'''
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl


def threed_points_plot(data):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(data[:,1], data[:,2], data[:,3], c='r', marker='o')

    plt.show()

if __name__ == '__main__':
