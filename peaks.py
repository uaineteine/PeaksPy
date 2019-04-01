import numpy as np
from scipy.signal import find_peaks
import matplotlib.pyplot as plt#might delete this after testing

def FindPeaksExt(xaxis, yaxis):  #np in please, extended gives indexes too
    indexes = find_peaks(yaxis)#assuming a nice smooth signal
    indexes = indexes[0]
    xp = xaxis.take(indexes)
    yp = yaxis.take(indexes)
    return xp, yp, indexes

def FindPeaks(xaxis, yaxis): #don't return indexes
    xp, yp, ind = FindPeaksExt(xaxis, yaxis)
    return xp, yp   #reduced return

def PlotPeaks(xaxis, yaxis):
    xp, yp = FindPeaks(xaxis, yaxis)
    xpneg, ypneg = FindPeaks(xaxis, -yaxis)
    ypneg = -ypneg
    
    plt.figure()
    plt.plot(xaxis, yaxis, color='r', label="data")
    plt.plot(xp, yp, color='b', linewidth=0, marker=".", markersize=7, label="pospeak")
    plt.plot(xpneg, ypneg, color='g', linewidth=0, marker=".", markersize=7, label="negpeak")
    plt.legend()
    plt.title("Peaks find example")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

def TestModule():
    x = np.linspace(0, 100, 1000)
    y = np.sin(x) + 0.5 * np.cos(0.5*x)
    PlotPeaks(x, y)

#run module
TestModule()