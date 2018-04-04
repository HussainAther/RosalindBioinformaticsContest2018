import pandas as pd

f = open("/data/Lei_student/Hussain/ML/dm6/peakerror/summary.tsv", "r")
o = open("/data/Lei_student/Hussain/ML/dm6/peakerror/summary.csv", "w")

for i in f.readlines():
    o.write(",".join(i.split("\t")[1:]))
