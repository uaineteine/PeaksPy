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
    plt.plot(xp, yp, color='b', linewidth=0, marker=".", markersize=7, label="maxpeak")
    plt.plot(xpneg, ypneg, color='g', linewidth=0, marker=".", markersize=7, label="minpeak")
    plt.legend()
    plt.title("Peaks find example")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

def TestModule():
    x = np.linspace(0, 100, 1000)
    y = np.sin(x) + 0.5 * np.cos(0.5*x)*np.sin(3*x)
    PlotPeaks(x, y)

def FD(xaxis, yaxis):#forward difference
    n = len(xaxis)
    new = n-1
    xnew = [0]*new
    ynew = [0]*new
    for i in range(0, new):
        xnew[i] = xaxis[i+1]
        ynew[i] = yaxis[i+1]-yaxis[i]
    return np.array(xnew), np.array(ynew)

def FirstPointUnder(xaxis, yaxis, underThis):
    for i, val in enumerate(yaxis):
        if val < underThis:
            return i

def LastPointUnder(xaxis, yaxis, aboveThis):#last point so do it in reverse:
    n = len(xaxis)
    for i in range(0, n):
        k = n - 1 - i #my new index counting down
        if yaxis[k] < aboveThis:
            return k
#run module
#TestModule()