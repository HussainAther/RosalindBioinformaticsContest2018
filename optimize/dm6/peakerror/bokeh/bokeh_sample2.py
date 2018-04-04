import numpy as np

from bokeh.plotting import *
from bokeh.models import ColumnDataSource

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

output_file("/data/Lei_student/Hussain/ML/dm6/peakerror/bokeh_sample2.html")
source = ColumnDataSource(data=dict(x=labels, y=mcc))


