import scipy as sp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

sns.set()

f_ca = "/data/Lei_student/Hussain/ML/dm6/peakerror/optimal/optimal_ca.csv"
f_sample = "/data/Lei_student/Hussain/ML/dm6/peakerror/optimal/optimal_sample.csv"
o_ca_h = "/data/Lei_student/Hussain/ML/dm6/peakerror/hamming/ca_hamming.png"
o_sample_h = "/data/Lei_student/Hussain/ML/dm6/peakerror/hamming/sample_hamming.png"

df_ca = pd.DataFrame.from_csv(f_ca)
df_sample = pd.DataFrame.from_csv(f_sample)

q_value = [.03, .04, .05, .06, .07]
slocal = [500, 1000, 1500]
llocal = [5000, 10000, 15000]
highmfold = [30, 40, 50, 60, 70]
lowmfold = [3, 4, 5, 6, 7]

x_ca = [] # List of dictionaries with binary heatmap values
x_sample = []

x_ca_labels = []

for index, row in df_ca.iterrows():
    temp_dict = {}
    temp_dict["ca"] = row["celltype"] + "_" + row["antibody"]
    temp_dict["q_value_" + str(row["q_value"])] = 1.0
    temp_dict["slocal_" + str(row["slocal"])] = 1.0
    temp_dict["llocal_" + str(row["llocal"])] = 1.0
    temp_dict["highmfold_" + str(row["highmfold"])] = 1.0
    temp_dict["lowmfold_" + str(row["lowmfold"])] = 1.0
    x_ca.append(temp_dict)

for index, row in df_sample.iterrows():
    temp_dict = {}
    temp_dict["samples"] = row["sample"]
    temp_dict["q_value_" + str(row["q_value"])] = 1.0
    temp_dict["slocal_" + str(row["slocal"])] = 1.0
    temp_dict["llocal_" + str(row["llocal"])] = 1.0
    temp_dict["highmfold_" + str(row["highmfold"])] = 1.0
    temp_dict["lowmfold_" + str(row["lowmfold"])] = 1.0
    x_sample.append(temp_dict)

x_ca_df = pd.DataFrame(x_ca) # Convert the lists to DataFrames and add zero values
x_sample_df = pd.DataFrame(x_sample)

x_ca_df.index = x_ca_df["ca"] # Index the DataFrames by their labels
x_sample_df.index = x_sample_df["samples"]

x_ca_df = x_ca_df.sort_values(x_ca_df.columns.tolist()).fillna(0.0) # Sort them by columns and relpace Na with zero
x_sample_df = x_sample_df.sort_values(x_sample_df.columns.tolist()).fillna(0.0)

x_ca_df2 = x_ca_df.drop(["ca"], axis=1)
x_sample_df2 = x_sample_df.drop(["samples"], axis=1)

fig = plt.figure(figsize = (14,10))
x_ca_df2_h = sp.spatial.distance.pdist(x_ca_df2, "hamming")
plt.hist(x_ca_df2_h)
plt.xlabel("Hamming distance")
plt.ylabel("Frequency")
plt.title("Hamming distances for optimal MCC celltype-antibody combinations")
plt.savefig(o_ca_h)

fig = plt.figure(figsize = (14,10))
x_sample_df2_h = sp.spatial.distance.pdist(x_sample_df2, "hamming")
plt.hist(x_sample_df2_h)
plt.xlabel("Hamming distance")
plt.ylabel("Frequency")
plt.title("Hamming distances for optimal MCC sample combinations")
plt.savefig(o_sample_h)


