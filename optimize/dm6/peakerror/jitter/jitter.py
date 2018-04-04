from scipy.stats import norm
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

f = open("/data/Lei_student/Hussain/ML/dm6/peakerror/summary.csv", "r")
o_sl_ll = "/data/Lei_student/Hussain/ML/dm6/peakerror/mcc_slocal_llocal.png"
o_sl_qv = "/data/Lei_student/Hussain/ML/dm6/peakerror/mcc_slocal_qvalue.png"
o_sl_hm = "/data/Lei_student/Hussain/ML/dm6/peakerror/mcc_slocal_highmfold.png"
o_sl_lm = "/data/Lei_student/Hussain/ML/dm6/peakerror/mcc_slocal_lowmfold.png"
o_ll_qv = "/data/Lei_student/Hussain/ML/dm6/peakerror/mcc_llocal_qvalue.png"
o_ll_lm = "/data/Lei_student/Hussain/ML/dm6/peakerror/mcc_llocal_lowmfold.png"
o_ll_hm = "/data/Lei_student/Hussain/ML/dm6/peakerror/mcc_llocal_highmfold.png"
o_qv_hm = "/data/Lei_student/Hussain/ML/dm6/peakerror/mcc_qvalue_highmfold.png"
o_qv_lm = "/data/Lei_student/Hussain/ML/dm6/peakerror/mcc_qvalue_lowmfold.png"
o_hm_lm = "/data/Lei_student/Hussain/ML/dm6/peakerror/mcc_highmfold_lowmfold.png"

mcc = []
slocal = []
llocal = []
qvalue = []
accuracy = []
highmfold = []
lowmfold = []

def stdev(num):
    return float(np.random.randn(1)*np.random.choice([1, -1])*float(num)*.01)

d = []
d1 = pd.read_csv("/data/Lei_student/Hussain/ML/dm6/peakerror/summary.csv")

count = 0
for i in f.readlines():
    if count > 0:
        temp_dict = {}
        accuracy.append(float(i.split(",")[0]))
        temp_dict["accuracy"] = float(i.split(",")[0])
        mcc.append(float(i.split(",")[9]))
        temp_dict["mcc"] = float(i.split(",")[9])
        highmfold.append(float(i.split(",")[6]) + stdev(i.split(",")[6]))
        temp_dict["highmfold"] = float(float(i.split(",")[6]) + stdev(i.split(",")[6]))
        llocal.append(float(i.split(",")[7]) + stdev(i.split(",")[7]))
        temp_dict["llocal"] = float(float(i.split(",")[7]) + stdev(i.split(",")[7]))
        lowmfold.append(float(i.split(",")[8]) + stdev(i.split(",")[8]))
        temp_dict["lowmfold"] = float(float(i.split(",")[8]) + stdev(i.split(",")[8]))
        qvalue.append(float(i.split(",")[11]) + stdev(i.split(",")[11]))
        temp_dict["qvalue"] = float(float(i.split(",")[11]) + stdev(i.split(",")[11]))
        slocal.append(float(i.split(",")[13]) + stdev(i.split(",")[13]))
        temp_dict["slocal"] = float(float(i.split(",")[13]) + stdev(i.split(",")[13]))
        d.append(temp_dict)
    count += 1

d = pd.DataFrame(d)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
ax.set_title("MCC of slocal vs. llocal")
ax.scatter(llocal, slocal, c=mcc)
sns.lmplot("llocal", "slocal", data=d, fit_reg=False, hue="mcc", legend=False)
ax.set_xlabel("llocal")
ax.set_ylabel("slocal")
plt.savefig(o_sl_ll)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
ax.set_title("MCC of slocal vs. qvalue")
ax.scatter(qvalue, slocal, c=mcc)
sns.lmplot("qvalue", "slocal", data=d, fit_reg=False, hue="mcc", legend=False)
ax.set_xlabel("qvalue")
ax.set_ylabel("slocal")
plt.savefig(o_sl_qv)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
ax.set_title("MCC of slocal vs. highmfold")
plt.scatter(highmfold, slocal, c=mcc)
sns.lmplot("highmfold", "slocal", data=d, fit_reg=False, hue="mcc", legend=False)
ax.set_xlabel("highmfold")
ax.set_ylabel("slocal")
plt.savefig(o_sl_hm)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
ax.set_title("MCC of slocal vs. lowmfold")
plt.scatter(lowmfold, slocal, c=mcc)
sns.lmplot("lowmfold", "slocal", data=d, fit_reg=False, hue="mcc", legend=False)
ax.set_xlabel("lowmfold")
ax.set_ylabel("slocal")
plt.savefig(o_sl_lm)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
ax.set_title("MCC of llocal vs. qvalue")
plt.scatter(qvalue, llocal, c=mcc)
sns.lmplot("qvalue", "llocal", data=d, fit_reg=False, hue="mcc", legend=False)
ax.set_xlabel("qvalue")
ax.set_ylabel("llocal")
plt.savefig(o_ll_qv)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
ax.set_title("MCC of llocal vs. lowmfold")
plt.scatter(lowmfold, llocal, c=mcc)
sns.lmplot("lowmfold", "llocal", data=d, fit_reg=False, hue="mcc", legend=False)
ax.set_xlabel("lowmfold")
ax.set_ylabel("llocal")
plt.savefig(o_ll_lm)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
ax.set_title("MCC of llocal vs. highmfold")
plt.scatter(highmfold, llocal, c=mcc)
sns.lmplot("highmfold", "llocal", data=d, fit_reg=False, hue="mcc", legend=False)
ax.set_xlabel("llocal")
ax.set_ylabel("highmfold")
plt.savefig(o_ll_hm)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
ax.set_title("MCC of qvalue vs. highmfold")
plt.scatter(highmfold, qvalue, c=mcc)
sns.lmplot("highmfold", "qvalue", data=d, fit_reg=False, hue="mcc", legend=False)
ax.set_xlabel("highmfold")
ax.set_ylabel("qvalue")
plt.savefig(o_qv_hm)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
ax.set_title("MCC of qvalue vs. lowmfold")
plt.scatter(lowmfold, qvalue, c=mcc)
sns.lmplot("lowmfold", "qvalue", data=d, fit_reg=False, hue="mcc", legend=False)
ax.set_xlabel("lowmfold")
ax.set_ylabel("qvalue")
plt.savefig(o_qv_lm)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
ax.set_title("MCC of highmfold vs. lowmfold")
plt.scatter(lowmfold, highmfold, c=mcc)
sns.lmplot("lowmfold", "highmfold", data=d, fit_reg=False, hue="mcc", legend=False)
ax.set_xlabel("lowmfold")
ax.set_ylabel("highmfold")
plt.savefig(o_hm_lm)
