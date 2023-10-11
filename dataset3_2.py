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

#using the Temp value calculated in the last part
T = 3891.44650092
## plotting using method 1 and taking all f,Kb, h and T to be parameters
def planck_eq(f,T,h,c,Kb):
    return 2*h*(f)**3/(c**2*(np.exp(h*f/(Kb*T)-1)))

(popt, pcov) = curve_fit(planck_eq,list_time, list_val, p0 = [5000,6.6260715*(10**-34),3*(10**8),1.380649*(10**-23),])
T,h,c,Kb = popt
print(f"The temperature at which this graph was taken is : {T} Kelvin")
print(f"h:{h},c:{c},Kb:{Kb}")
y = planck_eq(list_time,T,h,c,Kb)

plt.plot(list_time,y,color='blue')

plt.savefig("img_6.png")
#  plotting using method 2 and taking only one of the three unknowns  to be parameters

# def model_c(f,c):
#     h = float(6.6260715 * (10 ** -34))
#     Kb = float(1.380649 * (10 ** -23))
#     T = 3891.44650092
#     return 2*h*(f)**3/(c**2*(np.exp(h*f/(Kb*T)-1)))
#
# (popt,pocv) = curve_fit(model_c, list_time, list_val )
# c = popt
# print(f"c:{c}")
# y_c = model_c(list_time, c)
#
# def model_h(f,h):
#     c = float(3 * (10 ** 8))
#     Kb = float(1.380649 * (10 ** -23))
#     T = 3891.44650092
#     return 2*h*(f)**3/(c**2*(np.exp(h*f/(Kb*T)-1)))
#
# (popt,pocv) = curve_fit(model_h, list_time, list_val, p0 = [6*10**-34] )
# h = popt
# print(f"h:{h}")
# y_h = model_h(list_time, h)
#
# def model_Kb(f,Kb):
#     h = float(6.6260715 * (10 ** -34))
#     c = float(3 * (10 ** 8))
#     T = 3891.44650092
#     return 2*h*(f)**3/(c**2*(np.exp(h*f/(Kb*T)-1)))
#
# (popt,pocv) = curve_fit(model_Kb, list_time, list_val,p0 = [10**-23] )
# Kb =  popt
# print(f"Kb:{Kb}")
# y_Kb = model_Kb(list_time, Kb)
#
# plt.plot(list_time, y_c,color = 'blue')
# plt.plot(list_time, y_h,color = 'green')
# plt.plot(list_time, y_Kb,color = 'yellow')
# plt.legend(["points","cest","hest","Kbest"])
#
# plt.savefig("img_5.png")
#plt.errorbar(list_time[::50], list_val[::50], yerr=abs(y - list_val)[::50], color='green')


