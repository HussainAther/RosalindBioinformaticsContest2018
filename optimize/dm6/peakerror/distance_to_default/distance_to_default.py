import matplotlib.pyplot as plt
import numpy as np

f40 = open("/data/Lei_student/Hussain/ML/dm6/peakerror/40_mcc_llocal.csv", "r")
f30 = open("/data/Lei_student/Hussain/ML/dm6/peakerror/30_mcc_llocal.csv", "r")
f20 = open("/data/Lei_student/Hussain/ML/dm6/peakerror/20_mcc_llocal.csv", "r")
f10 = open("/data/Lei_student/Hussain/ML/dm6/peakerror/10_mcc_llocal.csv", "r")

distance_to_default = []
labels = []

count = 0
for i in f40.readlines():
    if count > 0:
        distance_to_default.append(float(i.split(",")[1]) - .7477454791039003)
        labels.append(40)
    count += 1

count = 0
for i in f30.readlines():
    if count > 0:
        distance_to_default.append(float(i.split(",")[1]) - .7023926834240052)
        labels.append(30)
    count += 1

count = 0
for i in f20.readlines():
    if count > 0:
        distance_to_default.append(float(i.split(",")[1]) - .734564190240499)
        labels.append(20)
    count += 1

count = 0
for i in f10.readlines():
    if count > 0:
        distance_to_default.append(float(i.split(",")[1]) - .8746081504702194)
        labels.append(10)
    count += 1

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
ax.set_title("Distance to default of each parameter combination")
plt.scatter(labels, distance_to_default)
ax.set_xlabel("Number of labels")
ax.set_ylabel("Parameter MCC - Default MCC")
fig.savefig("/data/Lei_student/Hussain/ML/dm6/peakerror/distance_to_default.png")
