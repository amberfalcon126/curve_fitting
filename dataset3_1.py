import numpy as np
import matplotlib.pyplot as plt
import fileinput
from scipy.optimize import curve_fit

# to extract the data from the text file
file1 = open("dataset3.txt", "r")
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

#plotting the original data
plt.scatter(list_time, list_val,color = 'red')
#values of the constants for checking
h = float(6.6260715*(10**-34))
Kb = float(1.380649*(10**-23))
c = float(3*(10**8))

# definign a function to estimate the curve
def planck_eq(f,T):
    return 2*h*(f)**3/(c**2*(np.exp(h*f/(Kb*T)-1)))

#using curve_fit to get the parameter "T"
(popt, pcov) = curve_fit(planck_eq,list_time, list_val,p0=1000)
print(f"The temperature at which this graph was taken is : {popt} Kelvin")
T = popt
y = planck_eq(list_time,T)

plt.plot(list_time, y,color = 'blue')
plt.errorbar(list_time[::50], list_val[::50], yerr=abs(y - list_val)[::50], color='green')

plt.savefig("img_4.png")