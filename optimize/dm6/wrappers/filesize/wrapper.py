from snakemake import shell
import pandas as pd
import ntpath
import numpy as np

sizes = [] # List of dictionaries that will become the DataFrame that will become the tsv

def size(file):
    return str(shell('stat --printf="%s" ' + file))

ip = []
inp = []

for file in snakemake.input.ip_bam:
    ip.append(os.path.splitext(ntpath.basename(file))[0]) # Get the ip name from the filename of the ip

for file in snakemake.input.inp_bam:
    inp.append(os.path.splitext(ntpath.basename(file))[0]) # Get the input name from filename of the input

for i, j in enumerate(ip):
    temp_dict = {"sample" : ip}
    if size("dedup/" + inp[i] + ".bam") == 0:
        temp_dict["ip_inp_ratio"] = np.nan
    else:
        temp_dict["ip_inp_ratio"] = size("dedup/" + ip[i] + ".bam") / size("dedup" + inp[i] + ".bam")
    sizes.append(temp_dict)

df = pd.DataFrame(sizes)

tsv = pd.DataFrame.to_csv(df)

with open(snakemake.output, "r") as file:
    file.write(tsv)
