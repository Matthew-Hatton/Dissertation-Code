
import numpy as np
import matplotlib.pyplot as plt

def scalefactor(scales):
    scalefactorlist = []
    for i in range(scales):
        scalefactorlist.append([2**i])
    scalefactors = []
    for x in scalefactorlist:
        for item in x:     
            scalefactors.append(item)
    scalefactors.insert(0,0)
    scalefactors.pop(1)
    return scalefactors
    

        
scalefactors = scalefactor(4) #Input how many scales



logscalefactors = []
for i in range(len(scalefactors)):
    logscalefactors.append(np.log(scalefactors[i]))
logscalefactors[0] = 0


N = [20,44,79,225] #Input number of elements inside boxes
logN = []
for y in N:
    logN.append(np.log(y))


logscalefactorsarr = np.array(logscalefactors)
logNarr = np.array(logN)

plt.plot(logscalefactorsarr,logNarr,'o')
plt.xlabel('Logarithmic Scale factor')
plt.ylabel('Logarithmic Number of boxes counted')
m, b = np.polyfit(logscalefactorsarr,logNarr,1)
print('******************')
print("The Fractal dimension is",m)
print('******************')
plt.plot(logscalefactorsarr,m*logscalefactorsarr + b)
plt.show()
