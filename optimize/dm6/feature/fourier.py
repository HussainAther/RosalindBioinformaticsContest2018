import matplotlib.pyplot as plt
import pandas as pd
from scipy import signal, stats
import numpy as np
import pyBigWig
import sys
import inspect
import re
import os
import ntpath

# Signal processing metrics
# Use plt.specgram to look at the read coverage distributions. That should give us the autocorrelation profiles 
# to use Fourier Transform on. Let's look over the peak regions.

if len(sys.argv) != 3:
    raise ValueError("Usage: python fourier.py coverage.bw output.tsv")
inp = sys.argv[1] # Input bigWig file of the read coverage
tsv = sys.argv[2] # Output tsv of the fourier spectrogram

basefile = tsv[:-4]

sample_name = os.path.splitext(ntpath.basename(inp))[0]

# Find the spectrograms at those areas
bw = pyBigWig.open(inp)

# Get the lengths of each of the chromosomes
chr2L_len = bw.chroms("chr2L")
chr2R_len = bw.chroms("chr2R")
chr3L_len = bw.chroms("chr3L")
chr3R_len = bw.chroms("chr3R")

fs = 1 # Sampling frequency

spec_list = [] 

temp_dict={"sample": sample_name}
chr2L_f, chr2L_t, chr2L_spec = signal.spectrogram(np.array(bw.values("chr2L", 0, chr2L_len)), fs)
plt.plot(chr2L_f, chr2L_spec.sum(axis=1))
plt.title(sample_name + " Spectrogram")
plt.xlabel("Sample frequencies")
plt.ylabel("Summed signal")
chr2L_entropy = stats.entropy(chr2L_spec.sum(axis=1)) 
plt.savefig(basefile + "_2L.png")
temp_dict["chr2L_entropy"] = chr2L_entropy

chr2R_f, chr2R_t, chr2R_spec = signal.spectrogram(np.array(bw.values("chr2R", 0, chr2R_len)), fs)
plt.plot(chr2R_f, chr2R_spec.sum(axis=1))
chr2R_entropy = stats.entropy(chr2R_spec.sum(axis=1)) 
plt.title(sample_name + " Spectrogram")
plt.xlabel("Sample frequencies")
plt.ylabel("Summed signal")
plt.savefig(basefile + "_2R.png")
temp_dict["chr2R_entropy"] = chr2R_entropy

chr3L_f, chr3L_t, chr3L_spec = signal.spectrogram(np.array(bw.values("chr3L", 0, chr3L_len)), fs)
plt.plot(chr3L_f, chr3L_spec.sum(axis=1))
chr3L_entropy = stats.entropy(chr3L_spec.sum(axis=1)) 
plt.title(sample_name + " Spectrogram")
plt.xlabel("Sample frequencies")
plt.ylabel("Summed signal")
plt.savefig(basefile + "_3L.png")
temp_dict["chr3L_entropy"] = chr3L_entropy

chr3R_f, chr3R_t, chr3R_spec = signal.spectrogram(np.array(bw.values("chr3R", 0, chr3R_len)), fs)
plt.plot(chr3R_f, chr3R_spec.sum(axis=1))
chr3R_entropy = stats.entropy(chr3R_spec.sum(axis=1)) 
plt.title(sample_name + " Spectrogram")
plt.xlabel("Sample frequencies")
plt.ylabel("Summed signal")
plt.savefig(basefile + "_3R.png")
temp_dict["chr3R_entropy"] = chr3R_entropy

spec_list.append(temp_dict)

spec_df = pd.DataFrame(spec_list)

tsv1 = pd.DataFrame.to_csv(spec_df, sep="\t")

with open(tsv, "w") as file:
    file.write(tsv1)
