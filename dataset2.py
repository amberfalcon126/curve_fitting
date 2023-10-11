import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# to extract the data from the text file
file1 = open("dataset2.txt", "r")
list1 = file1.readlines()
file1.close()
list2 = []
list_time = []
list_val = []
for row in list1:
    list2.append(row.split())
for i in range(len(list2)):
    list_time.append(float(list2[i][0]))
    list_val.append(float(list2[i][1]))
list_time = np.array(list_time)
#plotting the actual data
plt.scatter(list_time, list_val, color='red')
# calculating the time period and the fundamental frequency
store = []
for i in range(len(list_time)):
    if abs(list_val[i]) <0.15:
        store.append(list_time[i])
    if len(store) ==2:
        break
    else:
        continue
time = abs(store[0] -store[1])          # the time calculated here is the time period so the frequency becomes 2pi/time
f = 2*np.pi /time
def wave2(x, a1, a2, a3, f1, c):
    return a1 * np.sin(f1*x) + a2*np.sin(5*f1 * x) + a3*np.sin(3*f1*x) + c

# # using the lstsq method
# M = np.column_stack([np.sin(f*list_time),np.sin(5*f*list_time),np.sin(3*f*list_time), np.ones(len(list_time))])
# (a1, a2,a3,c), _, _, _ = np.linalg.lstsq(M, list_val, rcond = None)
# print(f"The equation of the curve is : {a1}sin({f}x) + {a2}sin({5*f}x) + {a3}sin({3*f}*x) + {c}")
# #defining a function to estimate the curve

#
# y1 = wave2(list_time, a1, a2, a3, f, c)
# #plotting the curve and the errorbars
# plt.plot(list_time, y1, color = 'blue')
#plt.errorbar(list_time[::25], list_val[::25], yerr=abs(y1 - list_val)[::25], color='green')

#plotting using curve_fit
(popt2, pocv2) = curve_fit(wave2, list_time, list_val,p0 = [ 2, 1, 5, 3, -0.02587517])
a12, a22, a32, f12, c2= popt2
print(f"The frequency calculated using curve_fit is : {f12}")
y2 = wave2(list_time, a12, a22, a32, f12, c2)
plt.plot(list_time, y2, color = 'black')
plt.errorbar(list_time[::25], list_val[::25], yerr=abs(y2 - list_val)[::25], color='green')

plt.legend(["points", "estm plot", "errorbars"], loc = "lower center")


plt.savefig("img_3.png")
