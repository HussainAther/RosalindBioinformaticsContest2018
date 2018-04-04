f = open("/data/Lei_student/Hussain/ML/dm6/peakerror/40_mcc_lowmfold_highmfold.csv", "r")
o = open("/data/Lei_student/Hussain/ML/dm6/peakerror/40_mcc_lowmfold_highmfold.tsv", "w")

for i in f.readlines():
    o.write(i.replace(",", "\t"))
