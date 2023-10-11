import numpy as np
import matplotlib.pyplot as plt
import fileinput
from scipy.optimize import curve_fit

# to extract the data from the text file
file1 = open("dataset1.txt", "r")
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
plt.scatter(list_time, list_val, color = 'red')
#defining the estimated curve
def line(x,m,c):
    return (m*x + c)
# using lstsq
M = np.column_stack([list_time, np.ones(len(list_time))])
(mopt, copt), _, _, _ = np.linalg.lstsq(M, list_val, rcond = None)       #this line does essentially what curve_fit does

#using curve_fit

# popt , pcov = curve_fit(line, list_time, list_val, p0 = [3, 1.6]) # popt = parameter_optimum;pcov = parameter covariance
# mopt, copt = popt

print(f"The estimated equation is {mopt} t + {copt}")
y = line(list_time, mopt, copt)
#plotting the curve and errobars
plt.plot(list_time, y, color = 'blue')
plt.errorbar(list_time[::25], list_val[::25], yerr  = abs(y - list_val)[::25], color = 'green')
plt.legend(["points","estm plot","errorbars"])
plt.savefig("img_1.png")