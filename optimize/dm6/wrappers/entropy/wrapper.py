from snakemake import shell
from scipy import stats
import pandas as pd
import numpy as np
import ntpath

entropy = []

# Calculate the entropy of the sum of each frequency value

for file in snakemake.input:
    sample_name = os.path.splitext(ntpath.basename(file))[0]
    df = pd.DataFrame(file, sep="\t")
    temp_dict = {}
    chr2L_freq, chr2R_freq, chr3L_freq, chr4R_freq = [], [], [], []
    chr2L_freq = df.loc[df["chr"]=="chr2L"]["spectrogram"].sum(axis=1)
    for index, row in df.iterrows():
        if row["chr"] == "chr2L":
            chr2L_freq.append(row["frequency"])
        elif row["chr"] == "chr2R":
            chr2R_freq.append(row["frequency"])
        elif row["chr"] == "chr3L":
            chr3L_freq.append(row["frequency"])
        elif row["chr"] == "chr3R":
            chr3R_freq.append(row["frequency"])
    temp_dict["sample"] = sample_name
    temp_dict["chr2L_entropy"] = stats.entropy(chr2L_freq)
    temp_dict["chr2R_entropy"] = stats.entropy(sum(chr2R_freq))
    temp_dict["chr3L_entropy"] = stats.entropy(sum(chr3L_freq))
    temp_dict["chr3R_entropy"] = stats.entropy(sum(chr3R_freq))
    entropy.append(temp_dict)

entropy_df = pd.DataFrame(entropy)

tsv = pd.DataFrame.to_csv(df, sep="\t")

with open(str(snakemake.output), "w") as file:
    file.write(tsv)
