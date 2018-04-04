import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

f = "/data/Lei_student/Hussain/ML/dm6/peakerror/summary.csv"
#o = "/data/Lei_student/Hussain/ML/dm6/peakerror/mcc_sort.png"
#o = "/data/Lei_student/Hussain/ML/dm6/peakerror/tptnfpfn.png"
o = "/data/Lei_student/Hussain/ML/dm6/peakerror/mcc.png"

mcc_dict = {}

with open(f) as file:
    for i in file.readlines():
        mcc = i.split(",")[9]
        sample = i.split(",")[12]
        if sample not in mcc_dict:
            mcc_dict[sample] = [mcc]
        else:
            mcc_dict[sample].append(mcc)

#d = pd.DataFrame.from_csv(f)
#sorted_mcc=d.sort_values("mcc")["mcc"]
#sorted_tp=d.sort_values("tp")["tp"]
#sorted_tn=d.sort_values("tn")["tn"]
#sorted_fp=d.sort_values("fp")["fp"]
#sorted_fn=d.sort_values("fn")["fn"]

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
#ax.set_title("MCC sorted from lowest to highest")
#ax.set_title("tp, tn, fp, fn sorted from lowest to highest")
#plt.scatter(range(20250),sorted_mcc, s=5)
#plt.scatter(range(20250),rando,c="b")
#plt.scatter(range(20250),sorted_tp, c="b", s=5)
#plt.scatter(range(20250),sorted_tn, c="g", s=5)
#plt.scatter(range(20250),sorted_fp, c="y", s=5)
#plt.scatter(range(20250),sorted_fn, c="r", s=5)
plt.scatter(range(2250), mcc_dict["SRR567586"], c="#a6cee3", label="bg3 suhw", s=5)
plt.scatter(range(2250, 4500), mcc_dict["lm32_kc_suhw_R1"], c="#1f78b4", label="kc suhw", s=5)
plt.scatter(range(4500, 6750), mcc_dict["sjl_kc_cp190_R1"], c="#b2df8a", label="kc cp190", s=5)
plt.scatter(range(6750, 9000), mcc_dict["sjl_s2_shep_R1"], c="#33a02c", label="s2 shep", s=5)
plt.scatter(range(9000, 11250), mcc_dict["sjl_s3_cp190_R1"], c="#fb9a99", label="s3 cp190", s=5)
plt.scatter(range(11250, 13500), mcc_dict["sjl_s3_suhw_R1"], c="#e31a1c", label="s3 suhw", s=5)
plt.scatter(range(13500, 15750), mcc_dict["sjl_s3_shep_R1"], c="#fdbf6f", label="s3 shep", s=5)
plt.scatter(range(15750, 18000), mcc_dict["dc92_bg3_ctcf-56"], c="#ff7f00", label="bg3 ctcf", s=5)
plt.scatter(range(18000, 20250), mcc_dict["dc94_bg3_ctcf-59"], c="#cab2d6", label="bg3 ctcf", s=5)
ax.set_title("MCC for celltype-antibody combos")
ax.set_xlabel("sample", fontsize=18)
ax.set_ylabel("mcc", fontsize=18)
#ax.set_ylabel("tp, tn, fp, fn count")
ax.legend(fontsize=10)
plt.savefig(o)
