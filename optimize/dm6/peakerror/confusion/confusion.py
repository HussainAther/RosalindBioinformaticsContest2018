import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Perform confusion matrix statistical tests on the output summary.csv 

f = "/data/Lei_student/Hussain/ML/dm6/peakerror/summary.csv"
o = "/data/Lei_student/Hussain/ML/dm6/peakerror/confusion/confusion.csv"

df = pd.DataFrame.from_csv(f) # Convert the csv to a DataFrame

df["ppv"] = df["tp"] / (df["tp"] + df["fp"]) # Positive predictive value
df["fdr"] = df["fp"] / (df["tp"] + df["fp"]) # False discovery rate
df["tpr"] = df["tp"] / (df["tp"] + df["fn"]) # True positive rate
df["fpr"] = df["fp"] / (df["tn"] + df["fp"]) # False positive rate
df["fnr"] = df["fn"] / (df["tp"] + df["fn"]) # False negative rate
df["tnr"] = df["tn"] / (df["tn"] + df["fp"]) # True negative rate
df["f1score"] = 2/((1/df["tpr"]) + (1/df["ppv"])) # F1 score
df["for"] = df["fn"] / (df["fn"] + df["tn"]) # False omission rate
df["npv"] = df["tn"] / (df["fn"] + df["tn"]) # Negative predictve value
df["lr_plus"] = df["tpr"] / df["fpr"] # Positive likelihood ratio
df["lr_minus"] = df["fnr"] / df["tnr"] # Negative likelihood ratio

csv = pd.DataFrame.to_csv(df) # Convert the DataFrame to a csv

with open(o, "w") as file: # Write it to an output file
    file.write(csv)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
ax.set_title("Confusion matrix")
plt.scatter(df["fdr"])
fig.savefig("/data/Lei_student/Hussain/ML/dm6/peakerror/confusion/confusion.png")
