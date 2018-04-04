import matplotlib.pyplot as plt
import numpy as np
f40 = open("/data/Lei_student/Hussain/ML/dm6/peakerror/40_summary_uniq.csv", "r") 
f30 = open("/data/Lei_student/Hussain/ML/dm6/peakerror/30_summary_uniq.csv", "r") 
f20 = open("/data/Lei_student/Hussain/ML/dm6/peakerror/20_summary_uniq.csv", "r") 
f10 = open("/data/Lei_student/Hussain/ML/dm6/peakerror/10_summary_uniq.csv", "r") 
o = open("/data/Lei_student/Hussain/ML/dm6/peakerror/distance_to_default_fourthcolumn.csv", "w")
d = {}

count = 0
for i in f10.readlines():
    if count > 0:
        key = [i.split(",")[2:6]] + [i.split(",")[8]] + [i.split(",")[10]]
        d[str(key)] = str(float(i.split(",")[6]) - .8746081504702194)
    count += 1
count = 0
for i in f20.readlines():
    if count > 0:
        key = [i.split(",")[2:6]] + [i.split(",")[8]] + [i.split(",")[10]]
        d[str(key)] += " " + str(float(i.split(",")[6]) - .734564190240499)
    count += 1
count = 0
for i in f30.readlines():
    if count > 0:
        key = [i.split(",")[2:6]] + [i.split(",")[8]] + [i.split(",")[10]]
        d[str(key)] += " " + str(float(i.split(",")[6]) - .7023926834240052)
    count += 1
count = 0
for i in f40.readlines():
    if count > 0:
        key = [i.split(",")[2:6]] + [i.split(",")[8]] + [i.split(",")[10]]
        d[str(key)]+= " " + str(float(i.split(",")[6]) - .7477454791039003)
    count += 1

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
sorted_d = list(sorted(d, key=d.__getitem__))
count = 0
for i in sorted_d:
    if count in range(500, 1000):
        plt.plot(np.arange(10, 50, 10), d[i].split(" "), alpha=1)
    else:
        plt.plot(np.arange(10, 50, 10), d[i].split(" "), alpha=.02, color="gray")
    count += 1
ax.set_title("Distance to default of each parameter combination")
ax.set_xlabel("Number of labels")
ax.set_ylabel("Parameter MCC - Default MCC")
fig.savefig("/data/Lei_student/Hussain/ML/dm6/peakerror/distance_to_default_line_second500.png")

for i in d:
    o.write(d[i].split(" ")[3] + "\n")
#    o.write(",".join(d[i].split(" ")) + "\n")
