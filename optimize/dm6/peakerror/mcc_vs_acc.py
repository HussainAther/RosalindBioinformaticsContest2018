import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

f = "/data/Lei_student/Hussain/ML/dm6/peakerror/summary.csv"
o = "/data/Lei_student/Hussain/ML/dm6/peakerror/mcc_vs_acc.png"

mcc = []
acc = []

count = 0
with open(f) as file:
    for i in file.readlines():
        if count > 0:
            token = i.split(",")
            acc.append(float(token[0]))
            mcc.append(float(token[9]))
        count += 1

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
plt.scatter(acc, mcc)
ax.set_title("MCC vs. Accuracy of default and optimal parameter combinations", fontsize=18)
ax.set_xlabel("Accuracy", fontsize=18)
ax.set_ylabel("MCC", fontsize=18)
fig.savefig(o)

