from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection='3d')

# # Data for a three-dimensional line
#zline = np.linspace(0, 15, 1000)
#xline = np.sin(zline)
#yline = np.cos(zline)
#ax.plot3D(xline, yline, zline, 'gray')
# # Data for three-dimensional scattered points
#zdata = 15 * np.random.random(100)
#xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
#ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
#ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens');

xdata = []
ydata = []
zdata = []
count = 0
f = open("/data/Lei_student/Hussain/ML/dm6/peakerror/40_mcc_llocal_qvalue.csv", "r")
for i in f.readlines():
    if count > 0:
        xdata.append(float(i.split(",")[0]))
        ydata.append(float(i.split(",")[1]))
        zdata.append(float(i.split(",")[2]))
    count += 1
#xdata, ydata = np.meshgrid(xdata, ydata)
ax.scatter3D(xdata, ydata, zdata, c=zdata) #Plot the two parameters on x and y with mcc as z
ax.scatter3D(10000, .05, .7477454791039003, c=(1,0,0), s=10, marker="*") #Plot the default parameters mcc
ax.set_xlabel("llocal")
ax.set_ylabel("qvalue")
ax.set_zlabel("mcc")
#ax.view_init(50, 35)
#ax.contour3D(xdata, ydata, zdata, 50, cmap="binary")
fig.savefig("/data/Lei_student/Hussain/ML/dm6/peakerror/40_mcc_llocal_qvalue.png")
