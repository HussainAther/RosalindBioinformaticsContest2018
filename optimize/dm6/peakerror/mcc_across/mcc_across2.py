import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

f = "/data/Lei_student/Hussain/ML/dm6/peakerror/summary.csv"
o = "/data/Lei_student/Hussain/ML/dm6/peakerror/mcc_across/mcc_across2.png"

default_mcc = {}
optimal_mcc = {}

count = 0
with open(f) as file:
    for i in file.readlines():
        if count > 0:
            token = i.split(",")
            mcc = float(token[9])
            params = token[11]
            sample = token[13]
            if params == "no-ds50100005no-nl0.051000":
                default_mcc[sample] = mcc
            if sample in optimal_mcc:
                if mcc > optimal_mcc[sample]:
                    optimal_mcc[sample] = mcc
            else:
                optimal_mcc[sample] = mcc
        count += 1

distance_to_default = {}
for sample in optimal_mcc:
    distance_to_default[sample] = abs(optimal_mcc[sample] - default_mcc[sample])
keys = list(sorted(distance_to_default, key=distance_to_default.__getitem__, reverse=True))
distance_to_default_sorted = []
for key in keys:
    distance_to_default_sorted.append(distance_to_default[key])

celltype_antibody = {
    'SRR567586': 'BG3 Su(Hw)', 
    'lm06_kc_shep-gp_R1': 'Kc Shep', 
    'lm07_kc_shep-r5_R1': 'Kc Shep', 
    'lm08_kc_shep-r6_R1': 'Kc Shep', 
    'lm10_kc_shep-gp_R1': 'Kc Shep', 
    'lm32_kc_suhw_R1': 'Kc Su(Hw)', 
    'lm33_bg3_suhw_R1': 'BG3 Su(Hw)', 
    'lm34_bg3_shep-gp_R1': 'BG3 Shep', 
    'lm36_bg3_shep-r6_R1': 'BG3 Shep', 
    'lm37_kc_mod-gp_R1': 'Kc Mod(mdg4)', 
    'lm38_kc_mod-rb_R1': 'Kc Mod(mdg4)', 
    'lm43_bg3_mod-gp_R1': 'BG3 Mod(mdg4)', 
    'lm44_bg3_mod-rb_R1': 'BG3 Mod(mdg4)', 
    'sjl_kc_cp190_R1': 'Kc CP190', 
    'sjl_s2_shep_R1': 'S2 Shep', 
    'sjl_s3_cp190_R1': 'S3 CP190', 
    'sjl_s3_suhw_R1': 'S3 Su(Hw)', 
    'sjl_s3_shep_R1': 'S3 Shep', 
    'dc92_bg3_ctcf-56': 'BG3 CTCF', 
    'dc94_bg3_ctcf-59': 'BG3 CTCF'}

ca_list = []

for sample in default_mcc:
    ca_list.append(celltype_antibody[sample])

def autolabel(rects, peaklist):
    count = 0
    for rect in rects:
        height = rect.get_height()
        if height < 0:
            va = "top"
        else:
            va = "bottom"
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(peaklist[count]),
                ha='center', va=va,
                rotation=90,fontsize=12)
        count += 1

N = len(default_mcc)
ind = np.arange(N)

default_number_of_peaks = [
    3228, 17359, 20801, 4889, 
    22343, 5428, 16645, 5671, 
    5777, 5900, 5010, 969, 3050, 
    5757, 10699, 3564, 2405, 6501, 
    8575, 3365] # The number of peaks called with the default parameters for the samples sorted in order of decreasing distance_to_default for each sample

optimal_number_of_peaks = {
    "lm06_kc_shep-gp_R1" : [4552, 4546],
    "lm32_kc_suhw_R1" : 13799,
    "dc94_bg3_ctcf-59" : [19375, 19375, 19375, 19375, 19375, 19375, 19319, 19375, 19375, 19375, 19375, 19375, 19375],
    "lm44_bg3_mod-rb_R1" : 4440,
    "dc92_bg3_ctcf-56" : 22572,
    "lm34_bg3_shep-gp_R1" : 4979,
    "lm43_bg3_mod-gp_R1" : 13779,
    "lm33_bg3_suhw_R1" : 5497,
    "SRR567586" : 5492,
    "lm36_bg3_shep-r6_R1" : 5230,
    "lm37_kc_mod-gp_R1" : [4720, 4768],
    "lm07_kc_shep-r5_R1" : 1180,
    "lm08_kc_shep-r6_R1" : 3333,
    "lm38_kc_mod-rb_R1" : [5403, 5419, 5416, 5418, 5469],
    "sjl_s2_shep_R1" : 9233,
    "sjl_kc_cp190_R1" : 3596,
    "lm10_kc_shep-gp_R1" : 2862,
    "sjl_s3_suhw_R1" : 5783,
    "sjl_s3_cp190_R1" : [8927, 9623],
    "sjl_s3_shep_R1" : 3121} # The number of peaks called with the optimal parameters for the samples sorted in order of decreasing distance_to_default for each sample

optimal_number_of_peaks = [
    4549, 13799, 19371, 4440,
    22572, 4979, 13779, 5497,
    5492, 5230, 4744, 1180, 
    3333, 5425, 9233, 3596, 
    2862, 5783, 9275, 3121] # Same as before but averaged the samples that have more than one optimal combination

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
width = .35
rects1 = ax.bar(ind, [default_mcc[i] for i in keys], width, color="r")
rects2 = ax.bar(ind + width, [optimal_mcc[i] for i in keys], width, color="b")
autolabel(rects1, default_number_of_peaks)
autolabel(rects2, optimal_number_of_peaks)
ax.set_xticks(ind + width)
ax.set_xticklabels([celltype_antibody[i] for i in keys], rotation=90)
plt.yticks(fontsize=14)
# ax.plot(ind, distance_to_default_sorted, color="g") 
ax.set_title("Default and optimal MCC for celltype-antibody combos", fontsize=24)
ax.set_xlabel("Celltype-antibody", fontsize=18)
ax.set_ylabel("MCC", fontsize=18)
ax.legend((rects1[0], rects2[0]), ("Default MCC", "Optimal MCC"), fontsize=14, loc=4)
fig.tight_layout()
plt.savefig(o)

