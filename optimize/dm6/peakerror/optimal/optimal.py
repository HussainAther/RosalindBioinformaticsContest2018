import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

f = "/data/Lei_student/Hussain/ML/dm6/peakerror/summary.csv"
out_ca = "/data/Lei_student/Hussain/ML/dm6/peakerror/optimal/optimal_ca.csv"
out_sample = "/data/Lei_student/Hussain/ML/dm6/peakerror/optimal/optimal_sample.csv"

df = pd.DataFrame.from_csv(f) # Convert the input csv files to DataFrames

df.index = df["sample"] + df["params"] # Index the DataFrames by sample and parameter combination

optimal_ca = pd.DataFrame # Initialize output DataFrames
optimal_sample = pd.DataFrame 

df["ca"] df["celltype"] + "_" + df["antibody"]
ca_list = df["ca"].unique()

df_list = []

for ca in ca_list:
    token = ca.split("_")
    c = token[0] # celltype
    a = token[1] # antibody
    m = df.loc[(df["antibody"] == a) & (df["celltype"] == c)]["mcc"].max()
    df_list.append(df.loc[df["mcc"] == m])

optimal_ca = pd.concat(df_list)

sample_list = df["sample"].unique()

df_list = []

for sample in sample_list:
    m = df.loc[df["sample"] == sample]["mcc"].max()
    df_list.append(df.loc[df["mcc"] == m])

optimal_sample = pd.concat(df_list)

# optimal_ca = df.loc[df.groupby(["sample"])["mcc"].max()] # Find the highest mcc for each celltype-antibody combo and return those rows
# optimal_sample = df.loc[df.groupby(["antibody", "celltype"])["mcc"].max()] # Highest mcc for each sample

o_ca_csv = pd.DataFrame.to_csv(optimal_ca) # Convert the DataFrame to a csv
o_sample_csv = pd.DataFrame.to_csv(optimal_sample) # Convert the DataFrame to a csv

with open(out_ca, "w") as file: # Write it to an output file
    file.write(o_ca_csv)

with open(out_sample, "w") as file:
    file.write(o_sample_csv)
