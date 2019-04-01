import numpy as numpy
from scipy.signal import find_peaks
import matplotlib.pyplot as plt#might delete this after testing

def FindPeaksExt(xaxis, yaxis):  #np in please, extended gives indexes too
    indexes = find_peaks(yaxis)#assuming a nice smooth signal
    indexes = indexes[0]
    xp = xaxis.take[indexes]
    yp = xaxis.take[indexes]
    return xp, yp, indexes

def FindPeaks(xaxis, yaxis): #don't return indexes
    xp, yp, ind = FindPeaksExt(xp, yp)
    return xp, yp   #reduced return