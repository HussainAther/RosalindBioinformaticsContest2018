from snakemake import shell
from scipy import signal
import pandas as pd
import numpy as np
import ntpath

cc_stats = [] # List of dictionaries that will get the cross-correlation data

for file in snakemake.input:
    sample = os.path.splitext(ntpath.basename(file))[0]
    with open(file, "r") as openfile:
        temp_dict = {"sample" : sample}
        for lineno, line in openfile:
            if lineno == 2:
                forward = list(map(int(line[7:-1].split(","))))
                forward_autocorr = np.corrcoef(forward[1:-1], forward[2:])
                temp_dict["forward_autocorr"] = forward_autocorr
            if lineno == 3:
                reverse = list(map(int, line[7:-1].split(",")))
                reverse_autocorr = np.corrcoef(reverse[1:-1], reverse[2:])
                temp_dict["reverse_autocorr"] = reverse_autocorr
            if lineno == 4:
                cross_correlation = list(map(int(line[11:-1].split(","))))
                temp_dict["cross_correlation"] = cross_correlation
            if lineno == 6:
                temp_dict["alternative_lags"] = line[11:-1].split(",")
        len_dist = signal.deconvolve(cross_correlation, forward_autocorr) 
        cc_stats.append(temp_dict)

# The deconvolution of the cross-correlation signal with the autocorrelation of reads aligning to the 
# same strand

df = pd.DataFrame(cc_stats)

tsv = pd.DataFrame.to_csv(df, sep="\t")

with open(str(snakemake.output), "w") as file:
    file.write(tsv)
