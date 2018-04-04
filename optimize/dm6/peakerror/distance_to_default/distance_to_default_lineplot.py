from scipy.stats import norm
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set_color_codes()

# Input the frequency files of distance to default and output a lineplot consolidating all four

f40 = open("/data/Lei_student/Hussain/ML/dm6/peakerror/distance_to_default_fourthcolumn.csv", "r")
f30 = open("/data/Lei_student/Hussain/ML/dm6/peakerror/distance_to_default_thirdcolumn.csv", "r")
f20 = open("/data/Lei_student/Hussain/ML/dm6/peakerror/distance_to_default_secondcolumn.csv", "r")
f10 = open("/data/Lei_student/Hussain/ML/dm6/peakerror/distance_to_default_firstcolumn.csv", "r")
output = "/data/Lei_student/Hussain/ML/dm6/peakerror/distance_to_default_lineplot.png"

f40_freq = []
f30_freq = []
f20_freq = []
f10_freq = []

for line in f40.readlines():
    f40_freq.append(float(line.replace("\n", "")))
for line in f30.readlines():
    f30_freq.append(float(line.replace("\n", "")))
for line in f20.readlines():
    f20_freq.append(float(line.replace("\n", "")))
for line in f10.readlines():
    f10_freq.append(float(line.replace("\n", "")))

fig = plt.figure(figsize=(10, 8))
ax = sns.distplot(f40_freq, color="y", fit=norm, fit_kws={"color":"y"}, label="40 labels", kde=False)
ax = sns.distplot(f30_freq, color="r", fit=norm, fit_kws={"color":"r"}, label="30 labels", kde=False) 
ax = sns.distplot(f20_freq, color="b", fit=norm, fit_kws={"color":"b"}, label="20 labels", kde=False)
ax = sns.distplot(f10_freq, color="g", fit=norm, fit_kws={"color":"g"}, label="10 labels", kde=False) 
ax.set_xlabel("Parameter MCC - Default MCC")
ax.set_ylabel("Frequency")
ax.legend()
fig.savefig(output)
