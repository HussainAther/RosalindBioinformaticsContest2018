f = open("/data/Lei_student/Hussain/ML/dm6/peakerror/summary.csv", "r")

max_mcc = {}

for i in f.readlines():
    mcc = i.split(",")[9]
    sample = i.split(",")[13]
    if sample in max_mcc:
        if mcc > max_mcc[sample]:
            max_mcc[sample] = mcc
    else:
        max_mcc[sample] = mcc
print(max_mcc)
print(len(max_mcc))

