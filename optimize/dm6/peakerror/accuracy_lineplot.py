from scipy.stats import norm
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Plot the accuracy for each subset of labels

f40 = open("/data/Lei_student/Hussain/ML/dm6/peakerror/40_summary.csv", "r")
f30 = open("/data/Lei_student/Hussain/ML/dm6/peakerror/30_summary.csv", "r")
f20 = open("/data/Lei_student/Hussain/ML/dm6/peakerror/20_summary.csv", "r")
f10 = open("/data/Lei_student/Hussain/ML/dm6/peakerror/10_summary.csv", "r")
output = "/data/Lei_student/Hussain/ML/dm6/peakerror/accuracy_lineplot.png"

f40_accuracy = []
f30_accuracy = []
f20_accuracy = []
f10_accuracy = []

count = 0
for i in f40.readlines():
    if count > 1:
        f40_accuracy.append(float(i.split(",")[0]))
    count +=1
count = 0
for i in f30.readlines():
    if count > 1:
        f30_accuracy.append(float(i.split(",")[0]))
    count +=1
count = 0
for i in f20.readlines():
    if count > 1:
        f20_accuracy.append(float(i.split(",")[0]))
    count +=1
count = 0
for i in f10.readlines():
    if count > 1:
        f10_accuracy.append(float(i.split(",")[0]))
    count +=1

fig = plt.figure(figsize=(10, 8))
set_context("talk")
ax = sns.distplot(f40_accuracy, color="y", fit=norm, fit_kws={"color":"y"}, label="40 labels", kde=False)
ax = sns.distplot(f30_accuracy, color="r", fit=norm, fit_kws={"color":"r"}, label="30 labels", kde=False) 
ax = sns.distplot(f20_accuracy, color="b", fit=norm, fit_kws={"color":"b"}, label="20 labels", kde=False)
ax = sns.distplot(f10_accuracy, color="g", fit=norm, fit_kws={"color":"g"}, label="10 labels", kde=False) 
ax.set_ylabel("Frequency")
ax.set_xlabel("Accuracy (Percent correct labels)")
ax.legend()
fig.savefig(output)
