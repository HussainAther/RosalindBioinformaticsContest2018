import numpy as np

from bokeh.layouts import gridplot
from bokeh.plotting import figure, output_file, show

flowmfold = open("/data/Lei_student/Hussain/ML/dm6/peakerror/40_mcc_lowmfold.csv", "r")
fhighmfold = open("/data/Lei_student/Hussain/ML/dm6/peakerror/40_mcc_highmfold.csv", "r")
fqvalue = open("/data/Lei_student/Hussain/ML/dm6/peakerror/40_mcc_qvalue.csv", "r")
fllocal = open("/data/Lei_student/Hussain/ML/dm6/peakerror/40_mcc_llocal.csv", "r")
fslocal = open("/data/Lei_student/Hussain/ML/dm6/peakerror/40_mcc_slocal.csv", "r")

output_file("/data/Lei_student/Hussain/ML/dm6/peakerror/parameter_visual.file")

lowmfold = []
lowmfold_mcc = []
highmfold = []
highmfold_mcc = []
qvalue = []
qvalue_mcc = []
llocal = []
llocal_mcc = []
slocal = []
slocal_mcc = []

count = 0
for i in flowmfold.readlines():
    if count > 0:
        lowmfold.append(i.split(",")[0])
        lowmfold_mcc.append(i.split(",")[1])
    count += 1
for i in fhighmfold.readlines():
    if count > 0:
        highmfold.append(i.split(",")[0])
        highmfold_mcc.append(i.split(",")[1])
    count += 1
for i in fqvalue.readlines():
    if count > 0:
        qvalue.append(i.split(",")[0])
        qvalue_mcc.append(i.split(",")[1])
    count += 1
for i in fslocal.readlines():
    if count > 0:
        slocal.append(i.split(",")[0])
        slocal_mcc.append(i.split(",")[1])
    count += 1
for i in fllocal.readlines():
    if count > 0:
        llocal.append(i.split(",")[0])
        llocal_mcc.append(i.split(",")[1])
    count += 1

s1 = figure(width=250, plot_height=250, title=None)
s1.circle(lowmfold, lowmfold_mcc)

s2 = figure(width=250, plot_height=250, title=None)
s2.circle(highmfold, highmfold_mcc)

s3 = figure(width=250, plot_height=250, title=None)
s3.circle(qvalue, qvalue_mcc)

s4 = figure(width=250, plot_height=250, title=None)
s4.circle(slocal, slocal_mcc)

s5 = figure(width=250, plot_height=250, title=None)
s5.circle(llocal, llocal_mcc)

p = gridplot([[s1, s2, s3, s4, s5]], toolbar_location=None)

show(p)
