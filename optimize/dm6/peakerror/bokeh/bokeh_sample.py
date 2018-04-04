import numpy as np

from bokeh.layouts import gridplot
from bokeh.plotting import figure, output_file, show

f40 = open("/data/Lei_student/Hussain/ML/dm6/peakerror/40_summary_uniq.csv", "r")
f30 = open("/data/Lei_student/Hussain/ML/dm6/peakerror/30_summary_uniq.csv", "r")
f20 = open("/data/Lei_student/Hussain/ML/dm6/peakerror/20_summary_uniq.csv", "r")
f10 = open("/data/Lei_student/Hussain/ML/dm6/peakerror/10_summary_uniq.csv", "r")

labels = []
mcc = []

count = 0
for i in f40.readlines():
    if count > 0:
        labels.append(40)
        mcc.append(i.split(",")[6])
    count += 1

count = 0
for i in f30.readlines():
    if count > 0:
        labels.append(30)
        mcc.append(i.split(",")[6])
    count += 1

count = 0
for i in f20.readlines():
    if count > 0:
        labels.append(20)
        mcc.append(i.split(",")[6])
    count += 1

count = 0
for i in f10.readlines():
    if count > 0:
        labels.append(10)
        mcc.append(i.split(",")[6])
    count += 1

s = figure(width=250, plot_height=250, title=None)
s.circle(labels, mcc)
show(s)
output_file("/data/Lei_student/Hussain/ML/dm6/peakerror/bokehgraph.html")
